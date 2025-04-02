# 1. Custom String Class: Implement a CustomString class that overloads the + operator for concatenation and the * operator to repeat the string. Include a method to return the string in uppercase. 

class CustomString:
   def __init__(self, value):
      self.value = value

   def __add__(self, other):
      if isinstance(other, CustomString):
         return CustomString(self.value + other.value)
      return NotImplemented

   def __mul__(self, times):
      if isinstance(times, int) and times >= 0:
         return CustomString(self.value * times)
      return NotImplemented

   def to_upper(self):
      return self.value.upper()

   def __repr__(self):
      return f'CustomString("{self.value}")'

# Example usage:
if __name__ == "__main__":
   str1 = CustomString("Great")
   str2 = CustomString(" World")

   # Concatenation
   concatenated = str1 + str2
   print("Concatenated String:", concatenated)

   # Repeating the string
   repeated = str1 * 3
   print("Repeated String:", repeated)

   # Uppercase
   uppercase = str1.to_upper()
   print("Uppercase String:", uppercase)


# 2. Currency Conversion: Create a Currency class that represents a monetary amount in a specific currency. Overload the + operator to add amounts in the same currency, and implement a method to convert between different currencies.

class Currency:
    exchange_rates = {  
        ('USD', 'EUR'): 0.91,
        ('EUR', 'USD'): 1.10,
        ('USD', 'INR'): 83.00,
        ('INR', 'USD'): 0.012,
        ('EUR', 'INR'): 91.0,
        ('INR', 'EUR'): 0.011
    }

    def __init__(self, amount, currency):
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if not isinstance(other, Currency):
            return NotImplemented
        return Currency(self.amount + other.amount, self.currency)

    def convert_to(self, target_currency):
        if self.currency == target_currency:
            return Currency(self.amount, self.currency)

        key = (self.currency, target_currency)
        if key not in self.exchange_rates:
            raise ValueError(f"Exchange rate not available for {self.currency} to {target_currency}.")

        converted_amount = self.amount * self.exchange_rates[key]
        return Currency(converted_amount, target_currency)

    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"


usd = Currency(100, "USD")
eur = Currency(50, "EUR")

# Addition of same currency
usd2 = Currency(50, "USD")
total_usd = usd + usd2
print(total_usd)  

# Conversion
converted_to_eur = usd.convert_to("EUR")
print(converted_to_eur)  

converted_to_inr = usd.convert_to("INR")
print(converted_to_inr)  

