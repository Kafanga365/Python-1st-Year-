class Shopping:
    def __init__(self):
        self.total = 0
        
    def spend(self, amount):
        self.total += amount
        
    def checkout(self):
        if self.total >= 100:
            self.total = self.total * 0.75
        elif self.total >= 50:
            self.total = self.total * 0.9
        else:
            pass
        
        print("discount", self.discount, " total: ", self.total)
        
    
    def getTotal(self):
        return self.total
    
    
    
def main():
    cart = Shopping()
    
    print ("After initialisation - ",cart.getTotal())
    
    cart.spend(34)
    
    print("Added 34 - ", cart.getTotal())
    
    
main()