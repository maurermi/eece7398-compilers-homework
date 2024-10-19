import blocks
import json
import utils
import sys

class CFG:
    def __init__ (self, blocks: dict):
        self.blocks = blocks
    
    def __str__(self):
        str = ""
        for block_name, block in self.blocks.items():
            str += "{ "
            for pred in block.preds:
                str += pred + " "
            str += "} -> " + block.name() + " -> { "
            for succ in block.succs:
                str += succ + " "
            str += "}\n"
        return str
    
    def compute_dominators(self):
        doms = dict()
        for block_name in self.blocks:
            doms[block_name] = set(self.blocks.keys())
            
        doms[".start"] = {".start"}
        changed = True
        considered_blocks = set(self.blocks.keys()) - set([".start"])
        while changed:
            changed = False
            for block_name in considered_blocks:
                new_doms = set(self.blocks.keys())
                # The dominators of this block are the intersection 
                # of the dominators of its predecessors
                for pred in self.blocks[block_name].preds:
                    new_doms = new_doms.intersection(doms[pred])
                # Plus itself
                new_doms.add(block_name)
                # If the dominators of this block have changed, update them
                # and trigger a new iteration of the outer loop
                if new_doms != doms[block_name]:
                    doms[block_name] = new_doms
                    changed = True
        return doms

    def compute_strict_dominators(self):
        # Strict dominators are simply the dominators minus the block itself
        doms = self.compute_dominators()
        sdoms = dict()
        for block_name in self.blocks:
            sdoms[block_name] = doms[block_name] - set([block_name])
        return sdoms

    def compute_immediate_dominators(self): 
        sdoms = self.compute_strict_dominators()
        idoms = dict.fromkeys(self.blocks.keys(), None)
        for block_name in self.blocks:
            # If this block has no strict dominators, skip it
            if len(sdoms[block_name]) == 0:
                continue
            # If this block has only one strict dominator, it is its immediate dominator
            if len(sdoms[block_name]) == 1:
                idoms[block_name] = next(iter(sdoms[block_name]))
                continue
            # Otherwise, the immediate dominator is the closest common dominator
            # i.e. the strict dominator of this block that is not a strict dominator
            # of any other strict dominator of this block
            for sdom in sdoms[block_name]:
                for sdom_inner in sdoms[block_name]:
                    if sdom_inner != sdom:
                        if sdom_inner not in sdoms[sdom]:
                            idoms[block_name] = sdom_inner
                            break
        return idoms

    def compute_dominance_frontiers(self):
        dom_frontiers = dict()
        sdoms = self.compute_strict_dominators()
        for block_name in self.blocks:
            dom_frontiers[block_name] = set()
        for block_name in self.blocks:
            # The dominance frontier of a block is either a successor
            # or a successor of a successor
            check_list = list(self.blocks[block_name].succs)
            seen = set()
            while len(check_list) > 0:
                successor = check_list.pop()
                if successor in seen:
                    # prevent infinite iteration
                    continue
                elif block_name not in sdoms[successor]:
                    # if this successor is not strictly dominated by the block
                    # then it is in the dominance frontier
                    dom_frontiers[block_name].add(successor)
                else:
                    # if it is strictly dominated, add its successors to the check list
                    check_list.extend(self.blocks[successor].succs)
                seen.add(successor)

        return dom_frontiers

if __name__ == '__main__': 
    import sys

    if len(sys.argv) != 2:
        print("Usage: python data_flow.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, 'r') as file:
        program = utils.read_json_file(file)

    for func in program['functions']:
        fn_blocks = blocks.form_blocks(func)
        cfg = CFG(fn_blocks)

        print("Nodes and their dominators:")
        print(cfg.compute_dominators())
        print()
        print("Nodes and their strict dominators:")
        print(cfg.compute_strict_dominators())
        print()
        print("Nodes and their immediate dominators:")
        print(cfg.compute_immediate_dominators())
        print()
        print("Nodes and their dominance frontiers:")
        print(cfg.compute_dominance_frontiers())
        print()
        print("Dominance tree (Mermaid):")
        print(utils.make_dominance_tree_mermaid(cfg.compute_immediate_dominators()))
        make_cfg_mermaid = utils.make_cfg_mermaid(fn_blocks)
        print("Control flow graph (Mermaid):")
        print(make_cfg_mermaid)