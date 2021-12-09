#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 21:35:02 2021

@author: elizavetalebosina
"""
import model_2048 
from visual import *
from objects import *
from colors import *
import tkinter as tk
from tkinter import *
import tkinter.messagebox as mb


bars = []
bars_values = []


root = tk.Tk()
main_grid = tk.Frame(
        bg=GRID_COLOR, bd=3, width=400, height=400)
main_grid.grid(pady=(80, 0))

score_frame = tk.Frame()
score_frame.place(relx=0.5, y=40, anchor="center")
tk.Label(
        score_frame,
        text="Score",
        font=SCORE_LABEL_FONT).grid(
        row=0)
score_label = tk.Label(score_frame, text="0", font=SCORE_FONT)
score_label.grid(row=1)



def update_value():
    global bars_values
    global bars
    
    for i in range(4):
        for j in range (4):
            bars[i][j].value = bars_values[i][j]
        

def move_right(event):
    global bars_values
    global bars
    global score
    model_2048.final_move_right(bars_values)
    update_value()
    for row in bars:
        for bar in row:
            update_image(bar)

def move_left(event):
    global bars_values
    global bars
    global score
    model_2048.final_move_left(bars_values)
    update_value()
    for row in bars:
        for bar in row:
            update_image(bar)

def move_up(event):
    global bars_values
    global bars
    global score
    model_2048.final_move_up(bars_values)
    update_value()
    for row in bars:
        for bar in row:
            update_image(bar)


def move_down(event):
    global bars_values
    global bars
    global score
    model_2048.final_move_down(bars_values)
    update_value()
    for row in bars:
        for bar in row:
            update_image(bar)


def add_new_tile(event):
    global bars_values 
    global bars
    model_2048.append_new_value(bars_values)
    update_value()
    for row in bars:
        for bar in row:
            update_image(bar)

def update_score(event): 
    score_label.configure(text = str(model_2048.score))
    
def stop_the_game(event):
    
    if model_2048.lost(bars_values) == 0:
        msg = "Вы проиграли! Ваш результат будет сохранён"
        mb.showinfo("Конец игры", msg)
    else:
        pass

def new_game(event = ''):
    global game
    global bars
    global bars_values
    global score
    
    for i in range (4):
        row = []
        for j in range (4):
            b = Bar(i,j)
            row.append(b)
        bars.append(row)
        
    for i in range (4):
        row = []
        for j in range(4):
            bar_value = bars[i][j].value
            row.append(bar_value)
        bars_values.append(row)
        
    
        
    for row in bars:
        for bar in row:
            create_image(bar, main_grid)
    
    model_2048.append_new_value(bars_values)
    update_value()
    
    for row in bars:
        for bar in row:
            update_image(bar)
    
    root.bind('<Down>', move_down)
    root.bind('<Up>', move_up)
    root.bind('<Right>', move_right)
    root.bind('<Left>', move_left)
    
    root.bind('<Down>', add_new_tile, '+')
    root.bind('<Up>', add_new_tile, '+')
    root.bind('<Right>', add_new_tile, '+')
    root.bind('<Left>', add_new_tile, '+')
    
    root.bind('<Down>', update_score, '+')
    root.bind('<Up>', update_score, '+')
    root.bind('<Right>', update_score, '+')
    root.bind('<Left>', update_score, '+')
    
    root.bind('<Down>', stop_the_game, '+')
    root.bind('<Up>', stop_the_game, '+')
    root.bind('<Right>', stop_the_game, '+')
    root.bind('<Left>', stop_the_game, '+')
       
              
new_game()

root.mainloop()


