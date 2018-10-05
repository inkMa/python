#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import sys


def sys_test():
	print('%s,hello,world!'%sys.argv[1])


if __name__ == '__main__' :
	sys_test()
else :
	print('this is a moudle.')