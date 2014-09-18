print("hello, this program  will calculate the volume of a swimming pool, you will need the dimensions of the deepest and shallowest ends of the swimming pool.")

print("please note that the deepest width and length will be the same as the shallow width and length.")

shallow_length = float(input("please input the shallow length: "))

shallow_width = float(input("please input the shallow width: "))

shallow_depth = float(input("please input the shallow depth: "))

deep_length = float(input("please input the deepest length: "))

deep_width = float(input("please input the deepest width: "))

deep_depth =  float(input("please input the deepest depth: "))

#this part is most likely very clunky, the only way i could think of doing this would be to use 6 variables.

print("hold on, this'll take a moment")

#maths start - the deepest length, width and depth will come up with total volume, then i will subtract.
#the triangular prism from the bottom.

deepest_total = deep_length * deep_width * deep_depth

volume_prism = shallow_width * shallow_length * (deep_depth - shallow_depth)

print("the total volume of your swimming pool is {0} centimetres cubed.".format(volume_prism))

print("thank you for using, have a nice day.")


