####################NATIONAL PARK ########################
class NationalPark:
    all = []
    ##############
    #initializer 
    ##############
    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)

    ##############
    # property name 
    @property #getter 
    def name(self):
        return self._name
    #setter 
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 3 <= len(name) and not hasattr(self, 'name'):
            self._name = name
        # else:
        #     raise Exception("- Names must be of type `str`/Names length must be greater or equal to 3 characters/Should **not be able** to change after the national_park is instantiated")


        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self ]
    
    def visitors(self):
        original_list = [ trip.visitor for trip in self.trips() ]
        unique_list = list(set(original_list))
        return unique_list
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        # create  a list of visitors 
        visitors = [ trip.visitor for trip in self.trips()]

        #set for the unique visitor
        set_of_visitors = set(visitors)

        max_visitor = max(set_of_visitors, key=visitors.count)

        return max_visitor
    
    @classmethod
    def most_visited(cls):
        # using the max function to find the park with the highest total visit 
        
        return max(cls.all, key=lambda park: park.total_visits()) 
    
        # lambda function take an argument 
        #and the value returned by this function will be used as the key for sorting or comparison

####################TRIP ########################
class Trip:
    all = []
    ##########
    #initializer 
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self) 

    ########## property start_date 
    #getter 
    @property
    def start_date(self):
        return self._start_date
    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7 and (start_date.endswith("st") or start_date.endswith("nd") or start_date.endswith("rd") or start_date.endswith("th")):
            self._start_date = start_date
        # else:
        #     raise Exception
            
    ########## property end_date 
    #getter 
    @property
    def end_date(self):
        return self._end_date
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7 and (end_date.endswith("st") or end_date.endswith("nd") or end_date.endswith("rd") or end_date.endswith("th")):
            self._end_date = end_date
        # else:
        #     raise Exception

    #property visitor
    #getter and setter 
    @property #getter 
    def visitor(self):
        return self._visitor
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor 
        else:
            raise Exception("Must be of type `Visitor`")
    
    #property national park
    #getter and setter 
    @property #getter 
    def national_park(self):
        return self._national_park
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park 
        else:
            raise Exception("Must be of type `national_park`")

        

####################VISITOR########################
class Visitor:

    ##########
    #initializer 
    def __init__(self, name):
        self.name = name

    ########## property name 
    #getter 
    @property
    def name(self):
        return self._name
    #setter 
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name #set the name 
        # else:
        #     raise Exception(" Names must be of type`str`Names must be between 1 and 15 characters, inclusive")

    def trips(self):
        return [ trip for trip in Trip.all if trip.visitor == self ] 
    
    def national_parks(self):
        original_list = [ trip.national_park for trip in self. trips()]
        unique_list = list(set(original_list))
        return unique_list

        #another option
        # return list({trip.national_park for tirp in self.trips()})
    
        # numbers = [ 1, 2, 1, 4, 2, 3, 2, 2, 2]

        # set comprehension to get unique number
        # unique_numbers_set = {num for num in numbers}

        #converting the set to a list
        # unique_numbers_list = list(unique_numbers_set)

        # unique_numbers_list
        # [1, 2, 3, 4]

    
    def total_visits_at_park(self, park):
        # if not isinstance(park, NationalPark):
        #     raise Exception
        if not park.visitors():
            return 0
        return len([ trip for trip in self.trips() if trip.national_park == park])
        
        