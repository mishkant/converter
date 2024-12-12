
def converter(ops, amount):

	if ops == "km":
		return amount * 1000

	elif ops == "m":
		return amount / 1000

	else:
		return "Error!"


ops = input("km or m? ")
amount = int(input(f"Amount of {ops}: "))

print(converter(ops, amount))