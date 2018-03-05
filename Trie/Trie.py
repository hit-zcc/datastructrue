# -*- coding: utf-8 -*-
# 字典树实现
#
#
# 1、字典树用边表示字母
#
# 2、有相同前缀的单词公用前缀节点，那我们可以的得出每个节点最多有26个子节点（在单词只包含小写字母的情况下）
#
# 3、整棵树的根节点是空的。为什么呢？便于插入和查找，这将会在后面解释。
#
# 4、每个单词结束的时候用一个特殊字符表示，图中用的‘′，那么从根节点到任意一个‘
# ’所经过的边的所有字母表示一个单词。
class Trie_Node():
    def __init__(self):
        self.count = 0
        self.isend=False
        self.node = {}
    def insert(self,word):
        if len(word) == 0:
            self.set_isend(True)
            self.count+=1
            return

        if self.node.get(word[0]):
            value = self.node.get(word[0])
            self.count+=1
            value.insert(word[1:])
        else:
            node = Trie_Node()

            self.node[word[0]] = node
            self.count+=1
            node.insert(word[1:])
    def set_isend(self,bl):
        self.isend=bl
    def find(self,word):
        if len(word) == 0:
            return (self.isend,self.count)
        if self.node.get(word[0]):
            value = self.node.get(word[0])
            return value.find(word[1:])

        else:
            return False
if __name__=="__main__":
    t = Trie_Node()
    t.insert('banana')
    t.insert('band')
    t.insert('bee')
    t.insert('absolute')
    print(t.find('ba'))
    print(t.find('b'))
    print(t.find('band'))
    print(t.find('abc'))