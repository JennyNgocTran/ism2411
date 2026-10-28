# Self-Assessment Questions
# 1. The order total passes through the first if statement,
# which returns as False. So then, it passes through the elif
# statement total >= 200, which comes out as True, resulting
# in a 10% discount on the final price.
# 2. The result would not be the same because the and statement
# would result in one boolean value while two separate if 
# statements would result in two separate boolean values.
# 3. I often encounter tiered conditional logic in my classes'
# grading systems (A+, A, B+, etc.). Knowing Python conditionals
# helps me understand that sorting grade percentages into their
# categories is often rigid.

# Exercise 1

total = float(input("Enter cart total: $"))

if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.1
elif total >= 100:
    discount = 0.05
else:
    discount = 0

final = total * (1 - discount)

# Exercise 3

region = "South"
extra_discount = 0
if region == "South" and total >= 100:
    extra_discount = 0.02
    print("Region bonus applied: additional 2% off")

final_discount = discount + extra_discount
final = total * (1 - final_discount)

print(f"Final discount: {final_discount:.1%}") # Gives whole percentage not the rate
print(f"Final price: ${final:,.2f}") # Gives final at 2 decimals with commas

# Exercise 2

if final > 1000:
    status = "manager_approval_required"
else:
    status = "auto_approved"

print(f"Status: {status}")

# Exercise 4

# The flat version is easier to read because it is more similar to conventional English.
customer_type = "wholesale"
# if region == "South":
#     if total > 100:
#         if customer_type == "wholesale":
#             extra_discount = 0.03

if region == "South" and total > 100 and customer_type == "wholesale":
    extra_discount = 0.03

# Exercise 5

amount = -50

if amount <= 0:
    print("SUSPICIOUS")
elif amount < 10000:
    print("NORMAL")
else:
    print("LARGE - REVIEW REQUIRED")

# Exercise 6 

total_spent_this_year = 2500
orders_this_year = 6
has_outstanding_balance = False

qualifies_by_spending = total_spent_this_year > 2000
qualifies_by_order = orders_this_year > 10

vip_upgrade = (qualifies_by_spending or qualifies_by_order) and not has_outstanding_balance

print(f"VIP upgrade: {vip_upgrade}")