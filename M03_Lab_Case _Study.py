#Vehical Class
class Vehicle:
    def __init__(self, type):
        self.type = type

#Vehicle subclass
class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type) 
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

#Allow the user to input data for the vehicle.
type = input("Enter the type of vehicle: ")
year = input("Enter the year of the vehicle: ")
make = input("Enter the manufacturer of the vehicle: ")
model = input("Enter the model of the vehicle: ")
doors = input("Enter the number of doors the vehicle has (2 or 4): ")
roof = input("Enter if the vehicle has a solid roof or a sun roof: ")
Auto = Automobile (type, year, make, model, doors, roof)

#Print output of the data
print("\nVehicle Type: "+Auto.type)
print("\nVehicle Year: "+Auto.year)
print("\nVehicle Make: "+Auto.make)
print("\nVehicle Model: "+Auto.model)
print("\nNumber of doors: "+Auto.doors)
print("\nType of roof: "+Auto.roof)