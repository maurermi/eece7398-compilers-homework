import json
import sys
from utils import read_json_file

def form_blocks(program: dict):
    terminators = {'br', 'ret', 'jmp'}
    blocks = []
    #for func in program['functions']:
    current_block = []
    for idx, instr in enumerate(program['instrs']):
        if 'label' not in instr:
            current_block.append(instr)
        if 'label' in instr:
            blocks.append(current_block)
            current_block = [instr]
        if idx == len(program['instrs']) - 1 or 'op' in instr and instr['op'] in terminators:
            blocks.append(current_block)
            current_block = []
    return blocks

def flatten_blocks(blocks):
    instrs = []
    for block in blocks:
        instrs += block
    return instrs

if __name__ == '__main__':
    form_blocks(read_json_file(sys.stdin))