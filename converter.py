
def converter(ops, amount):

	if ops == "km":
		return amount * 1000

	elif ops == "m":
		return amount / 1000

	elif ops == "mile":
		return amount * 1.62137

	elif ops == "kmm":
		return amount / 0.62137


	else:
		return "Error!"

print("Hello!")
ops = input("km or m? ")
amount = int(input(f"Amount of {ops}: "))

print(converter(ops, amount))
print("Bye!")
