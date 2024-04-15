# with open('wether_data.csv') as data:
#     report = data.readlines()
#     print(report)


# import csv 

# with open('wether_data.csv') as data:
#     report = csv.reader(data)
#     for row in report:
#         if row[1] != "temp":
#             print(row[1])
        

#? pandas data analysis library to handle tabular data

import pandas 

data = pandas.read_csv('wether_data.csv')
# print(data['temp'])

# temp_list = data['temp'].to_list()
# count = len(temp_list)

# total = 0
# for val in temp_list:
#     total = total + val 

# print(total/count)


# print(data['temp'].max())

#? getting data in pandas has 2 way data['temp'] or data.temp

#?getting row 

# (0°C × 9/5) + 32 = 32°F
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'friday']

# temp = int(monday.temp)

# fh = (temp * 9/5) + 32

# print(fh)




#?creating a datat frame from scratch

# data_dict = {
#     'students' :['amy','Hari'],
#     'Scores' :[23,45]
# }

# data = pandas.DataFrame(data_dict)
# print(data)

# data.to_csv('myNewdata.csv')

#? Data analysis first with nyc data for number of squirrels

# data = pandas.read_csv('nycdata.csv')
# # print(data['Primary Fur Color'])


# data_dict ={
#     'fur colors':['Gray','Cinnamon','Black'],
#     'counts':[]
# }

# for color in data_dict["fur colors"]:
#     data_dict['counts'].append(len(data[data['Primary Fur Color']== color]))


# newInput = pandas.DataFrame(data_dict)
# newInput.to_csv('output.csv')


# #? us states finding 

import turtle
import pandas

data = pandas.read_csv('50_states.csv')

screen = turtle.Screen()
image = 'blank_states_img.gif'

screen.addshape(image)
turtle.shape(image)

guess_state=[]
Score = 0
while len(guess_state) < 50:
    answer = screen.textinput(prompt="What is the state name",title=f'Score -  {Score}')

    pos = data[data['state'] == answer]
    print(pos.x)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(int(pos.x),int(pos.y))
    t.write(answer)
    Score += 1




screen.exitonclick()