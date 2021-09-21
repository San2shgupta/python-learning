print("Enter your Age or Date of birth year")
age = int(input())
while True:
    if age < 100:
        b = 2021
        a = (b - age)
        c = a + 100
        print('you are 100 years old in', c)
    elif age > 1921:
        a = age+100
        print('you are 100 years old in', a)
    elif age < 1921:
        print("You are older person")
    else:
        print("Type a valid input")
    want = int(input("Enter year you want to know how much you old in that\n"))
    if age > 1900:
        a = want-age
        print(a, "year old")
    else:
        a = 2021-age
        b = want-a
        print(b, "years old")