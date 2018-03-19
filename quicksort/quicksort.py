#
#
#  合并排序
# 将问题分解成为每次将两个有序的组数进行排序


class quicksort():
    def __init__(self):
        pass

    def sort(self,left,right,list):
        if left>=right:
            return
        start = left
        stop = right
        tag = list[left]
        while right!=left:
            while list[right]>tag and right>=left:
                right = right-1
            while list[left]<=tag and right>left:
                left = left+1
            if left<=right:
                tmp = list[left]
                list[left]=list[right]
                list[right] = tmp

        list[start] = list[left]
        list[left] = tag
        self.sort(start,left-1,list)
        self.sort(left+1, stop, list)











if __name__ == "__main__":

    sort = quicksort()
    list = [7, 5, 8, 3,445,56,78,0,2,3 ,4, 1, 43, 8, 9, 80, 67, 2]
    left = 0
    right = 17
    sort.sort(left,right,list)
    print(list)


