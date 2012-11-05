import sys

class TrieTreeSearch(object):

    def fileOpener(self, file_to_open):
        try:
            with open(file_to_open) as f:
                word_list = [i.strip('\r\n').split() for i in f.readlines()]
        except IOError:
            print 'Bad file path or filename, double check the filename and path.'
            return
        f.close()
        word_list = [i for v in word_list for i in v]
        separate = []
        for word in word_list:
            for letter in word:
                if not letter.isalpha():
                    separate.append(word)
        word_list = [i for i in word_list if i not in separate]
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
                    save = [i for i in back.get(keys[0]).keys() if i != None]
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
                for i in save:
                    if back.get(i).keys() == [None]:
                        final.append(prefix + i)
                    else:
                        partial = prefix
                        self.recursiveTreewalker(back, i, partial, final)
        print final
        return 


TrieTreeSearch().inputSort(sys.argv[1], sys.argv[2])


