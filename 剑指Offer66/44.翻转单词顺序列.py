# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:41:59 2019

@author: Tang
"""

'''
题目描述
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。
同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。
例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，
正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
'''
def solution(s):
     s=s.split(' ')
     print(s)
     s.reverse()
     return ' '.join(s)
print(solution('student. a am I'))