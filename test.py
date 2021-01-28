import collections

""" This is the class representing a person. It will save the name and balance. It receives as parameters the name and initial balance of the person. """
class Person:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    
    def printBalance(self):
        print(f"{self.name}'s balance: {self.balance}")
        
""" This is the class that will do the banking operations. It will save all transactions and print them. It will also settle debts.  """        
class Bank:
    def __init__(self):
        self.transactions = []
        
    def transaction(self, lender, borrower, value):
        lender.balance += value
        borrower.balance -= value
        
        self.transactions.append({
            "borrower" : borrower,
            "lender": lender,
            "value" : value 
        })
        
    def printAllTransactions(self):
        for transaction in self.transactions:
            print(f"{transaction['lender'].name} lent {str(transaction['value'])} bucks to {transaction['borrower'].name}")
            
    def printTransactions(self, person):
        print(f"{person.name}'s Transactions: \n")
        
        for transaction in self.transactions:
            if transaction['borrower'] == person:
                print(f"{person.name} borrowed {transaction['value']} bucks from {transaction['lender'].name}")
                
            elif transaction['lender'] == person:
                print(f"{person.name} lend {transaction['value']} bucks to {transaction['borrower'].name}")
    
    def printFullExtract(self, person):
        
        extract = {
            "name": person.name,
            "balance": person.balance,
            "credits": [],
            "debts": []
        }
        
        ''' Loop through transactions and create two dicts with credits and debts related to the person '''
        for transaction in self.transactions:
            if transaction['borrower'] == person:
                extract['debts'].append({ transaction['lender'].name: transaction['value'] })
                
            elif transaction['lender'] == person:
                extract['credits'].append({ transaction['borrower'].name: transaction['value'] })
        
        counterCred = collections.Counter() 
        counterDebt = collections.Counter() 
            
        ''' Uses the collections lib to sum transactions to the same person in the credits and debts dicts '''
        for c in extract['credits']:
            counterCred.update(c)
        
        extract['credits'] = dict(counterCred) 
        
        for d in extract['debts']:
            counterDebt.update(d)
        
        extract['debts'] = dict(counterDebt) 
        
        print(extract)
        
    def debtsToPerson(self, person, owesTo):
        debtSum = 0
        
        for transaction in self.transactions:
            if transaction['borrower'] == person and transaction['lender'] == owesTo:
                debtSum += transaction['value']
        
        return debtSum
    
    ''' def clearDebts(self, person, owesTo):
        owedDebt = self.debtsToPerson(person, owesTo)
        debtToReceive = self.debtsToPerson(owesTo, person)
        
        if debtToReceive > owedDebt:
            
            for index, transaction in self.transactions:
                if transaction['borrower'] == person and transaction['lender'] == owesTo:
                    if transaction['value'] < owedDebt:
                        owedDebt -= transaction['value']
                        transaction.remove(index) '''
                           
        
''' Creates Bank object '''
bank = Bank()
    
''' Creates the Persons objects '''
joao = Person("João")
maria = Person("Maria")
pedro = Person("Pedro")
ze = Person("Zé")
cebola = Person("Cebola")
charlinho = Person("Charlinho")

""" Transactions : Lender, (Borrower, Value) """
bank.transaction(maria, joao, 10)
bank.transaction(maria, joao, 15)
bank.transaction(joao, pedro, 15)
bank.transaction(joao, pedro, 15)
bank.transaction(cebola, ze, 50)
bank.transaction(joao, charlinho, 30)
bank.transaction(joao, maria, 30)
''' End of transactions '''

''' Print all transactions: '''
bank.printAllTransactions

''' Print all transactions from one person: '''
bank.printTransactions(joao)

''' Print Bank Extract '''
bank.printFullExtract(joao)




    
