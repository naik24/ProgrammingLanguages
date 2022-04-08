class Bicycle:
    
    def time(self, speed): 
        distance = 100 # in kilometers
        print('Total Time Required: ', distance/speed)

Bicycle.calculate_time = classmethod(Bicycle.time)
Bicycle.calculate_time(50)
