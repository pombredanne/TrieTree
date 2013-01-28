import sys
import re

class TrieTreeSearch(object):

    def fileOpener(self, file_to_open):
        try:
            with open(file_to_open) as f:
                word_list = [i for v in f.readlines() for i in re.findall('[A-Za-z]+', v)]
        except IOError:
            print 'Bad file path or filename, double check the filename and path.'
            return
        return word_list

    def treeCreator(self, words):
        tree = dict()
        if words == None:
            return
        for word in words:
            current_node = tree
            for letter in word:
                current_node = current_node.setdefault(letter, {})
            current_node = current_node.setdefault(None, None)
        return tree     

    def recursiveTreewalker(self, tree, key, partial, final):
        if tree.get(key).keys() == [None]:
            final.append(partial + key)
        else:
            partial += key
            for v in tree.get(key).keys():
                if v == None:
                    final.append(partial)
                if v != None:
                    self.recursiveTreewalker(tree.get(key), v, partial, final)

    def inputSort(self, prefix, data):
        keys = [i for i in prefix]
        back = self.treeCreator(self.fileOpener(data))
        if back == None:
            return
        final = []
        save = []
        while keys:
            if len(keys) == 1:
                try:
                    save = [i for i in back.get(keys[0]).keys()]
                    back = back.get(keys[0])
                except AttributeError:
                    print 'Dictionary has no words with that prefix.'
                    break
            else:
                try:
                    back = back.get(keys[0])
                except AttributeError:
                    print 'Dictionary has no words with that prefix.'
                    break
            keys = keys[1:]
            if save:
                for j in save:
                    if j != None:
                        if back.get(j).keys() == [None]:
                            final.append(prefix + j)
                        else:
                            partial = prefix
                            self.recursiveTreewalker(back, j, partial, final)
                    if j == None:
                        final.append(prefix)
        print final
        return 

if __name__ == '__main__':
    trie = TrieTreeSearch()
    trie.inputSort(sys.argv[1], sys.argv[2])

