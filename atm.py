#Anthony Gandini

from appjar import gui

class Account:

    def __init__(self , id , pin , savings , checking):
        self.ID = id
        self.PIN = pin
        self.savings = savings
        self.checking = checking
        
    def getID(self):
        return self.ID
        
    def getPIN(self):
        return self.PIN
        
    def getSavings(self):
        return self.savings
        
    def getChecking(self):
        return self.checking
        
    def withdraw(account , ammount):
        #True = savings account
        if acccount:
            if self.savings >= ammount:
                self.savings -= ammount
            else:
                improperAmmount()
        else:
            if self.checking >= ammount:
                self.checking -= ammount
            else:
                improperAmmount()
           
    def deposit(account , ammount):
        #True = savings account
        if acccount:
            self.savings += ammount
        else:
            self.checking += ammount
           
    def transfer(fromAccount , ammount):
        #True = savings account to checking
        if fromAccount:
            if self.savings >= ammount:
                self.savings -= ammount
                self.checking += ammount
            else:
                improperAmmount()
        else:
            if self.checking >= ammount:
                self.savings += ammount
                self.checking -= ammount
            else:
                improperAmmount()
            
    def improperAmmount():
        print("The ammount requested is more than there is available.")
            
            
def mainMenu():
    
    def press(button):
        if button == "Quit":
            app.stop()
    
    app = gui("Automated Teller Machine" , "400x200")
    app.setBg("orange")
    app.setFont("90")
    
    app.addLabelEntry("User ID")
    app.addLabelSecretEntry("PIN")
    
    app.addButtons(["Submit" , "Quit"] , press)
    app.setFocus("User ID")
    
    app.go()
    
def main():
    
    mainMenu()
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    