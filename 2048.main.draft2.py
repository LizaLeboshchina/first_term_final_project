from 2048_model import *
from 2048_vis import *
from 2048_objects import *

score = 0
bars = []
bars_values = []

game = True


def main():
    grid()
    master.title('2048')

    main_grid = tk.Frame(
        bg=c.GRID_COLOR, bd=3, width=400, height=400)
    main_grid.grid(pady=(80, 0))


 # создаем доску (графический интерфейс)
        bars = []
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


    
   



