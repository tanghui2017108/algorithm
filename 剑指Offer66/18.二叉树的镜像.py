# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:17:55 2019

@author: Tang
"""

'''
题目描述
操作给定的二叉树，将其变换为源二叉树的镜像。

输入描述:
二叉树的镜像定义：源二叉树 
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
'''
def solution(a):
     if a!=None:
          a.left,a.right=a.right,a.left
          solution(a.left)
          solution(a.right)
          
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     