class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelY = vehicle(150, 500)
print(f"The max speed of modelY = {modelY.max_speed}")
print(f"The mileage of modelY = {modelY.mileage}")