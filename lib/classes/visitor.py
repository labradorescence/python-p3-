class Visitor:

    #################
    #### Initializer
    #################

    def __init__(self, name):
        self.name = name

        ### Object Relationship Methods and Properties
        self._trips = []
        self._national_parks = []

    #################
    ####property name
    #################

    #getter
    @property #getter
    def name(self):
        return self._name #return name
    
    #setter 
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15 and not hasattr(self, 'name'):
            #- Names must be of type `str`
            # - Names must be between 1 and 15 characters, inclusive
            self._name = name
        else:
            raise Exception
    
    ### Object Relationship Methods and Properties        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if new_trip and isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips

    ### Object Relationship Methods and Properties    
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        if new_national_park and isinstance(new_national_park, NationalPark) and new_national_park not in self._national_parks:
            self._national_parks.append(new_national_park)
        return self._national_parks