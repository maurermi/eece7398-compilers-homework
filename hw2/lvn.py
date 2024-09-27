#!/usr/bin/env python3

import sys
from utils import read_json_file
from blocks import form_blocks, flatten_blocks
import pandas as pd

def strip_labels(data: dict):
    for func in data['functions']:
        instrs = []
        for instr in func['instrs']:
            if 'label' in instr:
                continue
            instrs.append(instr)
        func['instrs'] = instrs
    return data

def lvn(program: dict):
    # The hash table is formed as follows:
    # | hash | vn | list of canonical names |

    # The name table is formed as follows:
    # | name | vn |

    unsubstitutables = {'const', 'alloc'}
    for func in program['functions']:
        blocks = form_blocks(func)
        new_blocks = []
        for block in blocks:
            name_idx = 0
            hash_table = pd.DataFrame(columns=['vn', 'hash', 'cn'])
            name_table = {}
            for instr in block:
                if 'label' in instr:
                    continue

                new_args = []
                if 'args' in instr:
                    is_const = False
                    const_val = None
                    if 'op' in instr and instr['op'] == 'const':
                        is_const = True
                        const_val = instr['value']
                    for arg in instr['args']:
                        if arg in name_table:
                            new_args.append(name_table[arg][0])
                        else:
                            new_args.append(name_idx)
                            new_row = {'vn': name_idx, 'hash': '', 'cn': arg}
                            hash_table.loc[len(hash_table)] = new_row
                            name_table.update({arg: (name_idx, is_const, const_val)})
                            name_idx += 1
                            

                # Currently, new args contains the value number of each instr
                preimage = [instr['op']]
                if 'funcs' in instr:
                    for func in instr['funcs']:
                        preimage.append(str(func))
                for arg in new_args:
                    preimage.append(str(arg))
                hash = ''.join(preimage)

                
                # Now we have a hash by which we may index into the hash table
                if instr['op'] not in unsubstitutables and hash in hash_table['hash'].values:
                    if isinstance(instr['type'], dict):
                        if "ptr" in instr['type']:
                            if instr['op'] == 'call':
                                continue
                    # Extract the canonical name of this value number
                    cn_val = hash_table.loc[hash_table['hash'] == hash, 'cn'].values[0]
                    # If the canonical name has been reassigned, we need to handle an error
                    # In this case, we don't try to optimize this instr

                    ### here we could check and see if any other canonical names refer to this vn
                    if name_table[cn_val][0] != hash_table.loc[hash_table['hash'] == hash, 'vn'].values[0]:
                        hash_table.loc[hash_table['hash'] == hash, 'cn'] = instr['dest']
                    else:
                        instr['op'] = 'id'
                        new_val = hash_table.loc[hash_table['hash'] == hash, 'cn'].values[0]
                        is_const = name_table[new_val][1]
                        const_val = name_table[new_val][2]
                        instr['args'] = [hash_table.loc[hash_table['hash'] == hash, 'cn'].values[0]]

                        name_table[instr['dest']] = (hash_table.loc[hash_table['cn'] == cn_val, 'vn'].values[0], is_const, const_val)

                # If the hash is not in the hash table, let's see if any of the cns in the args
                # are redundant
                else:
                    # regardless add to hash table
                    if 'dest' not in instr:
                        continue
                    is_const = False
                    if 'op' in instr and instr['op'] == 'const':
                        is_const = True
                        const_val = instr['value']
                    new_row = {'vn': name_idx, 'hash': hash, 'cn': instr['dest']}
                    hash_table.loc[len(hash_table)] = new_row
                    name_table.update({instr['dest']: (name_idx, is_const, const_val)})
                    name_idx += 1

                    # try to optimize instr
                    for idx, arg in enumerate(new_args):
                        # Find the canonical name associated with the value number
                        cn_val = hash_table.loc[hash_table['vn'] == arg, 'cn'].values[0]
                        # If the canonical name has been reassigned, we need to handle an error
                        if name_table[cn_val][0] == arg:
                            instr['args'][idx] = cn_val
                        # here, likely not even worth trying to optimize the else case (but maybe)
            new_blocks.append(block)
        func = flatten_blocks(new_blocks)
    return program

if __name__ == "__main__":
    data = read_json_file(sys.stdin)
    import json
    json.dump(lvn(data), sys.stdout, indent=2)
