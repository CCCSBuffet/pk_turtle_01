import turtle as t

def main():
	trtl = t.Turtle(visible=False)
	trtl.penup()
	trtl.goto(-100, -100)
	trtl.pendown()
	length = 120
	while length > 20:
		trtl.forward(length)
		trtl.left(47)
		length = length - 1

	_ = input('hit enter to exit ')

if __name__ == '__main__':
	main()
