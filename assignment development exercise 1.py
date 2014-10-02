print("hello, this program will ask you for two numbers, divide one by the other, give you the integer and the variable.")

number_1 =  int(input("please enter your first number: "))

number_2 = int(input("please enter your second number: "))

number_integer = number_1 // number_2
number_remainder = number_1 % number_2

print("your answer is *drumroll please*")

print("the integer of your equation equals {0}".format(number_integer))
print("the remainder of your equation equals {0}".format(number_remainder))

print("thanks for using!")
