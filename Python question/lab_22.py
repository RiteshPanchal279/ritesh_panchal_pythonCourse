class Product:
   total_products=0
   def __init__(self,name,price,stock):
      self.name = name  
      self.price = price  
      self.stock = stock  
      Product.total_products += 1

   def update_stock(self,quantity):
      self.stock+=quantity

   def display_info(self,user_type="manager"):
      if user_type=='manager':
         print(f"Product: {self.name}, Price: ${self.price:.2f}, Stock: {self.stock}")
      else:
         print(f"Product: {self.name}, Price: ${self.price:.2f}")

   @staticmethod
   def product_info():
      print("Products are items available for purchase.")
    
   @classmethod
   def get_total_products(cls):
      return cls.total_products
      


class Customer:
   customer_count=0
   def __init__(self,name,email):
      self.name=name
      self.email=email
      self.orderHistory=[]
      Customer.customer_count+=1

   def place_order(self,order):
      self.orderHistory.append(order)
      
   @staticmethod
   def customer_info():
      print( "Customers can place orders and purchase products.")
    
   @classmethod
   def get_customer_count(cls):
      return cls.customer_count


class Order:
   order_count=0
   def __init__(self,order_id,customer):
      self.orderId = order_id
      self.customer = customer
      self.products = {}
      Order.order_count+=1
      
   def add_product(self,product, quantity):
      if product.stock >= quantity:
         self.products[product]=self.products.get(product,0)+quantity
         product.update_stock(-quantity)
      else:
         print(f"Not enough stock for {product.name}")
      
   @staticmethod
   def order_info():
        print( "Orders contain products purchased by customers.")
    
   @classmethod
   def get_order_count(cls):
        return cls.order_count



product1 = Product("Laptop", 20000, 10)
product2 = Product("Mouse", 600, 50)


customer1 = Customer("Ritesh", "One@example.com")
customer2 = Customer("Mohit", "Two@example.com")
order1 = Order(101,customer1)
order2 = Order(102,customer2)

order1.add_product(product1, 2)
order1.add_product(product2, 5)

order2.add_product(product2, 5)

customer1.place_order(order1)
product1.display_info('manager')
product2.display_info('manager')
product2.display_info('user')

print(f"Total products: {Product.get_total_products()}")
print(f"Total customers: {Customer.get_customer_count()}")
print(f"Total orders: {Order.get_order_count()}")