import time

class MicrowaveOven:
    def __init__(self,get_foodId):
        self.__get_foodId = get_foodId
        self.time = 0
        self.foodname = " "
        self.pounds = 0
    
    program_list = {1: "popcorn", 2: "pizza slice", 3: "baked potato", 4: "veggie snack",5: "defrost", 6: "custom time", 7: "turn off"}
    
    def default_heat_programs(self):
        print("**Microwave Menu**")
        for i in self.program_list:
            print(" " + str(i) + "-" + self.program_list[i])
        return  input("Choose option number: ")      

    def get_foodId(self):
        return self.__get_foodId
    
    def get_cooking_time(self):
        if self.__get_foodId == "1" :
            self.time = 3
            self.pounds = 0
            self.foodname = self.program_list.get(int(self.__get_foodId))

        if self.__get_foodId == "2" :
            self.time = 1.5
            self.pounds = 0 
            self.foodname = self.program_list.get(int(self.__get_foodId))

        if self.__get_foodId == "3" :
            self.time = 5
            self.pounds = 0
            self.foodname = self.program_list.get(int(self.__get_foodId))

        if self.__get_foodId == "4" :
            self.time = 2
            self.pounds = 0
            self.foodname = self.program_list.get(int(self.__get_foodId))

        if self.__get_foodId == "5" :
            print("**defrost program: 5 minutes for every 1 Lb**")
            self.pounds = int(input("approximate pounds to defrost: "))  
            self.time = self.pounds * 5 
            self.foodname = self.program_list.get(int(self.__get_foodId))

        if self.__get_foodId == "6" :
            self.time = int(input("input cooking time in minutes: ")) 
            self.pounds = 0 
            self.foodname = self.program_list.get(int(self.__get_foodId))

        if self.__get_foodId == "7" :
            self.time = 0
            self.pounds = 0
            self.foodname = self.program_list.get(int(self.__get_foodId))
       
        return self
    
class cooking_food(MicrowaveOven):
    def __init__(self,get_foodId, get_time):
        super().__init__(get_foodId)
        self.__get_time = get_time

    def start(self)  :
        i=0
        sec = int(self.__get_time) * 60
        while i <= int(self.__get_time) * 60 :
            print (str(int((i * 100)/sec)) + "%...", end = "") 
            time.sleep(1)
            i = i + 30
        print(" done!")
        time.sleep(2)    

def main():
    y = 1
    while y != "7" : 
        selectionId = MicrowaveOven(0).default_heat_programs()
        y = MicrowaveOven(selectionId).get_foodId()
        x = MicrowaveOven(y).get_cooking_time()
        if y!="7"  and  int(y) >= 1 and int(y) <= 6 : 
          print("The program for: " +  x.program_list.get(int(y))  + " will be running for " + str(x.time) + " minutes" ) 
          z = cooking_food(y,x.time).start()
        else :
          if y == "7":
            print("The microwave will be turned off" )

          
   

  
   
if __name__ == "__main__":
    main() 





        



