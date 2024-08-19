class CoffeeShopApp:
    
    def __init__(self):
        self.newCustomerName = StringVar()
        
    def createWidgets(self):
        customerEntry = Entry(
            self.mainFrame,
            textvariable=self.newCustomerName
            )
        customerEntry.grid(
            row=0
            column=0,
            )