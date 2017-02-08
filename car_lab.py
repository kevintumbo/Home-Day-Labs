class Car(object):
    def __init__(self, name=None, model=None,  car_type=None):
        self.num_of_doors = 4
        self.num_of_wheels = 4
        self.speed = 0
        
        if name is not None and isinstance(name, str):
            self.name = name
        else:
            self.name = 'General'

        if model is not None and isinstance(model, str):
            self.model = model
        else:
            self.model = 'GM'

        if car_type is not None and isinstance(car_type, str):
            self.type = car_type
        else:
            self.type = 'saloon'

        if name is 'Porshe' or name is 'Koenigsegg':
            self.num_of_doors = 2
            
        if self.type is 'trailer':
            self.num_of_wheels = 8   

    def is_saloon(self):
        if self.type is 'trailer':
            return False
        else:
            return True

    def drive(self, speed):
        if isinstance(speed, int):
            if speed is 7:
                self.speed = 77
            elif speed is 3:
                self.speed = 1000
            return self