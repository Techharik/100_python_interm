# from turtle import Turtle,Screen

# import random

# tim = Turtle()


# # for _ in range(15):
# #     tim.forward(100)
# #     tim.color("white")
# #     tim.forward(10)
# #     tim.color("black")

# #tuple - similar to list.
# my_tuple=(1,0,2)  #cannot change the value from the fiven list

# # my_tuple[2]=12; #immutable

# # my_tuple[0] #->accesing the variable from tuple

# # print(my_tuple)
# # color=['red','green','blue','yellow','orange','brown','aqua','violet']
# # direction = [0,90,180,270]
# # for silde in range(3,10):
   
# #     tim.color(random.choice(color))
    
# #     for _ in range(silde):
# #         angles = 360 / silde
# #         tim.forward(100)
# #         tim.right(angles)



# # tim.pensize(12)
# tim.speed("fastest")

# # for _ in range(200):
# #     tim.color(random.choice(color))
# #     tim.forward(40)
# #     tim.left(random.choice(direction))


# # for _ in range(100):
# #     tim.color(random.choice(color))
# #     tim.circle(100)
# #     current_heading = tim.heading()
# #     tim.setheading(current_heading +10)

# import colorgram


# # colors = colorgram.extract('images.jfif', 6)

# # print(colors)


# # rgb_color =[]

# # for color in colors:
# #      r= color.rgb.r
# #      g= color.rgb.g
# #      b= color.rgb.b
# #      new_color = (r,g,b)
# #      rgb_color.append(new_color)

# # print(rgb_color)

# color_list =[(244, 238, 226), (220, 230, 242), (245, 227, 237), (225, 242, 231)]


# for _ in range(100):
#      tim.dot(20,random.choice(color_list))
#      tim.forword(50) 



# screen = Screen()
# screen.exitonclick()




# #All the ways to import module:

# # import turtle
# # time = turtle.Turtle()

# # from turtle import Turtle || * everything in the module

# #import turtle as t

# #Installing modules :- 



import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)









screen = turtle_module.Screen()
screen.exitonclick()