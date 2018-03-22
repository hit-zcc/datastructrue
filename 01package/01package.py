#01背包：寻求子问题的最优解

class package():
    def __init__(self):
        pass
    def choose(self,weight,value,index,capacity):
        if capacity<=0: return 0
        if index==0 and capacity>=weight[0]:
            return value[0]
        elif index==0:return 0
        else:
            return max(self.choose(weight,value,index-1,capacity),
                       self.choose(weight,value,index-1,capacity-weight[index])+value[index])


if __name__ == "__main__":
    package = package()
    weight = [5,6,4]
    value = [20,10,12]
    print(package.choose(weight,value,2,10))

