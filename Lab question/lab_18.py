# 1. You have a list of user data with their names and email addresses. Create a
# dictionary that maps each domain (from the email address) to a list of users with
# emails from that domain.

users=[
   {'name': 'Alice', 'email': 'alice@gmail.com'},
    {'name': 'Bob', 'email': 'bob@yahoo.com'},
    {'name': 'Charlie', 'email': 'charlie@gmail.com'},
    {'name': 'David', 'email': 'david@outlook.com'},
    {'name': 'Eve', 'email': 'eve@yahoo.com'},
    {'name': 'Frank', 'email': 'frank@gmail.com'}
]

domain_user={}
for user in users:
   name=user['name']
   email=user['email']

   domain = email.split('@')[1]

   if domain not in domain_user:
      domain_user[domain]=[]
   domain_user[domain].append(name)

#  ------- OR ------------

domain_user = {
    domain: [user['name'] for user in users if user['email'].split('@')[1] == domain]
    for domain in {user['email'].split('@')[1] for user in users}
}

# for domain, names in domain_user.items():
#     print(domain, names)



# 2. You have a list of customer reviews for different products. Each review
# contains a product name and a rating. Your task is to create a dictionary that
# maps each product to its average rating.

reviews = [
    {'product': 'Laptop', 'rating': 6},
    {'product': 'Phone', 'rating': 4},
    {'product': 'Laptop', 'rating': 9},
    {'product': 'Tablet', 'rating': 7},
    {'product': 'Phone', 'rating': 8},
    {'product': 'Laptop', 'rating': 7},
    {'product': 'Tablet', 'rating': 9}
]
# taking all unique products
products = {review['product'] for review in reviews}

# Create dictionary mapping product to its average rating using comprehension
average_ratings = {
    product: sum(review['rating'] for review in reviews if review['product'] == product) /
             sum(1 for review in reviews if review['product'] == product)
    for product in products
}

# Print the result
print(average_ratings)