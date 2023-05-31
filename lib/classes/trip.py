class Trip:
    #################
    #### Initializer
    #################
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        ### Object Relationship Methods and Properties    
        visitor.trips(self)
        visitor.national_parks(national_park)

        national_park.trips(self)
        national_park.visitors(visitor)


    #################
    ####property visitor
    #################

    #getter
    @property
    def visitor(self):
        return self._visitor
    
    #setter
    @visitor.setter
    def visitor(self, visitor):
        from classes.visitor import Visitor
        if isinstance(visitor, Visitor): 
            self._visitor = visitor
        else:
            raise Exception("Must be of type `Visitor`")
        


    #################
    ####property national park
    #################

    #getter
    @property
    def national_park(self):
        return self._national_park
    
    #setter
    @national_park.setter
    def national_park(self, national_park):
        from classes.national_park import NationalPark
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise Exception("Must be of type `NationalPark`")


