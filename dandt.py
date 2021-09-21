#SANTOSH GUPTA
#BHAI MAIN NAYA HU , ABHI 7 DAYS HUA HAI CODING ME : TRY KIYA AS FUN
import random
print("This is Dare Or true Game by San2sh")
a = int(input("1 for dare \n2 for true\n"))
list = [ "Sing a song !", "Dance 1 minuets!", "Kiss me!", "Give me your number!"]
list1 = ["Who is your crush?", "Loves someone?", "Kissed anyone?", "Sleep with stranger?"]
choice = random.choice(list)
choice1 = random.choice(list1)


if a==1:
    print(choice)
elif a>2:
    print("wrong input")
else:
    print(choice1)
