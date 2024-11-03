#Addison Puffelis, 11/3/2024, Comments will describe what each line of code is doing. The code itself is creating a class and objects that call upon it.
#Creates a class named 'Flower'
class Flower:
    #creates a function that initializes the class
    def __init__(self, name):
        #Uses dot notation to pass the inheritable attribut, in this case its the name.
        self.name = name
    #creates a function for the flower to grow
    def grow(self):
        #displays text that tells you the the flower is growing, using the object name.
        print("The " +self.name + " is growing.")
    #a funtion for the flower to bloom
    def bloom(self):
        #same as before, but now it's telling you the flower is blooming, using the object name.
        print("The " + self.name + " is blooming.")
#main function loop
def main():
    #creates an object named 'Rose', calling on the class.
    flower1 = Flower("Rose")
    #Calls the flower grow function in the flower class, uses the name specified above.
    flower1.grow()
    #same as above, but calls the bloom funtion, using the specified flower name above.
    flower1.bloom()
    #creates a second object using the name 'Daisy' that calls upon the the flower class.
    flower2 = Flower("Daisy")
    #calls the flower class grow function, using the name above.
    flower2.grow()
    #same as above but calls the bloom funtion of the flower class, using the name above.
    flower2.bloom()
## HERE IS THE ADDITIONAL FLOWER OBJECT
    #creates a third object that calls the flower class, named 'Lavender'.
    flower3 = Flower("Lavender")
    #calls the flower class grow function, using the name above.
    flower3.grow()
    #Same as above but calls the bloom function from the flower class.
    flower3.bloom()
    
#this is used if the code is run directly, uses the file nameof the code.Checks if the code is running directly.
if __name__ == "__main__":
    #Runs the code
  main()
