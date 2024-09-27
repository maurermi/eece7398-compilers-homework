#!/usr/bin/env python3

from utils import read_json_file
from blocks import form_blocks, flatten_blocks
import sys
import json

def hash_instr(instr):
    hash = ''
    for (key, value) in instr:
        hash = hash.join([key, value])

def dce(program: dict):
    # This contains program instructions
    blocks = form_blocks(program) # This is a list of lists
    new_blocks = []
    for block in blocks:
        converged = False
        new_block = block
        while not converged:
            unused_indexes = set()
            last_def = dict() # Mapping of variables that have been defined but not yet used
            for idx, instr in enumerate(block):
                if 'args' in instr:
                    for arg in instr['args']:
                        last_def.pop(arg, '')
                if 'dest' in instr:
                    if instr['dest'] in last_def:
                        unused_indexes.add(last_def[instr['dest']])
                    last_def.update({instr['dest']: idx})

            if(len(unused_indexes) == 0):
                converged = True
            new_block = []
            for idx, instr in enumerate(block):
                if idx in unused_indexes:
                    continue
                new_block.append(instr)
            block = new_block

        new_blocks.append(new_block)
    return flatten_blocks(new_blocks)
            

if __name__ == '__main__':
    program = read_json_file(sys.stdin)
    # instrs = dce(program)
    for function in program['functions']:
        instrs = dce(function)
        function['instrs'] = instrs
    json.dump(program, sys.stdout, indent=2)