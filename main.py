import turtle as t

def main():
	screen = t.getscreen()
	trtl = t.Turtle(visible=False)
	trtl.hideturtle()
	trtl.penup()
	trtl.goto(-100, 0)
	trtl.pendown()
	c = 0
	for x in range(12):
		trtl.forward(200)
		trtl.left(150)
		c = c + 0.08
		trtl.pencolor((c, c, c))
	_ = input('hit enter to exit ')

if __name__ == '__main__':
	main()
