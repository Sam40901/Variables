print("this program will output the minimum amounts of £20, £10, £5, £2 and £1 notes and coins to make up your desired amount.")
amount = int(input("please give me your first number for me to calculate: "))

twenty = amount // 20
remainder = amount % 20
ten = remainder // 10
remainder = remainder % 10
five = remainder // 5
remainder = remainder % 5
two = remainder // 2
remainder = remainder % 2
one = remainder // 1
remainder = remainder % 1

print("the amount of £20 notes is {0}".format(twenty))
print("the amount of £10 notes is {0}".format(ten))
print("the amount of £5 notes is {0}".format(five))
print("the amount of £2 coins is {0}".format(two))
print("the amount of £1 coins is {0}".format(one))

print("thanks for using this program, made by Sam Morley, 22/9/13")

