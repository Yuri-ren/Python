#!coding: utf-8
'''
python实现一个冒泡排序算法
自己实现
'''

import os
import random


##生成随机list
l1=random.sample(range(10000),1900)

#l1=[9,1,7,4,8,2,4,3,6,10,5]


def paopao(l):
	#print len(l)
	#print l[0]
	#print l[len(l)-1]
	temp_l=[]
	for i in range(0,len(l)-1):
		##对list中的每个元素以及下一个元素进行比较
		current_num=l[i]
		next_num=l[i+1]
		if current_num <=next_num:
			##
			temp_l.append(current_num)
		else:
			pass

##交换list元素的方法
def change_list(l):
	count=0
	while (count<len(l)):
		##第一遍循环过去 可以保证最大的元素落在了最后面
		for i in range(0,len(l)-1):
			if l[i]>=l[i+1]:
				##前面的元素大于后面的，交换之
				temp=l[i]
				l[i]=l[i+1]
				l[i+1]=temp
				#print l
			else:
				##前后元素已经符合顺序 无需操作
				pass
		#print l
		count=count+1
		#print count
	print l

if __name__=="__main__":
	print "list初始顺序:"
	print l1
	print "*****end*****"
	print "开始排序"
	change_list(l1)
	print "*****end*****"
	#paopao(l1)
