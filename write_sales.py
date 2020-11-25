days_string = input("For how many days do you have sales? ")
days_int = int(days_string)
counter = 1
sales_file = open("sales.txt", "a")

while days_int > 0:
        this_day = input("Enter the sales for day #" + str(counter) + ": ")
        counter = counter + 1
        days_int = days_int - 1
        sales_file.write(this_day + "\n")
sales_file.close()

print("Data written to sales.txt")
