import matplotlib.pyplot as plt
from random import randint
class Die:
    def __init__(self, num_sides=6):
        self.num_sides=num_sides
    def roll(self):
        return randint(1,self.num_sides)
from plotly.graph_objs import Bar, Layout
from plotly import offline

die=Die()
results=[]
for roll_num in range(100):
    result=die.roll()
    results.append(result)
frequencies=[]
for value in range(1,die.num_sides+1):
    frequency= results.count(value)
    frequencies.append(frequency)
x_values=list(range(1,die.num_sides+1))
data=[Bar(x=x_values,y=frequencies)]

x_axis_config={'title':'Result'}
y_axis_config={'title':'Frequency of Results'}

my_layout=Layout(title='Results of rolling one Die 100 times', xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6.html')

