#  红黑树
#  1.根节点是黑色
#  2.节点不是黑色就是红色
#  3.红色节点的子节点不能是红色
#  4.从根节点到所有子节点经过的黑色节点个数相同
#  5.空节点都是黑色节点


# 节点数据结构需要维护的信息
#   1）左右节点的引用
#   2）当前节点的颜色
#   3）父节点的引用
#   4）当前节点的值

RED = 1
BLACK = 2
class Red_Black_Tree_Node():

    def __init__(self,value,color = RED):
        self.value = value
        self.left_node = None
        self.right_node = None
        self.color = color
        self.parent = None

    def set_color(self,color):
        self.color = color

    def is_leaf_node(self):
        if self.left_node or self.right_node:
            return False
        else:
            return True

    def is_root_node(self):
        if self.parent:
            return True
        else:
            return False

    def set_left_node(self,node):
        self.left_node = node
        if node is None:
            return
        node.parent = self

    def set_right_node(self,node):
        self.right_node = node
        if node is None:
            return
        node.parent = self

    def get_parent_direct_to_me(self):
        if self.parent.left_node is self:
            return 'left'
        elif self.parent.right_node is self:
            return 'right'

    def get_parent_direct_to_brother(self):
        if self.parent.left_node is self:
            return 'right'
        elif self.parent.right_node is self:
            return 'left'

    def get_brother(self):
        if self.get_parent_direct_to_brother() == 'left':
            return self.parent.left_node
        else:
            return self.parent.right_node

class Red_Black_Tree():
    def __init__(self,root):
        self.root = root
        root.set_color(BLACK)

    def insert(self,node,from_node=None):
        if not from_node:
            from_node = self.root
        if node.value>from_node.value and from_node.right_node is not None:
            self.insert(node,from_node.right_node)
        elif node.value>from_node.value and from_node.right_node is None:
            from_node.set_right_node(node)
            self.rebalance(node)
        elif node.value<from_node.value and from_node.left_node is not None:
            self.insert(node,from_node.left_node)
        elif node.value<from_node.value and from_node.left_node is  None:
            from_node.set_left_node(node)
            self.rebalance(node)
        else:
            raise RuntimeError('unexcept condition in insert')

    def rebalance(self,node):
        #当前节点为根节点
        if  node.parent == None:
            self.root = node
            self.root.color = BLACK
            return
        #情况一：当前节点的父节点为黑色不需要进行调整
        if node.parent.color == BLACK:
            return
        #当父节点是红色，分下列情况
        else:
            #1.父节点的兄弟节点也是红色->父节点和兄弟节点都变味黑色，祖父节点变为红色，以祖父节点继续开始
            if node.parent.get_brother() is not None and node.parent.get_brother().color == RED:
                node.parent.get_brother().color = BLACK
                node.parent.color = BLACK
                node.parent.parent.color= RED
                self.rebalance(node.parent.parent)

            # 1.父节点是右节点，自己是右节->父亲变为黑色，祖父变成红色 指向祖父节点 ，左旋
            elif node.get_parent_direct_to_me() == 'right' and node.parent.get_parent_direct_to_me() == 'right':
                node.parent.color = BLACK
                node.parent.parent.color = RED
                head = node.parent.parent
                self.trun_left(head)
                self.rebalance(head)
            # 1.父节点的兄弟节点是黑色->父节点变为黑色，祖父节点变为红色，在祖父节点为支点右旋
            elif node.get_parent_direct_to_me() == 'left' and  node.parent.get_parent_direct_to_me() == 'left':
                node.parent.color = BLACK
                node.parent.parent.color = RED
                head = node.parent.parent
                self.trun_right(head)
                self.rebalance(head)
            #指向父节点 右旋
            elif node.get_parent_direct_to_me() == 'left' and  node.parent.get_parent_direct_to_me() == 'right':
                head = node.parent
                self.trun_right(head)
                self.rebalance(head)
            #指向父节点，左旋
            elif node.get_parent_direct_to_me() == 'right' and  node.parent.get_parent_direct_to_me() == 'left':
                head = node.parent
                self.trun_left(head)
                self.rebalance(head)
#左旋操作

    def trun_left(self,node):
        if node.parent is not None:
            direct = node.get_parent_direct_to_me()
        parent_node = node.parent

        right_child = node.right_node
        right_child_left_node = node.right_node.left_node

        right_child.set_left_node (node)
        node.set_right_node (right_child_left_node)


        if parent_node is None:
            self.root = right_child
            right_child .parent = None
        else:
            if direct == 'left':
                parent_node.set_left_node ( right_child)
            else:
                parent_node.set_right_node (right_child)

#右旋操作
    def trun_right(self,node):
        if node.parent is not None:  
            direct = node.get_parent_direct_to_me()
        parent_node = node.parent

        left_child = node.left_node
        left_child_right_node = node.left_node.right_node

        left_child.set_right_node (node)
        node.set_left_node(left_child_right_node)

        if parent_node is None:
            self.root = left_child
            left_child .parent = None
        else:
            if direct == 'left':
                parent_node.set_left_node (left_child)
            else:
                parent_node.set_right_node ( left_child)

#测试代码
if __name__=="__main__":
    # ====================  测试左转  =================
    # q = Red_Black_Tree_Node(5)
    # w = Red_Black_Tree_Node(13)
    # e = Red_Black_Tree_Node(10)
    # e.set_left_node(q)
    # e.set_right_node(w)
    # r = Red_Black_Tree_Node(16)
    #
    # t = Red_Black_Tree_Node(17)
    # y = Red_Black_Tree_Node(18)
    # t.set_right_node(y)
    # t.set_left_node(r)
    #
    # a = Red_Black_Tree_Node(15)
    # s = Red_Black_Tree_Node(20)
    #
    # a.set_left_node(e)
    # a.set_right_node(t)
    #
    # s.set_left_node(a)
    # tree = Red_Black_Tree (s)
    # tree.trun_left(a)
    #====================  测试右转  =================
    # q = Red_Black_Tree_Node(5)
    # w = Red_Black_Tree_Node(13)
    # e = Red_Black_Tree_Node(10)
    # e.set_left_node(q)
    # e.set_right_node(w)
    # r = Red_Black_Tree_Node(16)
    #
    # t = Red_Black_Tree_Node(17)
    # y = Red_Black_Tree_Node(18)
    # t.set_right_node(y)
    # t.set_left_node(r)
    #
    # a = Red_Black_Tree_Node(15)
    # s = Red_Black_Tree_Node(20)
    #
    # a.set_left_node(e)
    # a.set_right_node(t)
    #
    # s.set_left_node(a)
    # tree = Red_Black_Tree (s)
    # tree.trun_right(e)
    # print ('ee')


    #====================  测试插入  =================
    q = Red_Black_Tree_Node(5)
    w = Red_Black_Tree_Node(13)
    e = Red_Black_Tree_Node(10)
    r = Red_Black_Tree_Node(16)

    t = Red_Black_Tree_Node(17)
    y = Red_Black_Tree_Node(18)

    a = Red_Black_Tree_Node(15)
    s = Red_Black_Tree_Node(20)


    tree = Red_Black_Tree(r)
    tree.insert(q)
    tree.insert(w)
    tree.insert(y)
    tree.insert(e)
    tree.insert(t)
    tree.insert(a)
    tree.insert(s)
    print ('over')
    pass

