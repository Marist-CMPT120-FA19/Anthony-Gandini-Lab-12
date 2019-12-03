#Anthony Gandini

from appjar import gui

class Account:

    def __init__(self , id , pin , savings , checking):
        self.ID = str(id)
        self.PIN = pin
        self.savings = int(savings)
        self.checking = int(checking)
        
    def getID(self):
        return str(self.ID)
        
    def getPIN(self):
        return self.PIN
        
    def getSavings(self):
        return self.savings
        
    def getChecking(self):
        return self.checking
        
    def withdraw(self , account , ammount):
        #True = savings account
        if account:
            self.savings -= int(ammount)
        else:
            self.checking -= int(ammount)
           
    def deposit(self , account , ammount):
        #True = savings account
        if account:
            self.savings += int(ammount)
        else:
            self.checking += int(ammount)
           
    def transfer(self , fromAccount , ammount):
        #True = savings account to checking
        if fromAccount:
            self.savings -= int(ammount)
            self.checking += int(ammount)
        else:
            self.savings += int(ammount)
            self.checking -= int(ammount)
                
    def toString(self):
        return str(str(self.ID) + "\t" + str(self.PIN) + "\t" + str(self.savings) + "\t" + str(self.checking))
            
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
            
    updateFile(acc.toString() , acc)
            
    app = gui("Automated Teller Machine" , "400x200")
    app.setBg("red")
    
    app.addLabel("confirm" , "Confirmation Page")
    app.setLabelBg("confirm" , "white")
    app.addLabel("msg" , "Transaction Complete")
    app.setLabelBg("msg" , "white")
    
    app.addButtons(["Continue" , "Switch Account"] , press)
    app.addButtons(["Quit"] , press)
    
    app.go()
    
def transactionMenu(type , boo , acc):

    def press(button):
        if boo:
            if button == type + " savings":
                if type == "To":
                    acc.deposit(True , app.getEntry("Ammount"))
                    app.stop()
                    confirmationMenu(acc)
                else:
                    if int(app.getEntry("Ammount")) < acc.getSavings():
                        acc.withdraw(True , app.getEntry("Ammount"))
                        app.stop()
                        confirmationMenu(acc)
                    else:
                        app.startSubWindow("error")
                        app.errorBox("TransactionError" , "Not enough funds in savings account!")
                        app.destroyAllSubWindows()
            elif button == type + " checking":
                if type == "To":
                    acc.deposit(False , app.getEntry("Ammount"))
                    app.stop()
                    confirmationMenu(acc)
                else:
                    if int(app.getEntry("Ammount")) < acc.getChecking():
                        acc.withdraw(False , app.getEntry("Ammount"))
                        app.stop()
                        confirmationMenu(acc)
                    else:
                        app.startSubWindow("error")
                        app.errorBox("TransactionError" , "Not enough funds in checking account!")
                        app.destroyAllSubWindows()
        else:
            if button == type + " savings to checking":
                if int(app.getEntry("Ammount")) < acc.getSavings():
                    acc.transfer(True , app.getEntry("Ammount"))
                    app.stop()
                    confirmationMenu(acc)
                else:
                    app.startSubWindow("error")
                    app.errorBox("TransactionError" , "Not enough funds in savings account!")
                    app.destroyAllSubWindows()
            elif button == type + " checking to savings":
                if int(app.getEntry("Ammount")) < acc.getChecking():
                    acc.transfer(False , (app.getEntry("Ammount")))
                    app.stop()
                    confirmationMenu(acc)
                else:
                    app.startSubWindow("error")
                    app.errorBox("TransactionError" , "Not enough funds in checking account!")
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
    
    app.addLabel("savingsBal" , ("Savings Account Balance:" , acc.getSavings()))
    app.setLabelBg("savingsBal" , "white")
    app.addLabel("checkingBal" , ("Checking Account Balance:" , acc.getChecking()))
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
    counter = -1
    newFile = []
    for i in accountsFile:
        counter += 1
        newFile = newFile + [i]
        if i.split("\t")[0] == acc.getID():
            newFile[counter] = newLine
        else:
            newFile[counter] = i
    accountsFile.close()
    accountsFile = open("accounts.txt" , "w")
    for i in range(counter+1):
        accountsFile.write(newFile[i])
        if i == 0:
            accountsFile.write("\n")
    accountsFile.close()
    
def main():
    mainMenu()
    
if __name__ == '__main__':
    main()
