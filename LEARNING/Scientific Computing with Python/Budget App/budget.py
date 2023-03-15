class Category:
    def __init__(self, name) -> None:
        self.name = name 
        self.ledger = [] 
        self.total = 0
    
    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})
        self.total += amount 
        
    def withdraw(self, amount, description=''):
        if self.check_funds(amount) : 
            self.ledger.append({"amount": -amount, "description": description})
            self.total -= amount 
            return True  
        else : 
            return False
        
    def get_balance(self) : return self.total 
    
    def transfer(self, amount, category) :
        if self.check_funds(amount) : 
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True  
        else : 
            return False

    def check_funds(self, amount) : return self.total >= amount 
    
    def __str__(self):
        ans = self.name.center(30, '*') + '\n'
        for transaction in self.ledger : 
            ans += transaction['description'].ljust(23)[:23] + "{0:.2f}".format(transaction['amount']).rjust(7)[-7:] + '\n'
        ans += f"Total: {self.total}"
        return ans 



def create_spend_chart(categories):
    
    # part-1 
    chart = "Percentage spent by category\n" 
    
    #part-2
    spent = []
    for item in categories : 
        spent.append(-sum([transaction['amount'] for transaction in item.ledger if transaction['amount'] < 0])) 
    s = sum(spent)
    spent = [int(i*10/s)*10 for i in spent]
    
    for graph in range(100, -1, -10) : 
        temp = f'{str(graph).rjust(3)}|'
        for perc in spent : 
            if perc >= graph : 
                temp += ' o '
            else : 
                temp += '   '
        #print(temp) 
        chart += temp + ' \n'
        
    del spent 
    
    #part-3
    chart += '    ' + "-"*(len(categories)*3+1) + '\n' 
    
    #part-4
    names = [item.name for item in categories] 
    m = max([len(name) for name in names])
    
    for i in range(m) :
        temp = ' '*4
        for j in range(len(names)) :
            try : 
                temp += names[j][i].center(3)
            except IndexError : 
                temp += ' '*3 
                
        #print(temp) 
        temp += ' \n' 
        chart += temp
        
    return chart[:-1]

