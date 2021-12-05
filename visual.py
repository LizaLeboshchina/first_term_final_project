#Экран: 400х480, отступ 80 сверху для подсчета очков, отступы у плиток от границ по 5.


coords = [[[5,85],[105,85],[205,85],[305,85]],     #1 строка плиток
          [[5,185],[105,185],[205,185],[305,185]],  #2 строка плиток
          [[5,285],[105,285],[205,285],[305,285]],  #3 строка плиток
          [[5,385],[105,385],[205,385],[305,385]]]   #4 строка плиток


for i in range(4):
    for j in range (4):
        bar = Bar(i, j, x, y)

def create_image(bar):
    bar.image = canv.label(text = str(bar.value),
                           bg = bar.color,
                           fg = bar.number.color[bar.value]
                        ).place(x = bar.x,
                                y = bar.y
                            )
    
def update_image(bar):
    bar.image = canv.label(x = bar.x,
                           y = bar.y,
                           text = str(bar.value),
                           bg = bar.color,
                           fg = bar.number.color[bar.value]
                        ).place(x = bar.x,
                                y = bar.y
                            )
    
    
