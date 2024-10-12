'''
Here, we are defining a data flow analysis for "reaching definitions"
'''

import blocks
import utils
from collections import deque
from typing import Callable
import copy

class Analysis():
    def __init__(self, forward: bool, merge: Callable[list, list], transfer: Callable[[dict, blocks.Block], dict]):
        self.forward = forward
        self.init = init
        self.merge = merge
        self.transfer = transfer
    
    def merge(self, b_ins: list):
        return self.merge(b_ins)
    
    def transfer(self, b_in: dict, block: blocks.Block):
        return self.transfer(b_in, block)

    def data_flow(self, blocks):
        worklist = deque(blocks.keys())
        in_edges = dict.fromkeys(blocks.keys(), [])
        out_edges = dict.fromkeys(blocks.keys(), [])

        for (block_id, block) in blocks.items():
            in_edges[block_id] = dict()
            out_edges[block_id] = dict()

        if self.forward:
            worklist.reverse()

        while len(worklist) > 0:
            block_id = worklist.pop()
            block = copy.deepcopy(blocks[block_id])
            in_edges[block_id] = copy.deepcopy(self.merge([copy.deepcopy(out_edges[p]) for p in block.preds]))
            b_out = self.transfer(copy.deepcopy(in_edges[block_id]), copy.deepcopy(block))
            if out_edges[block_id] != b_out:
                out_edges[block_id] = copy.deepcopy(b_out)
                if self.forward:
                    for s in block.succs:
                        if s is not None:
                            worklist.append(s)
                else:
                    for p in block.preds:
                        if p is not None:
                            worklist.append(p)
        return in_edges, out_edges

def reaching_merge_function(b_ins: list):
    b_out = dict()
    for b_in in b_ins:
        for elem in b_in:
            if elem in b_out:
                if b_in[elem][0] in b_out[elem]:
                    continue
                b_out[elem].append(b_in[elem][0])
            else:
                b_out[elem] = b_in[elem]
    return b_out

def reaching_transfer_function(b_in: dict, block: blocks.Block):
    defs = dict()
    for i, instr in enumerate(block.instrs):
        if 'dest' in instr:
            dest = instr['dest']
            if dest in b_in:
                # now the previous definition is killed
                del b_in[dest]
            # add the new definition as a list of instructions
            # we use a list because the merge may have multiple definitions of the same variable
            defs[dest] = [block.id + "_" + str(i)]
    return b_in | defs

if __name__ == '__main__': 
    import sys

    if len(sys.argv) != 2:
        print("Usage: python data_flow.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, 'r') as file:
        program = utils.read_json_file(file)

    analysis = Analysis(True, dict(), reaching_merge_function, reaching_transfer_function)
    for func in program['functions']:
        fn_blocks = blocks.form_blocks(func)
        in_edges, out_edges = analysis.data_flow(fn_blocks)
        print()
        for i in range(len(in_edges)):
            print("block_id: ", list(in_edges.keys())[i])
            print("in_edges: ", in_edges[list(in_edges.keys())[i]])
            print("out_edges: ", out_edges[list(out_edges.keys())[i]])
            print()
