import time
from collections import OrderedDict
import re

SUM = 0
NODES = 0

def timed(f):
    def run(args):
        start_time = time.time() * 1000
        ret = f(args)
        end_time = time.time() * 1000
        print('Total time for the method: %s ms' % (end_time - start_time))
        return ret
    return run


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {} #List of node
        self.end_Of_Word = False

    def is_empty(self):
        if len(self.children) == 0:
            return True

    def add_to_tree(self, word):
        node = self
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                global NODES
                NODES += 1
                new_node = TrieNode(char)
                node.children[char] = new_node
                node.children = OrderedDict(sorted(node.children.items(), reverse=False))
                node = new_node
        node.end_Of_Word = True
        global SUM
        SUM += 1

    def print_trie(self):
        new_str = []
        if self:
            if not self.end_Of_Word:
                for key, node in self.children.items():
                    for s in node.print_trie():
                        new_str.append(key+s)
            else:
                if bool(self.children):
                    for key, node in self.children.items():
                        for s in node.print_trie():
                            new_str.append(key + s)
                new_str.append(' ')
        return new_str

    def print_trie_reverse(self):
        if self:
            if not self.is_empty():
                for key, node in self.children.items():
                    for s in node.print_trie():
                        yield key+s
            else:
                if bool(self.children):
                    for key, node in self.children.items():
                        for s in node.print_trie():
                            yield key + s
                yield ''


@timed
def load_words_and_add(root):
    with open('words.txt', 'r') as file:
        for line in file:
            for word in re.split('[,\n\r]', line):
                if word != "":
                    root.add_to_tree(word.upper())


@timed
def print_all(root):
    j = 0
    for i in list(root.print_trie()):
        j += 1
        print(i)
        print(j)
    print("")


@timed
def print_all_reverse(root):
    j = 0
    list1 = []
    for i in list(root.print_trie_reverse()):
        list1.append(i)
    list1.reverse()
    for i in list1:
        j += 1
        print(i)
        print(j)
    print("")
