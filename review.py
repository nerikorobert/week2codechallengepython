class Review:
    REVIEWS = [] # list of reviews

    def __init__(self,customer,restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review.REVIEWS.append(self) # Add the review instance to the list of all reviews
        restaurant.reviews.append(self)  # Add the review to the restaurant's list of reviews
        customer.add_review(self)  # Automatically associate the review with the customer

    def get_rating(self):
        return self._rating  # Return the rating of the review
    
    @classmethod
    def all(cls):
        return cls.REVIEWS  # Return all review instances created
    
    def customer(self):
        return self._customer  # Return the associated customer instance
    
    def restaurant(self):
        return self._restaurant  # Return the associated restaurant instance