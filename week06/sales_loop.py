# Self-Assessment Questions
# 1. The accumulator pattern has 3 steps: initialize, loop, and update. Initializing allows the accumulator to exist before 
# the first iteration begins, usually by setting a starting value for a variable. Looping iterates over every item in a sequence 
# one at a time. Updating inside the loop refers to updating the variable each iteration.
# 2. The code length of the for loop is shorter than the while loop. for loop is good for predictable data but not for unpredictable.
# while loop is good for unpredictable datasets, but could create an infinite loop if the condition never becomes False.
# 3. Creating a balance sheet given assets, liabilities, and stockholders' equity. The list would contain the values of items under 
# each category; accumulate the sum of each category/subcategory separately; print the subtotals of current assets/liabilities and 
# totals of assets, liabilities, and stockholders' equity.

# Exercise 1

sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0 # initialize
count = 0
current_max = 0
count_over_100 = 0
total_over_100 = 0

for sale in sales:
    total += sale # update
# Exercise 2
    count += 1 
# Exercise 3
    if sale > current_max:
        current_max = sale
# Exercise 4
    if sale > 100:
        count_over_100 += 1
        total_over_100 += sale

average = total / count

print(f"Total: ${total}")
print(f"Count: {count}")
print(f"Average: ${average:.2f}")
print(f"Largest sale: ${current_max}")
print(f"Sales over $100: {count_over_100}")
print(f"Total of those sales: ${total_over_100}")

# Exercise 5
for sale in sales:
    if sale > 400:
        print(f"Alert: outlier found - ${sale}. Stopping.")
        break
    if sale <= 100:
        continue
    print(f"${sale}")

# Exercise 6
total = 0
i = 0 # index
while i < len(sales):
    total += sales[i]
    i += 1

print(f"Total (while loop): ${total}")

# I would use the for loop over while loop since the for loop is shorter and there is a greater chance of accidentally creating an 
# infinite loop using a while loop. And in accounting, datasets already have a known quantity of items.

# Exercise 7

for sale in sales:
    if sale >= 200:
        discount = 0.10
    elif sale >= 100:
        discount = 0.05
    else:
        discount = 0
    discounted_price = sale * (1 - discount)
    print(f"${sale} -> {discount*100:.0f}% discount -> " f"${discounted_price:.2f}")