
class Driver():
    
    _all = []
    _count = 0
    
    def __init__(self, name, car_make, car_model):
        self.name = name
        self.car_make = car_make
        self.car_model = car_model
        
        self._all.append(self)
        Driver._count += 1
        
    @classmethod
    def fleet_size(cls):
        return cls._count
    
    @classmethod
    def driver_names(cls):
        return [ele.name for ele in Driver._all]

    @classmethod
    def fleet_makes(cls):
        return [ele.car_make for ele in Driver._all]
    
    @classmethod
    def fleet_models(cls):
        return [ele.car_model for ele in Driver._all]

    @classmethod
    def fleet_makes_count(cls):
        all_makes = cls.fleet_makes()
        #turn list to counter dict
        make_count = {}
        for make in all_makes:
            make_count[make] = make_count.get(make, 0) + 1
        return make_count
    
    @classmethod
    def fleet_models_count(cls):
        all_models = cls.fleet_models()
        models_count = {}
        for model in all_models:
            models_count[model] = models_count.get(model, 0) + 1
        return models_count
    
    @classmethod
    def percent_of_fleet(cls, car_make):
        total_cars = len(cls.fleet_makes())
        makes = cls.fleet_makes_count()
        car_make_count = makes[car_make]
        
        percentage = round(car_make_count / float(total_cars) * 100, 2)
        return "{}%".format(percentage)
    

#Driver("Helga Pataki", "Toyota", "Camry")
#Driver("Arnold Shortman", "Toyota", "Highlander")
#Driver("Gerald Johanssen", "Toyota", "Camry")
#Driver("Robert 'Big Bob' Pataki", "Honda", "Pilot")
#Driver("Grandpa Phil", "Jeep", "Grand Cherokee")
#Driver("Rhonda Wellington Lloyd", "Kia", "Sonata")
#Driver("Phoebe Heyerdahl", "Honda", "Civic")

#print(Driver.fleet_size())
#print(Driver.driver_names())
#print(Driver.fleet_makes())
#print(Driver.fleet_models())
#print(Driver.fleet_makes_count())
#print(Driver.fleet_models_count())
#print(Driver.percent_of_fleet("Toyota"))
  
    