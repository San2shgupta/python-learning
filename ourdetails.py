print("enter name which detailsyou want know")
a = input("santosh, mannu, guddu, arbind\n")


class details:
    def printdetails(self):
        return f"Name is:- {self.name}," \
               f"\nMobile no :-{self.mob}," \
               f"\nMarit status:- {self.merit}," \
               f"\nHome town:- {self.home}"

santosh = details()
santosh.name = "SANTOSH GUPTA"
santosh.mob = "8724052258"
santosh.merit = "UNMARRIED"
santosh.home = "NAGPURA"

mannu = details()
mannu.name = "MANNU GUPTA"
mannu.mob = "6387453507"
mannu.merit = "UNMARRIED"
mannu.home = "NAGPURA"

guddu = details()
guddu.name = "SASHIKANT GUPTA"
guddu.mob = "9910294220"
guddu.merit = "MARRIED"
guddu.home = "NAGPURA"

arbind = details()
arbind.name = "ARVIND GUPTA"
arbind.mob = "7068342959"
arbind.merit = "MARRIED"
arbind.home = "NAGPURA"


if a=='santosh':
    print("here is the details about SANTOSH:--\n",santosh.printdetails())
elif a=='mannu':
    print("here is the details about MANNU:--\n",mannu.printdetails())
elif a=='guddu':
    print("here is the details about GUDDU:--\n",guddu.printdetails())
elif a=='arbind':
    print("here is the details about ARBIND:--\n",arbind.printdetails())
else:
    print("WRONG INPUT")