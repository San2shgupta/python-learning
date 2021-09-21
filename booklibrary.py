class Library:
    def __init__(self,List,name):
        self.listbook= List
        self.name=name
        self.lendDict={}
    def displaybook(self):
        print(f"we have following books in our library: {self.name}")
        for book in self.listbook:
            print(book)

    def lendbook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("book dict has been updatet: you can take book now")
        else:
            print(f"Book is already used by {self.lendDict[book]}")
    def addbook(self,book):
        self.listbook.append(book)
        print("Book has been added to the list")
    def returnbook(self,book):
        self.lendDict.pop(book)
if __name__ == '__main__':
    santosh = Library(['python','java','php','c++'],"Santosh")
    while(True):
        print(f"WELLCOME TO THE: {santosh.name} LIBRERY.Enter your choice to continue")
        print("1.Display boook")
        print("2.Land boook")
        print("3.Add boook")
        print("4.Return boook")
        user_choice= int(input())

        if user_choice==1:
            santosh.displaybook()
        elif user_choice==2:
            book=input("Enter the name of book you want to land:")
            name=input("enter your name:")
            santosh.lendbook(name,book)
        elif user_choice==3:
            book=input("Enter the name of the book you want to add")
            santosh.addbook(book)
        elif user_choice==4:
            book=input("Enter the name of the book you want to return")
            santosh.returnbook(book)
            print("BOOK SUCCESSFULLY RETURN")
        else:
            print('not a valid option')

        print("press q to Quite and c to Continue")
        user_choice2=input()
        if user_choice2=="q":
            quit()
        elif user_choice2=="c":
            continue
        else:
            print("Enter again")


