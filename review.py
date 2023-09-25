from review import Review

class Customer:
    CUSTOMERS = []  # A list to store all customer instances

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self.reviews = []  # List to store reviews associated with this customer
        Customer.CUSTOMERS.append(self)  # Add the instance to the list of all customers

    @property
    def given_name(self):
        """Return the given name of the customer."""
        return self._given_name

    def family_name(self):
        """Return the family name of the customer."""
        return self._family_name

    @property
    def full_name(self):
        """Return the full name of the customer."""
        return f"{self._given_name} {self._family_name}"

    @classmethod
    def all(cls):
        """Return a list of all customer instances."""
        return cls.CUSTOMERS

    def add_review(self, review):
        """Add a review to this customer's list of reviews."""
        self.reviews.append(review)

    def num_review(self):
        """Return the number of reviews by this customer."""
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, name):
        """
        Find and return a customer instance by full name.

        Args:
            name (str): The full name to search for.

        Returns:
            Customer or None: The found customer instance or None if not found.
        """
        for customer in cls.CUSTOMERS:
            if customer.full_name == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        """
        Find and return all customer instances with a specific given name.

        Args:
            name (str): The given name to search for.

        Returns:
            list: A list of customer instances with the given name.
        """
        return [customer for customer in cls.CUSTOMERS if customer._given_name == name]
