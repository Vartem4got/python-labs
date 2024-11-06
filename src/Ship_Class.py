class Ship:

    def __init__(self, name="Unknown", mass=0, pasngrs=0):

        self.__name = name             
        self.__mass = mass       
        self.__pasngrs = pasngrs
        self.public_int = 0            
        self.public_str = "Public"     

    # Def get ->
    def get_name(self):
        return self.__name

    def get_mass(self):
        return self.__mass

    def get_pasngrs(self):
        return self.__pasngrs

    # Def set ->
    def set_name(self, name):
        self.__name = name

    def set_mass(self, mass):
        self.__mass = mass

    def set_pasngrs(self, pasngrs):
        self.__pasngrs = pasngrs

    # str repl del ->
    def __str__(self):
        return f"Ship(Name: {self.__name}, Mass: {self.__mass}, Pasngrs: {self.__pasngrs})"


    def __repr__(self):
        return f"Ship('{self.__name}', {self.__mass}, {self.__pasngrs})"


    def __del__(self):
        print(f"Ship {self.__name} is being destroyed.")

# def main - >
def main():

    ship1 = Ship("Titanic", 46000, 2400)
    ship2 = Ship("Queen Mary", 76000, 2700)
    ship3 = Ship()


    print(ship1)
    print(ship2)
    print(ship3)

    
        # i hate debug, if it goes wrong agan i dknow what to do
    

    print(ship3)
    
    
    

if __name__ == "__main__":
    main()

