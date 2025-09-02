    #Inner if statment



swapnil = input("enter your first number: ")
hridoy = input("enter your second number: ")
tanmoy = input("enter your third number: ")

if swapnil > hridoy:
    if swapnil > tanmoy:
        print(swapnil)
    else:
        print(tanmoy)

if hridoy > swapnil:
    if hridoy > tanmoy:
        print(hridoy)
    else:
        print(tanmoy)

         



# identify votting age

age = 15
def check_votting_age(age):
    if age >= 18:
        print("you are elizable to voot")
    else:
        print("you are not elezable to voot")

check_votting_age(age)        