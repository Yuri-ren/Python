#!coding: utf-8

#插入排序的实现


l1=[1,3,5]

##将一个num插入一个有序list中的方法 插入之后的list依然为有序
def insert_into_list(num,sort_list):
	#new_list=sort_list
	for i in range(0,len(sort_list)):
		##通过比较前后两个元素找到了要插入的位置
		if ( num>=sort_list[i]) and (num < sort_list[i+1]):
			insert_index=i
			#new_list.insert(i,num)
			#print sort_list
	#print insert_index
	sort_list.insert(insert_index+1,num)
	return sort_list


print insert_into_list(4,l1)
