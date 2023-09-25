class Restaurant:
    RESTAURANTS = []

    def __init__(self, name):
        """
        Initialize a restaurant instance with a given name.

        Args:
            name (str): The name of the restaurant.
        """
        self.name = name
        self.reviews = []  # List to store reviews associated with this restaurant
        Restaurant.RESTAURANTS.append(self)  # Add the instance to the list of all restaurants

    def get_name(self):
        """
        Get the name of the restaurant.

        Returns:
            str: The name of the restaurant.
        """
        return self.name

    def get_reviews(self):
        """
        Get the reviews associated with this restaurant.

        Returns:
            list: A list of reviews associated with this restaurant.
        """
        return self.reviews

    @classmethod
    def all(cls):
        """
        Get all restaurant instances created.

        Returns:
            list: A list of all restaurant instances.
        """
        return cls.RESTAURANTS

    def customers(self):
        """
        Get customers who have reviewed this restaurant.

        Returns:
            list: A list of customers who have reviewed this restaurant.
        """
        return list({review.customer() for review in self.reviews})

    def average_star_rating(self):
        """
        Calculate and return the average star rating of the restaurant.

        Returns:
            float: The average star rating of the restaurant, or 0 if no reviews exist.
        """
        if not self.reviews:
            return 0
        total_rating = sum(review.get_rating() for review in self.reviews)
        return total_rating / len(self.reviews)
