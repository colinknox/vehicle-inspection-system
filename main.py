class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def safety_check(self):
        raise NotImplementedError("Each vehicle type must implement its own safety check")
    
    def get_info(self):
        return f"{self.make} {self.model}"
    


nissan_fairlady = Vehicle("Nissan", "Fairlady")

print(f"DEBUG: Make = {nissan_fairlady.make}, Model = {nissan_fairlady.model}")
print(f"DEBUG: Safety check = {nissan_fairlady.safety_check()}")
print(f"DEBUG: Get info = {nissan_fairlady.get_info()}")