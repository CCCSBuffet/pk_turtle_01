import turtle as t

def main():
	screen = t.getscreen()
	trtl = t.Turtle(visible=False)
	trtl.hideturtle()
	trtl.penup()
	trtl.goto(-100, 0)
	trtl.pendown()
	flag = True
	for x in range(36):
		if flag:
			trtl.pendown()
		else:
			trtl.penup()
		flag = not flag
		trtl.forward(200)
		trtl.left(170)

	_ = input('hit enter to exit ')

if __name__ == '__main__':
	main()
