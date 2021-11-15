#   a123_apple_1.py
import turtle as trtl

#-----variable----

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

def draw_apple(active_apple):
  active_apple.shape(pear_image)
  wn.update()

#writes A/letter
def letter():
	writer.penup()
	writer.setposition(-30,100)
	writer.pendown()
	writer.color("white")
	writer.write("A", font=("Arial", 74, "bold"))
	writer.hideturtle()

#moves turtle/apple/pear down
def falling():
	writer.clear()
	apple.setheading(-90)
	apple.penup()
	if apple.ycor() != -200:
		apple.forward(10)
		falling()
		
		
	else:
		print("fell")
	
	
#-----function calls----

draw_apple(apple)
letter()
wn.onkeypress(falling, "a")
wn.listen()
wn.mainloop()