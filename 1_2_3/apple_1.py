#a123_apple_1.py
import turtle as trtl
import random as rand

#-----variable----
number_of_apples = 5
letters = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
number_of_letters = 8
turtle_list = []


#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)
wn.bgpic("background.gif")


writer = trtl.Turtle()
writer.hideturtle()

trtl.Turtle()



#-----functions-----
#   a123_apple_and_letters.py
#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. 
def move_turtle(turtle):
		turtle.hideturtle()
		random_position = rand.randint(-200,200)
		turtle.penup()
		turtle.setposition(random_position, 0)
		turtle.pendown()
		screen_update(turtle)
	



#TODO Create a function that draws a new letter from the letter list.
# 1st in function order
def pull_letter():
	random_letter = rand.randint(0,8)
	current_letter = letters[random_letter]
	
	print(current_letter)
	draw_letter(current_letter)
	#gets current_letter as needed, the runs apple_drop if letter pressed
	wn.onkeypress(apple_drop, current_letter)
	
	

#TODO Create a function that takes a turtle (apple) as its parameter
# and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen

def screen_update(turtle):
	global apple_image
	global pear_image
	turtle.showturtle()
	turtle.shape(apple_image) 
	wn.update()
	
	




#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.
for i in range(0, number_of_apples):
	current = trtl.Turtle()
	turtle_list.append(current)
	move_turtle(current)

  #Your code here

#TODO Create a function that takes a letter as its parameter, retrieve a
# random turtle (apple) and causes the turtle (apple) to drop from the tree and the letter 
# to disappear. Call the apple reseting function.

#gets a random turtle and then causes for the turtle to drop
def apple_drop():
	randomturtle = rand.randint(0,4)
	in_use_turtle = turtle_list[randomturtle]
	falling(in_use_turtle)


def falling(falling_turtle):
	falling_turtle.setheading(-90)
	falling_turtle.penup()
	if falling_turtle.ycor() != -200:
		falling_turtle.forward(10)
		falling(falling_turtle)

	else:
		move_turtle(falling_turtle)
		pull_letter()
		

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop an apple at random.

#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.



  

#writes A/letter
# 2nd in function order
def draw_letter(cur_letter):
	writer.clear()
	writer.penup()
	writer.setposition(-30,100)
	writer.pendown()
	writer.color("white")
	writer.write(cur_letter, font=("Arial", 74, "bold"))
	wn.update()
	wn.onkeypress(apple_drop, cur_letter)
	wn.listen()
	


		
	
		
	
	
#-----function calls----
pull_letter()







wn.mainloop()
