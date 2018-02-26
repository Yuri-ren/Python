#-*-coding=UTF-8-*-
import random

'''
网上的代码 实现了冒泡排序
'''

class BubbleSort:
    def __init__(self,list_=[]):
        self.list_ = list_
    def get_current_list(self):
        return self.list_
    def ascent_sort(self):
        for i in range(0,len(self.list_)-1):
            for j in range(0, len(self.list_)-i-1):
                if self.list_[j]>self.list_[j+1]:
                    temp = self.list_[j]
                    self.list_[j] = self.list_[j+1]
                    self.list_[j+1] = temp

#实例化
#l1=[1,8,4,9,2]
##生成随机list
l1=random.sample(range(100000),19000)
list1 = BubbleSort(l1)
print list1.get_current_list()
list1.ascent_sort()
print list1.get_current_list()
