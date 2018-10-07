#!/usr/bin/python3

def sum(array):
	sum = 0
	listlen = len(array)
	print('len=%d.'%listlen)
	for i in range(listlen):
		sum += array[i]
	print('sum=%d.'%sum)


if __name__ == '__main__':
	array = [1,1,2,2,3,3]
	sum(array)