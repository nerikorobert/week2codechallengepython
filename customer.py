from review import Review

class Customer:
    CUSTOMERS = [] # list of all customers

    def __init__(self,given_name,family_name):
        self._given_name = given_name
        self._family_name = family_name
        self.reviews = [] # List to store reviews associated with this customer
        Customer.CUSTOMERS.append(self) # Add the instance to the list of all customers

    @property
    def given_name(self):
        return self._given_name #Return given name of customer
        
    
    def family_name(self):
        return self._family_name #Return family name of customer
        
    @property
    def full_name(self):
        return f"{self._given_name} {self._family_name}" #Return full name of customer
        
    @classmethod
    def all(cls):
        return cls.CUSTOMERS #returns a list of all customer instances
        
    def add_review(self, review):
        self.reviews.append(review) # Add the review to this customer's list of reviews
        
    def num_review(self):
        return len(self.reviews) # Number of reviews by this customer
        
    @classmethod
    def find_by_name(cls,name):
        for customer in cls.CUSTOMERS:
            if customer.full_name == name:
                return customer # Find and return a customer instance by full name
            return None # Return None if customer not found

    @classmethod
    def find_all_by_given_name(cls,name):
        return [customer for customer in cls.CUSTOMERS if customer._given_name == name]
        #Finds and returns all customers instances with a specific given name