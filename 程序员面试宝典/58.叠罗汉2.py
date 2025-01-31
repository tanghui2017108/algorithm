# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 15:31:09 2019

@author: Tang
"""

'''
题目描述



叠罗汉是一个著名的游戏，游戏中一个人要站在另一个人的肩膀上。为了使叠成的罗汉更稳固，我们应该让上面的人比下面的人更轻一点。现在一个马戏团要表演这个节目，为了视觉效果，我们还要求下面的人的身高比上面的人高。请编写一个算法，计算最多能叠多少人，注意这里所有演员都同时出现。

给定一个二维int的数组actors，每个元素有两个值，分别代表一个演员的身高和体重。同时给定演员总数n，请返回最多能叠的人数。保证总人数小于等于500。

测试样例：
[[1,2],[3,4],[5,6],[7,8]],4
返回：4

关键点  同时出现，可以先按照身高排序，然后按照叠罗汉1的方法
'''
def getHeight(actors, n):
        # write code here
        a=[0 for j in range(n)]
        a[0]=1
        actors=sorted(actors)  
        for i in range(1,n):
            m=1
            for j in range(i):
                if  actors[i][1]>actors[j][1]:
                    if a[j]+1>m:
                        m=a[j]+1
            a[i]=m
        return max(a)