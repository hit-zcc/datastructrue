#获得数组的最大值和最小值
#建立两个辅助数组，一个存储每个元素出现的个数，一个存储有多少个元素比他小

class CountSort():
    def __init__(self):
        pass
    def sort(self,list):
        result = [0 for x in range(0, len(list))]
        max,min = self.getmaxmin(list)
        tup = {}
        aft={}
        for i in range(min,max+1):
            tup[i] = 0
        for num in list:
            tup[num] = 1 if tup[num]==0 else tup[num]+1
        for key,value in tup.items():
            if key == min:
                aft[key] = 0
            else:
                aft[key] = aft[key-1]+tup[key-1]
        yy = list[::-1]
        for i in yy:
            result[aft[i]+tup[i]-1] = i
            tup[i]=tup[i]-1
        return result


    def getmaxmin(self,list):
        max = list[0]
        min = list[0]
        for num in list:
            if num>max:
                max=num
            if num<min:
                min=num
        return max,min

if __name__ == "__main__":
    sort = CountSort()
    list = [1, 5, 8, 3, 4, 1,  8, 9,  5, 6, 10, 3, 4]
    result = sort.sort(list)
    print(result)
