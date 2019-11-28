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
                
    def toString():
        return string(self.ID + "\t" + self.PIN + "\t" + self.savings + "\t" + self.checking)
            
    def improperAmmount():
        print("The ammount requested is more than there is available.")
            
def confirmationMenu(acc):
    
    def press(button):
        if button == "Continue":
            app.stop()
            actionMenu(acc)
        elif button == "Switch Account":
            app.stop()
            mainMenu()
        else:
            app.stop()
            
    #updateFile(acc.toString() , acc)
            
    app = gui("Automated Teller Machine" , "400x200")
    app.setBg("red")
    
    app.addLabel("confirm" , "Confirmation Page")
    app.setLabelBg("confirm" , "white")
    
    app.addButtons(["Continue" , "Switch Account"] , press)
    app.addButtons(["Quit"] , press)
    
    app.go()
    
def transactionMenu(type , boo , acc):

    def press(button):
        if boo:
            if button == type + " savings":
                app.stop()
                confirmationMenu(acc)
            elif button == type + " checking":
                app.stop()
                confirmationMenu(acc)
        else:
            if button == type + " savings to checking":
                print(app.getEntry("Ammount"))
                acc.transfer(True , app.getEntry("Ammount"))
                app.stop()
                confirmationMenu(acc)
            elif button == type + " checking to savings":
                acc.transfer(False , (app.getEntry("Ammount")))
                app.stop()
                confirmationMenu(acc)
        if button == "Back":
            app.stop()
            actionMenu(acc)
                
    app = gui("Automated Teller Machine" , "400x200")
    app.setBg("green")
    
    app.addLabelEntry("Ammount")
    app.setFocus("Ammount")
    
    if boo:
        app.addButtons([(type + " savings") , (type + " checking")] , press)
        app.addButtons(["Back"] , press)
    else:
        app.addButtons([(type + " savings to checking") , (type + " checking to savings")] , press)
        app.addButtons(["Back"] , press)
    
    app.go()

def actionMenu(acc):

    def press(button):
        if button == "Deposit":
            app.stop()
            transactionMenu("To" , True , acc)
        elif button == "Withdraw":
            app.stop()
            transactionMenu("From" , True , acc)
        elif button == "Transfer":
            app.stop()
            transactionMenu("From" , False , acc)
        else:
            app.stop()
            mainMenu()
    
    app = gui("Automated Teller Machine" , "400x200")
    app.setBg("blue")
    
    app.addLabel("savingsBal" , ("Savings Account Balance: " + acc.getSavings()))
    app.setLabelBg("savingsBal" , "white")
    app.addLabel("checkingBal" , ("Checking Account Balance: " + acc.getChecking()))
    app.setLabelBg("checkingBal" , "white")
    app.addButtons(["Deposit" , "Withdraw" , "Transfer" , "Back"] , press)
    
    app.go()
    
def mainMenu():
    
    def press(button):
        if button == "Quit":
            app.stop()  
        elif button == "Submit":
            if checkCredentials(app.getEntry("User ID") , app.getEntry("PIN")):
                accountsFile = open("accounts.txt" , "r")
                for i in accountsFile:
                    a = createAccount(i.split("\t"))
                    if app.getEntry("User ID") == a.getID():
                        if app.getEntry("PIN") == a.getPIN():
                            accountsFile.close()
                            app.stop()
                            actionMenu(a)
            else:
                app.startSubWindow("error")
                app.errorBox("loginError" , "Invalid login credentials!")
                app.destroyAllSubWindows()
            
    app = gui("Automated Teller Machine" , "400x200")
    app.setBg("orange")
    
    app.addLabelEntry("User ID")
    app.addLabelSecretEntry("PIN")
    
    app.addButtons(["Submit" , "Quit"] , press)
    app.setFocus("User ID")
    
    app.go()
    
def checkCredentials(id , pin):
    accountsFile = open("accounts.txt" , "r")
    for i in accountsFile:
        a = createAccount(i.split("\t"))
        if id == a.getID():
            if pin == a.getPIN():
                accountsFile.close()
                return True
        
def createAccount(info):
    return Account(info[0] , info[1] , info[2] , info[3])
    
def updateFile(newLine , acc):
    accountsFile = open("accounts.txt" , "r")
    counter = 0
    for i in accountsFile:
        counter += 1
        if i.split("\t")[0] == acc.getID:
            break
    
def main():
    mainMenu()
    
if __name__ == '__main__':
    main()
