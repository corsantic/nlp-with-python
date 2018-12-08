# -*- coding: utf-8 -*-


print("Hello World!")






result = 1+ 2 

result = 1+3 

print(result)



for i in range(2,20,5):
    print(i,end="-")
    
    
list1 = [1,2,3,4]


for item in list1:
    print(item)
    
tuple1 = (12,"String",13.6,"String2")
tuple2 = (30,50,9)

print(tuple1)
print(tuple1[0])

tuple3 = tuple2+tuple1

len(tuple3)




dict1={}


dict1["car"] = "Car is a mechanical wheeler"

print(dict1.get("car","not found"))



input1 = input("enter a something:")
some = input1;

print (some)


inp = input ("Enter something for the file write : ")

with open("text.txt","w") as f:
    f.write(inp)
    

inp = input ("Enter something for add to the file : ")

with open("text.txt","a") as f:
    f.write(inp)
    

with open("text.txt","r") as f:
    print(f.read())
    


def function(arg1,arg2):
    return (arg1+arg2)

print(function(1,3))


class Dog:
    def bark(self):
        print("Dog is barking")
    def bite(self):
        print("Dog is biting you")

dog = Dog()

dog.bark()


class Game:
    def __init__(self,name):
        self.name = name
    def start(self):
        print(self.name , " has been started")
    def stop(self):
        print(self.name, " has been stopped" )


game = Game("WoW")

print(game.name)

game.start()
game.stop()



str = ["string","str","str2"]

newStr= [string for string in str]


words = ["you","think","you","do","but","you","don't"]
sentence = "-".join(words);










