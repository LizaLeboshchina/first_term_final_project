#обновление графического интерфейса

from objects import *
from colors import *
import tkinter as tk
from tkinter import *



def create_image(bar, main_grid):
    '''
    Функция создаёт изображение плиток сразу ппосле их инициализации
    Выводит на экран изображение пустой доски для игры 
    На вход принимает:
        bar - плитка, объект класса Bar
        main_grid - поверхность для отрисовки доски

    '''
    bar.frame = tk.Frame(
                    main_grid,
                    bg=EMPTY_BAR_COLOR,
                    width=100,
                    height=100)
    bar.frame.grid(row=bar.i, column=bar.j, padx=5, pady=5)
    bar.number = tk.Label(main_grid, bg=EMPTY_BAR_COLOR)
    bar.number.grid(row=bar.i, column=bar.j)
    

def update_image(bar):
    '''
    Функция изменяет изображения плиток 
    Используется для обновления экрана после каждого хода
    На вход принимает:
        bar - плитка, объект класса Bar

    '''
    if bar.value == 0:
        
        bar.frame.configure(bg=EMPTY_BAR_COLOR)
        bar.number.configure(bg=EMPTY_BAR_COLOR, text='')
     
    else:
        bar.frame.configure(bg=BAR_COLORS[bar.value])
        bar.number.configure(
                        bg=BAR_COLORS[bar.value],
                        fg=BAR_NUMBER_COLORS[bar.value],
                        font=BAR_NUMBER_FONTS[bar.value],text=str(bar.value))
        


