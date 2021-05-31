class atm:
    def __init__(self,cardNumber,pinNumber):
        self.balance = 10000
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
    def cashWithdrawl(self):
        cw = int(input('enter the amount to withdraw:-   '))
        if cw<10000:
            self.balance = self.balance-cw
        else: 
            print('amount is not present in the acc.')    

    def balanceEnquiry(self):
        print(self.balance)
  
def name():
    cardNo = input('enter the card no.:-  ')
    pinNo = input('enter the pin number:- ')

    user1 = atm(cardNo,pinNo)
    user1.cashWithdrawl()
    user1.balanceEnquiry()
    
name()    