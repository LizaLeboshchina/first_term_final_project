#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 21:35:02 2021

@author: elizavetalebosina
"""
from 2048_model import *
from 2048_vis import *
from 2048_objects import *
import colors as c

score = 0
bars = []
bars_values = []

game = True
        
def move_right():
    global bars.values
    global bars
    global score 
    final_move_right(bars.values)
    for bar in bars:
        change_value(bar)
    for bar in bars:
        update_image(bar)
    update_score()
        
def move_left():
    global bars.values
    global bars
    final_move_left(bars.values)
    for bar in bars:
        change_value(bar)
    for bar in bars:
        update_image(bar)
    update_score()

def move_up():
    global bars.values
    global bars
    final_move_up(bars.values)
    for bar in bars:
        change_value(bar)
    for bar in bars:
        update_image(bar)
    update_score()

def move_down():
    global bars.values
    global bars
    final_move_up(bars.values)
    for bar in bars:
        change_value(bar)
    for bar in bars:
        update_image(bar)
    update_score()


def add_new_tile():
    append_new_value(bars_values)
    for bar in bars:
        update_image(bar)
    
    
def win():
    global bars_values
    global game
    for bar_value in bars_values:
        if bar_value == 2048:
            win = True
    return win

def new_game(event = ''):
    global game
    global bars
    global bars.values
    global score
    for i in range (4):
        for j in range (4):
            b = Bar(i,j, x, y)
            bars.append(b.value)
            bars_values.append(b.value)
    append_new_value(bars.values)
    for bar in bars:
        create_image(bar)
  
    canv.bind('<Down>', move_down)
    canv.bind('<Up>', move_up)
    canv.bind('<Right>', move_right)
    canv.bind('<Left>', move_left)
    
    canv.bind('<Down>', add_new_tile, '+')
    canv.bind('<Up>', add_new_tile, '+')
    canv.bind('<Right>', add_new_tile, '+')
    canv.bind('<Left>', add_new_tile, '+')
    
    while game:
        if len(cout_empty(bars_values)) == 0:
            game = False
        if win():
            game = False
    break


def main():
    grid()
    root.title('2048')

    main_grid = tk.Frame(
        bg=c.GRID_COLOR, bd=3, width=400, height=400)
    main_grid.grid(pady=(80, 0))
    # создаем окно для вывода общего счета
    score_frame = tk.Frame(self)
    score_frame.place(relx=0.5, y=40, anchor="center")
    tk.Label(
        score_frame,
        text="Score",
        font=c.SCORE_LABEL_FONT).grid(
        row=0)
    score_label = tk.Label(score_frame, text="0", font=c.SCORE_FONT)
    score_label.grid(row=1)

    bars = []

 # создаем доску (графический интерфейс)
    def create_board(main_grid): 
        global bars 
        for i in range(4):
            row = []
            for j in range(4):
                bar_frame = tk.Frame(
                    main_grid,
                    bg=c.EMPTY_BAR_COLOR,
                    width=100,
                    height=100)
                bar_frame.grid(row=i, column=j, padx=5, pady=5)
                bar_number = tk.Label(main_grid, bg=c.EMPTY_BAR_COLOR)
                bar_number.grid(row=i, column=j)
                bar_data = {"frame": bar_frame, "number": bar_number}
                row.append(bar_data)
                bars.append(row)
        
new_game()

root.mainloop()

