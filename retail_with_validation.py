FACTOR = 2.5
answer = 'y'

while answer == "y":
  cost = float(input("Enter the item's wholesale cost: "))
  while cost <= 0:
    print("ERROR: the cost cannot be negative.")
    cost = float(input("Enter the correct wholesale cost: "))
  retail = cost * FACTOR
  print("Retail price: $" + format(retail, ".2f"))
  answer = input("Do you have another item? (Enter y for yes): ")