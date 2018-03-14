#!coding: utf-8

#插入排序的实现


l1=[1,2,3,4,5,6,7,8,9,10]

##将一个num插入一个有序list中的方法 插入之后的list依然为有序
def insert_into_list(num,sort_list):
	final_index=len(sort_list)-2
	last_index=len(sort_list)-1
	#print final_index
	#print last_index
	##要处理index越界的问题
	for i in range(0,len(sort_list)-1):
		print i
		#if (i+1)<=
		##通过比较前后两个元素找到了要插入的位置
		if ( num>=sort_list[i]) and (num <=sort_list[i+1]):
			insert_index=i
		else:
			##比较到了最后还是没找到最终的位置
			if i == final_index:
				print "找了一圈还是没找到适合的坑"
				insert_index=None
	if insert_index:
		sort_list.insert(insert_index+1,num)
	else:
		##找不到插入位置 直接将其插入第一个或者最后一个
		if num<=sort_list[0]:
			print ("%d 比list中任意一个元素都小~将其插入到最前面~" %(num))
			sort_list.insert(0,num)
		elif num>=sort_list[last_index]:
			print ("%d 比list中任意一个元素都大~将其插入到最后面~" %(num))
			sort_list.append(num)
	return sort_list


print insert_into_list(15,l1)
