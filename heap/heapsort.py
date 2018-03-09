#
#
#  堆排序
#  每次比较当前堆得母节点和子节点的值，子节点递归调用，保证母节点的值为最大值

class heapsort():
    def __init__(self):
        pass

    def createheap(self,list,startnode):
        if 2*startnode+1>len(list):
            return
        elif 2*startnode+2>len(list):
            if (list[startnode]<list[2*startnode]):
                tmp = list[startnode]
                list[startnode] = list[2*startnode]
                list[startnode*2] = tmp
                return
        else:
            self.createheap(list,startnode*2)
            self.createheap(list,startnode*2+1)
            left_max_value = list[startnode*2]
            right_max_value = list[startnode*2+1]

            max_index=startnode*2 if left_max_value>right_max_value else startnode*2+1
            max_index=max_index if list[max_index]>list[startnode] else startnode
            if max_index != startnode:

                tmp = list[max_index]
                list[max_index] = list[startnode]
                list[startnode] = tmp
                self.createheap(list,max_index)
    def sort(self,list,tmp):
        if len(list)==1:
            return
        tmp.append(list[1])

        list[1] = list[len(list)-1]
        del list[len(list)-1]
        self.createheap(list,1)
        self.sort(list,tmp)




if __name__=="__main__":
    sort = heapsort()
    list=[-1,5,8,3,4,1,43,8,9,80,67,2,5,76,87,34,5,6,7676,3,4]
    tmp = []
    sort.createheap(list,1)
    sort.sort(list,tmp)
    print(tmp)

