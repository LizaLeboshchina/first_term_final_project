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



import random 
import copy
from copy import deepcopy 


#list = [[0,2,2,0], [2,0,2,0], [0,8,0,0], [2,16,0,0]] # список для проверки работы функций 

score = 0

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


def asses_pos_down(i,j, list):
    '''
    Функция оценивает максимально возможное смещение элемента вниз
    Принимает: 
        i - строка, в которой находится элемент в списке global list
        j - столбец, в котором находится элемент в списке global list
        Возвращает pos - колличество ячеек, на которое можно сместиться вниз
    '''
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
    '''
    Функция осуществляет максимальное смещение всех элементов вниз
    Максимальное смещение расчитывается с помощью функции asses_pos_down
    На вход принимает:
        list - спсиок, в котором необходимо провести смещение 

  
    '''
    
    for k in range (4):
        for i in range(4):
            for j in range (4):
                pos = asses_pos_down(i,j, list)
                if pos == 1:
                    list[i][j],list[i+1][j] = list[i+1][j],list[i][j]
                elif pos ==2:
                    list[i][j],list[i+2][j] = list[i+2][j],list[i][j]           


def sum_down(old_list):
    '''
    Функция осуществляет суммирование элементов списка по правилам игры 2048 
    Принимает: 
        old_list - список, который нужно модифицировать 
    '''
    new_list = copy.deepcopy(old_list)
    global score 
    for i in range(3):
        for j in range(4): 
            if old_list[i+1][j] == old_list[i][j]:
                new_list[i+1][j] = 2*old_list[i+1][j]
                score += old_list[i+1][j]
                new_list[i][j] = 0 
    for x in range (4):
        for y in range (4):
            old_list[x][y] = new_list[x][y]
    

    

def final_move_down(list):
    '''
    Функция осуществляет движение вниз по правилам игры 2048, то есть смещение и сложение элементов одновременно
    На вход принимает:
        list - список, который необходимо модифицировать 
    Возврщает :
        тот же список list c требуемой модификацией 
    
    '''
    prep_move_down(list)
    sum_down(list)
    return list


def asses_pos_up(i,j, list):
    '''
    Функция оценивает максимально возможное смещение элемента ввверх
    Принимает: 
        i - строка, в которой находится элемент в списке global list
        j - столбец, в котором находится элемент в списке global list
        Возвращает pos - колличество ячеек, на которое можно сместиться вверх
    '''
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
    '''
    Функция осуществляет максимальное смещение всех элементов вверх
    Максимальное смещение расчитывается с помощью функции asses_pos_up
    На вход принимает:
        list - спсиок, в котором необходимо провести смещение 

  
    '''
    for k in range (4):
        for i in range(4):
            for j in range (4):
                pos = asses_pos_up(i,j, list)
                if pos == 1:
                    list[i][j],list[i-1][j] = list[i-1][j],list[i][j]
                elif pos ==2:
                    list[i][j],list[i-2][j] = list[i-2][j],list[i][j]
                
    return list


def sum_up(old_list):
    '''
    Функция осуществляет суммирование элементов списка по правилам игры 2048 
    Принимает: 
        old_list - список, который нужно модифицировать 
    '''
    new_list = copy.deepcopy(old_list)
    global score 
    for i in range(1,4):
        for j in range(4): 
            if old_list[i-1][j] == old_list[i][j]:
                new_list[i-1][j] = 2*old_list[i-1][j]
                score += old_list[i-1][j]
                new_list[i][j] = 0 
    for x in range (4):
        for y in range (4):
            old_list[x][y] = new_list[x][y]
    


def final_move_up(list):
    '''
    Функция осуществляет движение вверх по правилам игры 2048, то есть смещение и сложение элементов одновременно
    На вход принимает:
        list - список, который необходимо модифицировать 
    Возврщает :
        тот же список list c требуемой модификацией 
    
    '''
    prep_move_up(list)
    sum_up(list)
    return(list)


def asses_pos_left(i,j, list):
    '''
    Функция оценивает максимально возможное смещение элемента влево
    Принимает: 
        i - строка, в которой находится элемент в списке global list
        j - столбец, в котором находится элемент в списке global list
        Возвращает pos - колличество ячеек, на которое можно сместиться влево
    '''
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
    '''
    Функция осуществляет максимальное смещение всех элементов влево
    Максимальное смещение расчитывается с помощью функции asses_pos_left
    На вход принимает:
        list - спсиок, в котором необходимо провести смещение 
    '''
    for k in range (4):
        for i in range(4):
            for j in range (4):
                pos = asses_pos_left(i,j, list)
                if pos == 1:
                    list[i][j],list[i][j-1] = list[i][j-1],list[i][j]
                elif pos ==2:
                    list[i][j],list[i][j-2] = list[i][j-2],list[i][j]
                
    return list

