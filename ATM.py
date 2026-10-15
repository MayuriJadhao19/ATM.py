class Customer:
    def __init__(self,customer_id,name):
        self.customer_id = customer_id
        self.name = name
        self.accounts = []
    def add_account(self,account):
        self.accounts.append(account)
        
class Account:
    def __init__(self,account_no,balance = 0):
        self.account_no = account_no
        self.balance = balance

#Execution of program starts here
c=Customer(123,"Mayuri")
a=Account(1,2000)
c.add_account(a)

print("Print Cstomer Details :")
print(f"Customer id:{c.customer_id}")
print(f"Customer Name :{c.name}")

#Display account details through customer object
print(f"Account No :{c.accounts[0].account_no}")
print(f"Balance :{c.accounts[0].balance}")

    
