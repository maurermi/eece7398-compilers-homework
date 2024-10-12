import sys
from utils import read_json_file

class Block:
    def __init__(self, instrs: list, id, preds: set, succs: set):
        self.instrs = instrs
        self.id = id
        self.preds = preds
        self.succs = succs
    
    def __str__(self):
        return f"Instructions: {self.instrs}\n ID: {self.id}\n Predecessors: {self.preds}\n Successors: {self.succs}\n"
    
    def name(self):
        return self.id

def form_blocks(program: dict):
    terminators = {'br', 'ret', 'jmp'}
    blocks = dict()

    current_block_id = ".start"
    current_block = Block([], current_block_id, set(), set())
    last_term = False
    for idx, instr in enumerate(program['instrs']):
        if 'label' not in instr:
            # if there is no current block, we have not properly created one beforehand -- this should never happen if this program is correct
            if not current_block:
                print("ERROR: No current block")
                exit(1)
            # append the instruction like any other
            current_block.instrs.append(instr)

        if 'label' in instr: # we may have a fallthrough
            label = instr['label']
            if current_block:
                if not last_term: # i.e. if this is a fallthrough, then this new block is a successor of the current block
                    current_block.succs = set([instr['label']])
                blocks.update({current_block_id: current_block}) # regardless add the current block to the list

            # update the current block
            current_block = Block([instr], instr['label'], set([current_block_id]), set())
            if not last_term: # if the last block was a fallthrough, then the last block is a predecessor
                # it's possible that this is a new label, so we check and update accordingly
                if label not in blocks:
                    new_block = Block([], label, set(), set())
                    blocks.update({label: new_block})
                blocks[label].preds.add(current_block_id)
                current_block = blocks[label]
            # update the current block id to match this new block
            current_block_id = instr['label']

        if idx == len(program['instrs']) - 1: # this is the last instruction in the program
            if not current_block:
                print("ERROR: No current block")
                exit(1)
            # this is the last instruction we will handle regardless of whether the next is a terminator
            blocks.update({current_block_id: current_block})
            break # exit the loop
        elif 'op' in instr and instr['op'] in terminators:
            # we have a terminator instruction
            op = instr['op']
            if op == 'br':
                # if there is a branch, there are two possible successors of this block
                current_block.succs.add(instr['labels'][0])
                current_block.succs.add(instr['labels'][1])

                # also update the 'preds' of the successor blocks or create these blocks if they are new to us
                if instr['labels'][0] in blocks:
                    blocks[instr['labels'][0]].preds.add(current_block_id)
                else:
                    new_block = Block([instr], instr['labels'], set([current_block_id]), set())
                    blocks.update({instr['labels'][0]: new_block})
                
                if instr['labels'][1] in blocks:
                    blocks[instr['labels'][1]].preds.add(current_block_id)
                else:
                    new_block = Block([instr], instr['labels'], set([current_block_id]), set())
                    blocks.update({instr['labels'][1]: new_block})

            elif op == 'jmp':
                # if there is a jump, there is only one possible successor of this block
                current_block.succs.add(instr['labels'][0])
                if instr['labels'][0] in blocks:
                    blocks[instr['labels'][0]].preds.add(current_block_id)
                else:
                    new_block = Block([instr], instr['labels'], set([current_block_id]), set())
                    blocks.update({instr['labels'][0]: new_block})

            # if there is a return, it is to another function, so we ignore this as the scope changes

            blocks.update({current_block_id: current_block})
            # no matter what, we expect a label after this instr, so this current block will get replaced
            current_block = None
            last_term = True # this is so we don't consider the next instruction as a fallthrough
        elif last_term:
            last_term = False
    for block, blockval in blocks.items():
        print("printing blocks")
        print(block, "\n", blockval)
    return blocks

def flatten_blocks(blocks):
    instrs = []
    for block in blocks:
        instrs += block
    return instrs

if __name__ == '__main__':
    form_blocks(read_json_file(sys.stdin))