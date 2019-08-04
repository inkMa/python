#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import sys


def sys_test():
	argc = len(sys.argv)
	if argc > 1:
		print('%s,hello,world!'%sys.argv[1])
	else:
		print("hello! please input your name.")

if __name__ == '__main__' :
	sys_test()
else :
	print('this is a moudle.')