# Import necessary classes from respective modules
from customer import Customer  # Imports Customer class from customer.py module
from restaurant import Restaurant  # Imports Restaurant class from restaurant.py module
from review import Review  # Imports Review class from review.py module

# SAMPLE DATA
# Create Customer and Restaurant instances
customer1 = Customer("Robert", "Rinnah")
customer2 = Customer("Neriko", "Clara")
restaurant1 = Restaurant("Supu Zone")
restaurant2 = Restaurant("Mutura Zone")

# REVIEWS SAMPLE DATA
# Creating Review instances
review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant1, 14)
review3 = Review(customer1, restaurant2, 8)
review4 = Review(customer2, restaurant2, 7)

# Print all customers
print("All Customers:")
for customer in Customer.all():
    print(customer.full_name)

# Print all restaurants
print("\nAll Restaurants:")
for restaurant in Restaurant.all():
    print(restaurant.name)

# Print average star rating for each restaurant
print("\nAverage Star Ratings:")
for restaurant in Restaurant.all():
    avg_rating = restaurant.average_star_rating()
    print(f"{restaurant.name}: {avg_rating}")

# Find customers by given name
print("\nCustomers with given name 'Neriko':")
given_name = "Neriko"
matching_customers = Customer.find_all_by_given_name(given_name)
for customer in matching_customers:
    print(customer.full_name)

# Print the number of Reviews for Each customer
print("\nNumber of Reviews for Each customer:")
for customer in Customer.all():
    num_review = customer.num_review()
    print(f"{customer.full_name}'s Reviews: {num_review}")

# Print the list of reviews for each customer
print("\nList of Reviews for Each Customer:")
for customer in Customer.all():
    print(f"{customer.full_name}'s Reviews:")
    for review in customer.reviews:
        print(f"  - Restaurant: {review.restaurant().name}")
        print(f"    Rating: {review.get_rating()}")
