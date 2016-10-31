class Car(object):
    """A class that instantiates various cars .If no arguement is given, 
    the following will be the default attributes."""
    def __init__(self,name='General',model='GM',car_type='saloon'):
        self.car_type =car_type
        self.name=name
        self.model = model
        self.speed=0
        if ( self.name == 'Porsche' or self.name == 'Koenigsegg'):
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4
        if (self.car_type == 'trailer'):
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4
    def is_saloon(self):
        if self.car_type == 'saloon':
            return True
        else:
            return False

    
    def drive(self, speed):
        if (self.car_type == 'trailer'):
            self.speed = speed * 11
            return self
        else:
            #if self.speed == 0:
             #   self.speed = 0
            #else:
                self.speed = 10 ** speed
                return self
one=Car('Porsche')
#one.drive(0)
#one.is_saloon()
