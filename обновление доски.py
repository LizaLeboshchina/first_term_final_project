import tkinter as tk
import random
import colors as c



def update_GUI(self):
        for i in range(4):
            for j in range(4):
                bar_value = self.matrix[i][j]
                if bar_value == 0:
                    self.bars[i][j]["frame"].configure(bg=c.EMPTY_BAR_COLOR)
                    self.bars[i][j]["number"].configure(
                        bg=c.EMPTY_BAR_COLOR, text="")
                else:
                    self.bars[i][j]["frame"].configure(
                        bg=c.BAR_COLORS[bar_value])
                    self.bars[i][j]["number"].configure(
                        bg=c.BAR_COLORS[bar_value],
                        fg=c.BAR_NUMBER_COLORS[bar_value],
                        font=c.BAR_NUMBER_FONTS[bar_value],
                        text=str(bar_value))
        self.score_label.configure(text=self.score)
        self.update_idletasks()
