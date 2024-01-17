#######################################################################################################################
class NationalPark:
    all = []
    def __init__(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise Exception("name should be initialized as a string")
       # NationalPark.all.append(self)
        type(self).all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 3<= len(name) and not hasattr(self, 'name'):
            self._name = name
        # else:
        #     raise Exception("Names must be of type `str`/length must be greater or equal to 3 characters/Should **not be able** to change after the national_park is instantiated")

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self]
    
    def visitors(self):
        #option1
        original_list = [trip.visitor for trip in self.trips()]
        unique_list = list(set(original_list))
        return unique_list
    
        #option2
        # return list({trip.visitor for trip in self.trips()})
    
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        # visitors = [trip.visitor for trip in self.trips()]        
        # return max(set(visitors), key=visitors.count)
        
        # Create a list of visitors associated with each trip
        visitors = [trip.visitor for trip in self.trips()]

        # Create a set to get unique visitors (remove duplicates)
        set_of_visitors = set(visitors)

        # Find the visitor with the maximum count in the original list
        # The key parameter uses the count of occurrences in the original list
        max_visitor = max(set_of_visitors, key=visitors.count)

        # Return the Visitor instance that has visited the park the most
        # If the park has no visitors, return None
        return max_visitor

    @classmethod
    def most_visited(cls):
        # Use the max function to find the park with the highest total visits
        # The key parameter specifies a lambda function that extracts the total 
        #visits for each park
        return max(cls.all, key=lambda park: park.total_visits())

#######################################################################################################################
class Trip:
    all = []
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)


    @property
    def start_date(self):
        return self._start_date
    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7 and (start_date.endswith("st") or start_date.endswith("nd") or start_date.endswith("rd") or start_date.endswith("th")) :
            self._start_date = start_date
        # else:
        #     raise Exception
        
    @property
    def end_date(self):
        return self._end_date
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and 7 <= len(end_date) and (end_date.endswith("st") or end_date.endswith("nd") or end_date.endswith("rd") or end_date.endswith("th")) :
            self._end_date = end_date
        # else:
        #     raise Exception

#getter
    @property
    def visitor(self):
        return self._visitor
    
    #setter
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor): 
            self._visitor = visitor
        else:
            raise Exception("Must be of type `Visitor`")
        
#getter
    @property
    def national_park(self):
        return self._national_park
    
    #setter
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise Exception("Must be of type `NationalPark`")


#######################################################################################################################
class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        # else:
        #     raise Exception ("Names must be of type `str` Names must be between 1 and 15 characters, inclusive")
        

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        # return list({trip.national_park for trip in self.trips()})
    
        original_list = [trip.national_park for trip in self.trips()]
        unique_list = list(set(original_list))
        return unique_list


    def total_visits_at_park(self, park):
    # if not isinstance(park, NationalPark):
    #     raise Exception
        if not park.visitors():
            return 0
        return len([trip for trip in self.trips() if trip.national_park == park])