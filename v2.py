
lists = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
list1 = lists[0:9]
list2 = lists[9:18]
list3 = lists[18:27]
list4 = []

date = input('month and day')
str = input('say')

m = int(date.split(' ')[0])
d = int(date.split(' ')[1])

#change lists order
def list_change(m,list1,list2,list3,list4):
	if (m-1)%3 == 1:
		list4 = list1
		list1 = list2
		list2 = list3
		list3 = list4

	if (m-1)%3 == 2:
		list4 = list1
		list1 = list3
		list3 = list2
		list2 = list4
	
	list_all = [list1,list2,list3]

	return list_all

#change elements order in list
def list_work(d,listx):
	list5 = []
	a = (d-1)%9
	if a > 0:
		for i in range(a):
			listx.append(listx[i])
		for i in range(9):
			list5.append(listx[i+a])
	else:
		list5 = listx		

	return list5

#caculate the position changed
def caculate(d, m, lists, list1, list2, list3, list4, str):
	for i in str:
		if i in lists:
			if i in list1:
				list_index = [1,3,2]
				x1 = list_index[(m-1)%3]
				
				list_all =list_change(m, list1, list2, list3, list4)
				
				x2 = list_work(d,list_all[x1-1]).index(i)

				x1 = x1*10 + x2 + 1
				print(x1, end=" ")

			if i in list2:
				list_index = [2,1,3]
				x1 = list_index[(m-1)%3]

				list_all =list_change(m, list1, list2, list3, list4)
				x2 = list_work(d,list_all[x1-1]).index(i)

				x1 = x1*10 + x2 + 1
				print(x1, end=" ")

			if i in list3:
				list_index = [3,2,1]
				x1 = list_index[(m-1)%3]

				list_all =list_change(m, list1, list2, list3, list4)
				x2 = list_work(d,list_all[x1-1]).index(i)

				x1 = x1*10 + x2 + 1
				print(x1, end=" ")

		else:
			print('str is not right')
			break

#start work
if m in [1, 3, 5, 7, 8, 10, 12]:
	if d < 32:
		caculate(d, m, lists, list1, list2, list3, list4, str)
	else:
		print('day is wrong')

elif m in [4, 6, 9, 11]:
	if d < 31:
		caculate(d, m, list1, list2, list3, list4, str)
	else:
		print('day is wrong')

elif m == 2:
	if d < 30:
		caculate(d, m, list1, list2, list3, list4, str)
	else:
		print('day is wrong')

else:
	print('month is wrong')