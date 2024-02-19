class console:
    def getString(self):
        return input()
    def printString(self, a):
        print(a.upper())

b = console()

userInput = b.getString()
b.printString(userInput)    

