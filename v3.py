listx = []
lists = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
listx.append(lists[0:9])
listx.append(lists[9:18])
listx.append(lists[18:27])

date = input('month and day')
str = input('say')

m = int(date.split(' ')[0])
d = int(date.split(' ')[1])


def list_work(d,listx):
	list5 = []
	c = len(listx)
	#print(c)
	a = (d-1)%c
	if a > 0:
		for i in range(a):
			listx.append(listx[i])
			#print(i)
			#print(listx)
		for i in range(c):
			#print(i+a)
			list5.append(listx[i+a])
			#print(list5)
	else:
		list5 = listx		

	return list5

def caculate(m, listx, d, str):
	b = 0
	listx = list_work(m, listx)
	for i in listx:
		listx[b] = list_work(d, i) 
		b += 1

	for i in str:
		#print(listx)
		for x in range(len(listx)):
			if i in listx[x]:

				f = listx[x].index(i)
				g = (x+1)*10 + f + 1
				print(g, end=" ")

#caculate(m, listx, d, str)
def main(m, listx, d, str):
	if m in [1, 3, 5, 7, 8, 10, 12]:
		if d < 32:
			caculate(m, listx, d, str)
		else:
			print('day is wrong')

	elif m in [4, 6, 9, 11]:
		if d < 31:
			caculate(m, listx, d, str)
		else:
			print('day is wrong')

	elif m == 2:
		if d < 30:
			caculate(m, listx, d, str)
		else:
			print('day is wrong')

	else:
		print('month is wrong')



if __name__ == '__main__':
	main(m, listx, d, str)