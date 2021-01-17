import Q1
import time

PatriciaSum = 0
NODES_P = 0

def timed_p(f):
    def run(*args):
        start_time = time.time() * 1000
        ret = f(*args)
        end_time = time.time() * 1000
        print('Total time for the method: %s ms' % (end_time - start_time))
        return ret
    return run


class Patricia:
    def __init__(self, string):
        self.string = string
        self.children = {}
        self.end_of_word = False

    def add_from_trie(self, trie, new_str):
        for item in trie.children.items():
            new_str.append(item[0])
            if len(item[1].children) > 1:
                new_node = self.add(new_str, item[1].end_Of_Word)
                new_str.clear()
                new_node.add_from_trie(item[1], new_str)
            elif len(item[1].children) == 0:
                self.add(new_str, True)
                new_str.clear()
            elif item[1].end_Of_Word:
                new_node = self.add(new_str, True)
                new_str.clear()
                new_node.add_from_trie(item[1], new_str)
            else:
                self.add_from_trie(item[1], new_str)


    def add(self, str_list, boolean):
        string = ''.join(str_list)
        node = Patricia(string)
        global NODES_P
        NODES_P += 1
        node.end_of_word = boolean
        self.children[string] = node
        if boolean:
            global PatriciaSum
            PatriciaSum += 1
        return node


@timed_p
def start_to_add(patricia_root, trie):
    patricia_root.add_from_trie(trie, [])


