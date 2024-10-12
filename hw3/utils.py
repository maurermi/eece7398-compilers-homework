import json
import sys

def read_json_file(input):
    try:
        data = json.load(input)
        return data
    except json.JSONDecodeError:
        print(f"Error: The input does not contain valid JSON.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

def flatten_blocks(blocks):
    instrs = []
    for block in blocks:
        instrs += block
    return instrs
