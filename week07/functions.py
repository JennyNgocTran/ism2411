# Self-Assessment Questions
# 1. The first bug I found was a missing colon on line 10 from using the traceback. My current debugging instincts are still weak but further practice and experience
# will help enhance them.
# 2. apply_discount(price, tier) applies a discount to a customer's price based on their tier. The inputs are price (before discount) and the customer's tier. It will
# return the final price (after the discount is applied). A colleague could probably use the function if they understand what the inputs are and what data type they should be.
# 3. AI use: asked ChatGPT what SyntaxError meant on line 81; fixed the error myself

# Exercise 1

# Define calculate tax function

def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}") # $7.00
print(f"Tax on $250 at 8%: ${tax2:.2f}") # $8.00

# Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# Exercise 3

# Write it out manually first, then refactor into a function

discounted = apply_discount(200, "gold") # used below
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${after_tax:.2f}")

# Refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, "gold", 0.07):.2f}")

# Exercise 4

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")

# Exercise 5 (fixed version of broken_sales.py)

sales = [120, 80, 250, 175, 90]

# Added a plus sign before the equal sign on line 76
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

# Added a colon on line 81
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

# Removed the equal sign on line 87
i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# Exercise 6

x = 100 # apple # Global

def double_it():
    x = 999 # another apple (not the same apple as above) # Local
    return x * 2

print(x) # x = 100
print(double_it()) # x = 1998 
print(x) # x = 100