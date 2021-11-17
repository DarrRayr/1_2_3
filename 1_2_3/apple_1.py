#a123_apple_1.py
import turtle as trtl
import random as rand

#-----variable----
number_of_apples = 5
letters = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
number_of_letters = 8


#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)
wn.bgpic("background.gif")

apple = trtl.Turtle()
writer = trtl.Turtle()

#-----functions-----
#   a123_apple_and_letters.py
#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. 
def move_turtle(turtle):
	
	if len(letters) > -1:
		random_position = rand.randint(-200,200)
		turtle.penup()
		turtle.setposition(random_position, 0)
		turtle.pendown()
		screen_update(turtle)


#TODO Create a function that draws a new letter from the letter list.
def pull_letter():
	global number_of_letters
	global letters
	random_letter = rand.randint(0,number_of_letters)
	current_letter = letters[random_letter]
	print(current_letter)
	letters.pop[random_letter]
	draw_letter(current_letter)
	number_of_letters -= 1
	

#TODO Create a function that takes a turtle (apple) as its parameter
# and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen

def screen_update(turtle):
	global apple_image
	global pear_image
	turtle.shape(apple_image) 
	wn.update()
	
	




#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.
for i in range(0, number_of_apples):
	current = trtl.Turtle()
	move_turtle(current)

  #Your code here

#TODO Create a function that takes a letter as its parameter, retrieve a
# random turtle (apple) and causes the turtle (apple) to drop from the tree and the letter 
# to disappear. Call the apple reseting function.
def apple_drop(letter, turtle):
	falling(turtle)
	writer.clear()

def falling(falling_turtle):
	writer.clear()
	falling_turtle.setheading(-90)
	falling_turtle.penup()
	if falling_turtle.ycor() != -200:
		falling_turtle.forward(10)
		falling(falling_turtle)

	else:
		falling_turtle.hideturtle()

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop an apple at random.

#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.

wn.listen()
trtl.mainloop()


  

#writes A/letter
def draw_letter(cur_letter):
	writer.penup()
	writer.setposition(-30,100)
	writer.pendown()
	writer.color("white")
	writer.write("cur_letter", font=("Arial", 74, "bold"))
	

#moves turtle/apple/pear down


		
	
		
	
	
#-----function calls----
pull_letter()




wn.onkeypress(falling, "")
wn.listen()
wn.mainloop()
