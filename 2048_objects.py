import random

colors = dict()

colors['0'] = '#a3a3a3'
colors['2'] = '#deb976'
colors['4'] = '#ede0c8'
colors['8'] = '#edc850'
colors['16'] = '#edc53f'
colors['32'] = '#f67c5f'
colors['64'] = '#f65e3b'
colors['128'] = '#edcf72'
colors['256'] = '#edcc61'
colors['512'] = '#f2b179'
colors['1024'] = '#f59563'
colors['2048'] = '#edc22e'

class Bar:
    def __init__(self, i, j):
        self.value = 0
        self.color = colors[str(self.value)]
        self.i = i
        self.j = j

    def change_color(self,value):
        self.color = colors[str(self.value)]


b = Bar(0,0,4)

b.value = 2
b.change_color()

print(b.color)

bars = []
bars.value

for i in range(4):
    for j in range(4):
        b = Bar(i,j)
        bars.append(b)
        bars.value.append(b.value)

if len(count_empty(bars.value)) !=0:
    append_new_value(bars.values)
    for i in range(4):
        for j in range(4):
            bars[i][j].value = bars.values[i][j]
        






