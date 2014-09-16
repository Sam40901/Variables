print("hello, this program will ask for the dimensions of a lift and a fridge, and work out how much space will be left in the lift once the fridge is inside.")

lift_height = float(input("please enter the lifts height: "))

lift_width = float(input("please enter the lifts width : "))

lift_depth = float(input("please enter the lifts width : "))

lift_volume = lift_height * lift_width * lift_depth

print("the lifts total volume equals {0}".format(lift_volume))

fridge_height = float(input("please enter the fridges height : "))

fridge_width = float(input("please enter the frigdes width : "))

fridge_depth = float(input("please enter the fridges depth: "))

fridge_volume = fridge_height * fridge_width * fridge_depth

print("the fridges total volume equals {0}".format(fridge_volume))

answer_volume = lift_volume - fridge_volume

print("the total space left in the lift is {0}".format(answer_volume))

print("thanks for using this program")
