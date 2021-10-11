class Person:
    def __init__(self,initialAge):
        self.initialAge = initialAge
        if self.initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.initialAge = 0
    def amIOld(self):
        if self.initialAge < 13 :
            print("You are young.")
        elif self.initialAge > 12 and self.initialAge < 18:
            print("You are a teenager.")
        elif self.initialAge > 17 :
            print("You are old.")
    def yearPasses(self):
        temp = self.initialAge 
        self.initialAge += 1
        if self.initialAge == temp+3:
            if self.initialAge < 13 :
                print("You are young.")
            elif self.initialAge > 12 and self.initialAge < 18:
                print("You are a teenager.")
            elif self.initialAge > 17 :
                print("You are old.")
