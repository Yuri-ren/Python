#!coding: utf-8

import random,os
#插入排序的实现


l1=[1,2,3,4,5,6,7,8,9,10]

#随机生成一个list
l1=random.sample(range(100),19)
print l1
#l1=sorted(l1)
#print l1
#os._exit(-1)
#l1=[0,3,4,8,15,19,21,25,26,32,33,44,58,65,73,76,82,84,89]

##将一个num插入一个有序list中的方法 插入之后的list依然为有序
def insert_into_list(num,sort_list):
	#final_index=len(sort_list)-2
	#last_index=len(sort_list)-1
	if num <sort_list[0]:
		print ("%d 比list中任意一个元素都小~将其插入到最前面~" %(num))
		sort_list.insert(0,num)
	elif num >sort_list[len(sort_list)-1]:
		print ("%d 比list中任意一个元素都大~将其插入到最后面~" %(num))
		sort_list.append(num)
	else:	
		final_index=len(sort_list)-2
		last_index=len(sort_list)-1
		##要处理index越界的问题 通过前后元素的比较 必然能找到适合插入的位置
		for i in range(0,len(sort_list)-1):
			#print i,sort_list[i],sort_list[i+1]
			##通过比较前后两个元素找到了要插入的位置
			if ( num>=sort_list[i]) and (num <=sort_list[i+1]):
				insert_index=i
		print ("开始插入数据,成为有序list的第%d个元素" %(insert_index+2))
		sort_list.insert(insert_index+1,num)
	return sort_list

##储存最后排序完成的list
sorted_list=[]
sorted_list.append(l1[0])
print sorted_list
for i in range(1,len(l1)-1):
	#print l1[i]
	sorted_list=insert_into_list(l1[i],sorted_list)
print sorted_list

