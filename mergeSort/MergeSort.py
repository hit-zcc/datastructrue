#
#
#  合并排序
# 将问题分解成为每次将两个有序的组数进行排序

class Mergesort():
    def __init__(self):
        pass
    def sort(self,list,start,stop):
        listtmp = []
        if stop>start:
            listl = self.sort(list,start,int((stop-start)/2)+start)
            listr = self.sort(list,int((stop-start)/2)+start+1,stop)
            rindex = 0
            lindex = 0
            while  rindex<len(listr) and lindex<len(listl):
                   if listr[rindex]<listl[lindex]:
                       listtmp.append(listr[rindex])
                       rindex+=1
                   else:
                        listtmp.append(listl[lindex])
                        lindex+=1
            listtmp.extend(listr[rindex:])
            listtmp.extend(listl[lindex:])
            return listtmp

        else:
            listtmp .append(list[start])
            return listtmp



if __name__=="__main__":
    sort = Mergesort()
    list=[7,5,8,3,4,1,43,8,9,80,67,2]
    print (sort.sort(list,0,11))