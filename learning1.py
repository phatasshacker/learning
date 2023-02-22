#episode 1
#print('Hello, world!')

#print("Hello World!!!!!!!!!!!!!")
#print('I am captain america')
#print('I am creepy poppy')
# just learning python bruv this is a COMMENT just for HUMANS ONLY

#print("Hello world \n"  "I am captain america")

#multi-line string
#print("""Hello world
#I am captain america""")

#concatenating, Python cant read spaces
#print("I am Iron Man. " + "No, I am Tony stark. " + "No, I am Poppy ")

#or try using \n which is a new line character
#print("I am Iron Man. \n" + "No, I am Iron Man. \n")

#using * to multiply
#print("I am poppy \n" * 100)
#print("I am poppy \n" * 100 )

#episode 2
#learning about variables
#automating a robot coffee barista
print("Hello, welcome to NetWorkChuck Coffee!")

#input function

name = input("what is your name? \n")
if name != "sania":
	print("get out of here!")
else:
	print("come on in!")

if name == "tope" or name == "sania" or name == "loki":
	evil_status = input("are you evil? \n")
	good_deeds = int(input("how many good deeds have you done today? \n"))
	if evil_status == "yes" and good_deeds < 4:
		print("you are not welcome here!")
		exit()
	else:
		print("oh so youre a good " + name + " , come in boy")
else:
	print("hello " + name + ", thank you for coming in today. \n")

menu = "black coffee, rose latte, cappucino"
print(name +
      ",what would you like from the menu? Here is what we are serving. \n" +
      menu)

order = input()

if order == "black coffee":
	price = 10.00
elif order == "rose latte":
	price = 5.00
elif order == "cappucino":
	price = 12.00
else:
	print("we dont have that here")
	price = 0

quantity = input("how many coffees would you like \n")
total = price * int(quantity)
print("that sounds great " + name + ", we will have that made in a minute")

print("thank you, your total is \n", (total))
print("sounds great " + name + " we will have your " + quantity + " " + order +
      " out soon")

#episode3
#name = "Sania"

#age = 21

#print(name)
#print(age)

#print(type(name))
#print(type(age))

#actual_age = 40.90

#print(type(actual_age))

#print(5 / 7 + 9 ** 55)

#results = age + actual_age
#print(results)

