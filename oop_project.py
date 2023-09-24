from bank_app import * 

Ali = BankAccount(1000,'Ali')
Osman = BankAccount(2000,'Osman')
Omar = BankAccount(3000,'Omar')

Ali.getBalance()
Osman.getBalance()
Omar.getBalance()

Ali.deposit(500)

Osman.withdraw(10000)

Omar.transfer(1000,Ali)

Talha = InterestRewardsAcct(5000,'Talha')
Talha.getBalance()
Talha.deposit(3000)
Talha.transfer(300,Osman)

Amin = SavingsAcct(7000,'Amin')
Amin.getBalance()
Amin.deposit(3000)
Amin.transfer(8000,Talha)