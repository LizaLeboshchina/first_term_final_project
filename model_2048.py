#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 12:47:21 2021

@author: elizavetalebosina
"""
'''

Математическая модель движения и сложения плиток в игре 2048
Движение разбито на 3 составляющие:
    1) оценка возможного смещения (asses_pos_direction)
    2) подготовительное смещение - положение плиток до сложения (prep_move_direction)
    3) сложение (sum_direction))


'''
list = [[0,2,2,0], [2,0,2,0], [0,8,0,0], [2,16,0,0]] # список для проверки работы функций 

def norm_print(list):
    '''
    Функция является тестовой
    Печатает двумерный массив в виде таблицы
    Написана для удобной проверки работы функций, не будет использоваться в финальной программе
    '''
    print('-'*10)
    for row in list:
        print(*row)
    print('-'*10)


def asses_pos_down(i,j):
    pos = 0
    if i==3:
        pos = 0
    else:
        if list[i+1][j] == 0:
            pos+=1
        if i <=1:
            if list[i+2][j] ==0 and list[i+1][j] ==0:
                pos+=1
    return pos

def prep_move_down(list):
    for k in range (4):
        for i in range(4):
            for j in range (4):
                pos = asses_pos_down(i,j)
                if pos == 1:
                    list[i][j],list[i+1][j] = list[i+1][j],list[i][j]
                elif pos ==2:
                    list[i][j],list[i+2][j] = list[i+2][j],list[i][j]
                
    return list
def sum_down(list):
    for k in range (4):
        for i in range(3):
            for j in range(4): 
                if list[i+1][j] == list[i][j]:
                    list[i+1][j] = 2*list[i+1][j]
                    list[i][j] = 0
    

def final_move_down(list):
    prep_move_down(list)
    sum_down(list)
    return(list)

def asses_pos_up(i,j):
    pos = 0
    if i==0:
        pos = 0
    else:
        if list[i-1][j] == 0:
            pos+=1
        if i >=2:
            if list[i-2][j] ==0 and list[i-1][j] ==0:
                pos+=1
    return pos

def prep_move_up(list):
    for k in range (4):
        for i in range(4):
            for j in range (4):
                pos = asses_pos_up(i,j)
                if pos == 1:
                    list[i][j],list[i-1][j] = list[i-1][j],list[i][j]
                elif pos ==2:
                    list[i][j],list[i-2][j] = list[i-2][j],list[i][j]
                
    return list
def sum_up(list):
    for k in range (4):
        for i in range(1,4):
            for j in range(4): 
                if list[i-1][j] == list[i][j]:
                    list[i-1][j] = 2*list[i-1][j]
                    list[i][j] = 0
    

def final_move_up(list):
    prep_move_up(list)
    sum_up(list)
    return(list)

def asses_pos_left(i,j):
    pos = 0
    if j==0:
        pos = 0
    else:
        if list[i][j-1] == 0:
            pos+=1
        if j >=2:
            if list[i][j-2] ==0 and list[i][j-1] ==0:
                pos+=1
    return pos


def prep_move_left(list):
    for k in range (4):
        for i in range(4):
            for j in range (4):
                pos = asses_pos_left(i,j)
                if pos == 1:
                    list[i][j],list[i][j-1] = list[i][j-1],list[i][j]
                elif pos ==2:
                    list[i][j],list[i][j-2] = list[i][j-2],list[i][j]
                
    return list
def sum_left(list):
    for k in range (4):
        for i in range(4):
            for j in range(1,4): 
                if list[i][j-1] == list[i][j]:
                    list[i][j-1] = 2*list[i][j-1]
                    list[i][j] = 0
    

def final_move_left(list):
    prep_move_left(list)
    sum_left(list)
    return(list)

def asses_pos_right(i,j):
    pos = 0
    if j==3:
        pos = 0
    else:
        if list[i][j+1] == 0:
            pos+=1
        if j <=1:
            if list[i][j+2] ==0 and list[i][j+1] ==0:
                pos+=1
    return pos


def prep_move_right(list):
    for k in range (4):
        for i in range(4):
            for j in range (4):
                pos = asses_pos_right(i,j)
                if pos == 1:
                    list[i][j],list[i][j+1] = list[i][j+1],list[i][j]
                elif pos ==2:
                    list[i][j],list[i][j+2] = list[i][j+2],list[i][j]
                
    return list
def sum_right(list):
    for k in range (4):
        for i in range(4):
            for j in range(3): 
                if list[i][j+1] == list[i][j]:
                    list[i][j+1] = 2*list[i][j+1]
                    list[i][j] = 0
    

def final_move_right(list):
    prep_move_right(list)
    sum_right(list)
    return(list)



# Проверка корректной работы функций 

norm_print(list)
norm_print(final_move_up(list))