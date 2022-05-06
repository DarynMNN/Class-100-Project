from threading import activeCount


class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin
    def CheckBalance(self):
        print("your balance is 50,000")
    def Withdrawl(self, amount):
        new_amount = 50000 - amount
        print("you have withdrawled amount "+str(amount)+".your remaining balance  "+str(new_amount))
def main():
    Card_number = input("insert your card number:->")
    pin_number = input("enter your pin number:->")
    new_user = Atm(Card_number, pin_number)
    print("choose your activity")
    print("1.Balance inquiry  2.Withdrawl")
    activity = int(input("enter activity number:->"))
    if(activity==1):
        new_user.CheckBalance()
    elif(activity==2):
        amount = int(input("enter the amount:-> "))
        new_user.Withdrawl(amount)
    else:
        print("enter a valid number")
if __name__ == "__main__":
    main()

