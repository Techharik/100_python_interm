# with open('wether_data.csv') as weather:
#     firstLine = weather.readlines()
#     print(firstLine)

# readlines have everything in a list as array

# csv default module.
# import csv

# with open('wether_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperature  = [];
#     for row in data:
#        if row[1] != 'temp':
#         temperature.append(int(row[1]))
#     print(temperature)

#we get the most readble and worable array string values.
# but here also we need to lot of work for getting values form csv

#pandas.

# import pandas as pd

# data = pd.read_csv("wether_data.csv")
# print(data["temp"])

#padas - series - daatframe:
#series - 1 dimensional
#datafrome  -2 dimensional

# data = pd.read_csv("wether_data.csv")
# data_dict = data.to_dict() # coverting a dataframe to obj or dic
# print(data_dict)

# avergage temorature finding:

# temp_list = data['temp'].to_list()
# average_temp = 0
# totalList = len(temp_list)

# for x in temp_list:
#     average_temp +=x

# result = average_temp/totalList;

# print(result)

# #or 

# average = sum(temp_list)/len(temp_list)
# print(average)

#or

# average = data['temp'].mean()
# maxi = data['temp'].max()

# print(maxi)

#? get the rows. 
# maxi = data['temp'].max()
# print(data[data.temp == maxi]) # getting row 
# print(data[data.temp == maxi].day) # getting particular data in row.

#converting faren to cel in monday

# mondaytemp = data[data.day == 'monday'].temp
# intmondaytemp = int(mondaytemp.iloc[0])
# monday_cel_temp = (intmondaytemp  * 9/5 ) + 32

# print(monday_cel_temp)


# converting the python dic to csv file.


#weather data csv is currently in celc converting that o farent

# import pandas as pd

# datafile = pd.read_csv('wether_data.csv')

# temp = datafile['temp'].tolist()

# newtemp=[];
# for f in temp:
#     faren = (f * 9/5) +32
#     newtemp.append(int(faren))



# new_data_file = {
#     "day":datafile.day.tolist(),
#     "temp":newtemp,
#     "condition":datafile.condition.tolist()
# }

# new_data_file = pd.DataFrame(new_data_file)

# new_data_file.to_html("mydata.html",index=False)


# final project gussing the date form csv file and to the map.

import turtle
import pandas as pd 


screen = turtle.Screen()
screen.title('Us States')

screen.addshape("blank_states_img.gif")

turtle.shape("blank_states_img.gif")

states_files = pd.read_csv("50_states.csv")
allstates = states_files["state"].to_list()

game_end = False

while not game_end:
        answer_state = turtle.textinput(title="enter the state name" , prompt="enter here")

        if  answer_state in allstates:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            cordinatesX = states_files[states_files['state'] == answer_state].x
            cordinatesY = states_files[states_files['state'] == answer_state].y
            t.goto(int(cordinatesX.iloc[0]),int(cordinatesY.iloc[0]))
            t.write(answer_state)
        else:
              game_end= True


screen.mainloop()