def sum_left(old_list):
    '''
    Функция осуществляет суммирование элементов списка по правилам игры 2048 
    Принимает: 
        old_list - список, который нужно модифицировать 
    '''
    new_list = copy.deepcopy(old_list)
    global score 
    for i in range(4):
        for j in range(1,4): 
            if old_list[i][j-1] == old_list[i][j]:
                new_list[i][j-1] = 2*old_list[i][j-1]
                score += old_list[i][j-1]
                new_list[i][j] = 0 
    for x in range (4):
        for y in range (4):
            old_list[x][y] = new_list[x][y]
    

def final_move_left(list):
    '''
    Функция осуществляет движение влево по правилам игры 2048, то есть смещение и сложение элементов одновременно
    На вход принимает:
        list - список, который необходимо модифицировать 
    Возврщает :
        тот же список list c требуемой модификацией 
    
    '''
    prep_move_left(list)
    sum_left(list)
    return(list)

def asses_pos_right(i,j, list):
    '''
    Функция оценивает максимально возможное смещение элемента вправо
    Принимает: 
        i - строка, в которой находится элемент в списке global list
        j - столбец, в котором находится элемент в списке global list
        Возвращает pos - колличество ячеек, на которое можно сместиться вправо
    '''
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
    '''
    Функция осузествляет максимальное смещение всех элементов вправо
    Максимальное смещение расчитывается с помощью функции asses_pos_right
    На вход принимает:
        list - спсиок, в котором необходимо провести смещение 

  
    '''
    for k in range (4):
        for i in range(4):
            for j in range (4):
                pos = asses_pos_right(i,j,list)
                if pos == 1:
                    list[i][j],list[i][j+1] = list[i][j+1],list[i][j]
                elif pos ==2:
                    list[i][j],list[i][j+2] = list[i][j+2],list[i][j]
                
    return list


def sum_right(old_list):
    '''
    Функция осуществляет суммирование элементов списка по правилам игры 2048 
    Принимает: 
        old_list - список, который нужно модифицировать 
    '''
    new_list = copy.deepcopy(old_list)
    global score 
    for i in range(4):
        for j in range(3): 
            if old_list[i][j+1] == old_list[i][j]:
                new_list[i][j+1] = 2*old_list[i][j+1]
                score += old_list[i][j+1]
                new_list[i][j] = 0 
    for x in range (4):
        for y in range (4):
            old_list[x][y] = new_list[x][y]
    

def final_move_right(list):
    '''
    Функция осуществляет движение вправо по правилам игры 2048, то есть смещение и сложение элементов одновременно
    На вход принимает:
        list - список, который необходимо модифицировать 
    Возврщает :
        тот же список list c требуемой модификацией 
    
    '''
    prep_move_right(list)
    sum_right(list)
    return(list)


def count_empty(list):
    '''
    Функция принимает на вход двумерный список - list
    Возвращает список координат нулевых элементов 

    '''
    empty = []
    for i in range (4):
        for j in range (4):
            if list[i][j] == 0:
                empty.append([i,j])
    return empty


def append_new_value(list):
    '''
    Функция принимает на вход двумерный список - list
    Заменяет рандомный нулевой элемент на 2

    '''
    if len(count_empty(list)) == 0:
        pass
    else:
        index= random.randrange(0, len(count_empty(list))) 
        coord = count_empty(list)[index]
        list[coord[0]][coord[1]] = 2
    return list

def lost(list):

    loose = 0
    
    for i in range (4):
        for j in range (4):
            loose+= asses_pos_left(i,j, list) + asses_pos_right(i,j, list) + asses_pos_up(i,j, list) + asses_pos_down(i,j, list)
    
    for i in range (4):
        for j in range (3):
            if list[i][j] == list[i][j+1]:
                loose+= 1
    for i in range (4):
        for j in range (1,4):
            if list[i][j] == list[i][j-1]:
                loose+= 1
    for i in range (3):
        for j in range (4):
            if list[i][j] == list[i+1][j]:
                loose+= 1
    for i in range (1,4):
        for j in range (4):
            if list[i][j] == list[i-1][j]:
                loose+= 1
                      
    return loose
                


def win(list):
    victory = False
    for i in range(4):
        for j in range (4):
            if list[i][j] == 2048:
                victory = True
    return victory 

def save_to_file(file):
    
    '''
    Функция сохраняет счёт в файл
    На вход принимает файл, в который нужно созранить сяёт - file 
    '''
    with open (file, 'w'):
        file.write(str(score))


# Проверка корректной работы функций 

#norm_print(list)
#norm_print(final_move_left(list))
#print(score)

#norm_print(final_move_down(list))
#print(score)
