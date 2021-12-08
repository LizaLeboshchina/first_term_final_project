#обновление графического интерфейса


def update_image(bar):
        for i in range(4):
            for j in range(4):
                bar_value = list[i][j]
                if bar_value == 0:
                    bars[i][j]["frame"].configure(bg=c.EMPTY_CELL_COLOR)
                    bars[i][j]["number"].configure(
                        bg=c.EMPTY_CELL_COLOR, text='')
                else:
                    bars[i][j]["frame"].configure(
                        bg=c.BAR_COLORS[bar_value])
                    bars[i][j]["number"].configure(
                        bg=c.BAR_COLORS[cell_value],
                        fg=c.BAR_NUMBER_COLORS[bar_value],
                        font=c.BAR_NUMBER_FONTS[bar_value],
                        text=str(bars.values[i][j]))
                
        score_label.configure(text=score)
        update_idletasks()
    
