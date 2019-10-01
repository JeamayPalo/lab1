#Lab 2 of Python Class but it's the first real lab

#Problem 1: Ingredient Adjuster

num_of_cookies = float(input("How many cookies do you want to make?" ))
adjusted_quantity = num_of_cookies / 48
cups_of_sugar = 1.5 * adjusted_quantity
cups_of_butter = 1 * adjusted_quantity
cups_of_flour = 2.75 * adjusted_quantity

print ("You need " + str(cups_of_sugar) + " cups of sugar," + str(cups_of_butter) + " cups of butter, and " + str(cups_of_flour) + " cups of flour.")

#Problem 2: Male/Female Percent

num_of_males = int(input("Enter the number of males:"))
num_of_females = int(input("Enter the number of females:"))
total = num_of_males + num_of_females 
percent_males = num_of_males / total
percent_females = num_of_females / total

print ("Percent males: " + str(int(percent_males * 100)) + "%")
print ("Percent females: " + str(int(percent_females * 100)) + "%")

#Problem 3: Stock Transaction

num_of_shares = int(input("Enter the number of shares:"))
purchase_price = float(input("Enter the purchase price:"))
sale_price = float(input("Enter the sale price: "))
profit_or_loss = (sale_price * num_of_shares) - (purchase_price * num_of_shares)

print ("Shares: " + str(num_of_shares))
print ("Purchase price: $" + str(purchase_price * num_of_shares))
print ("Sale price: $" + str(sale_price * num_of_shares))
print ("Profit/Loss: $" + str(profit_or_loss))

