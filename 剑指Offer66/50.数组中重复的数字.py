# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:06:23 2019

@author: Tang
"""

'''
题目描述


在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，
但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
'''
def solution(data,k):
     dic=dict()
     for i in data:
          if i in dic:
               if i==k:
                    return True
          else:
               dic[i]=1
          