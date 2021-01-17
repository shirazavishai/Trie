import Q1
import Q1d
import Q2

##Trie
print("Q1:")
trie = Q1.TrieNode(' ')
print("Load Words : ")
Q1.load_words_and_add(trie)
print(" %d words" % Q1.SUM)
Q1.print_all(trie)
print("")
Q1.print_all_reverse(trie)
print("done Q1")

#Trie using Patricia
print("\nQ1d:")
patricia = Q1d.Patricia('')
print("Add words: ")
Q1d.start_to_add(patricia, trie)
print("Number of nodes in patricia tree = ", Q1d.NODES_P)
print("Number of nodes in trie = ", Q1.NODES)
print("done Q1d")

