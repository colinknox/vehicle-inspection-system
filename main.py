class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def safety_check(self):
        raise NotImplementedError("Each vehicle type must implement its own safety check")
    
    def get_info(self):
        return f"{self.make} {self.model}"
    
class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
    
    def safety_check(self):
        return "Car safety check: Brakes, lights, and seatbelts OK"   
    


nissan_fairlady = Vehicle("Nissan", "Fairlady")
car = Car("Ford", "Mustang")

# print(f"""
# Make = {car.make}
# Model = {car.model}
# Get info = {car.get_info()}
# """)

print(f"""
Make = {car.make}
Model = {car.model}
Safety check = {car.safety_check()}
Get info = {car.get_info()}
""")

