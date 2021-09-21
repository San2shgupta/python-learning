import datetime

def now():
    return datetime.datetime.now()


def san():
    c = int(input("Enter 1 for Exersise 2 for show\n"))
    if (c==1):

        value = input("Type Here\n")
        with open("santosh-exer.txt", "a") as fl:
            fl.write(str([(now())]) + ":" + value + "\n")
        print("Successfully Written")
    elif (c == 2):
        a = open("santosh-exer.txt")
        print(a.read())
    return san()
def sasi():
    c = int(input("Enter 1 for Exersise 2 for show\n"))
    if c==1:
        value=input("Type Here\n")
        with open("sasikant-exer.txt", "a") as fl:
            fl.write(str([(now())]) + ":" + value + "\n")
        print("SUCCESSFULLY WRITTEN....")
    elif(c==2):
        a = open("sasikant-exer.txt")
        print(a.read())
    return sasi()

a = int(input("1 for santosh, 2 for Sashikant\n"))
if a==1:
    print(san())
elif(a==2):
    print(sasi())