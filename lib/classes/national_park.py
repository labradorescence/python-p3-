class NationalPark:

    #################
    ##### Initializer 
    #################

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []

        self.visitors_count = {}
        


    #################
    ##### Property Name 
    #################
    #getter 
    @property
    def name(self):
        return self._name 

    #setter 
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, 'name'):
            self._name = name
        else:
            raise Exception
        

    ### Object Relationship Methods and Properties
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if new_trip and isinstance(new_trip, Trip):
            self._trips.append(new_trip)

        return self._trips
        pass
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        if isinstance(new_visitor, Visitor) and new_visitor not in self._visitors:
            self._visitors.append(new_visitor)
        return self._visitors
        pass
    
    def total_visits(self):
        return len(self._trips)
        pass
    
    # def best_visitor(self):
    #     for trip in self._trips:
    #         if trip.visitor in self.visitors_count:
    #             self.visitors_count[trip.visitor] += 1
    #         else:
    #             self.visitors_count[trip.visitor] = 1
    #     return max(self.visitors_count, key=self.visitors_count.get)
    #     pass

    def best_visitor(self):
        max_visitor = None
        max_visits = 0

        for single_visitor in self._visitors:
            print(self._trips)
            v_visits = len([one_trip for one_trip in self._trips if one_trip.visitor == single_visitor])

            print(v_visits)

            if v_visits > max_visits:
                max_visits = v_visits
                max_visitor = single_visitor

        return max_visitor