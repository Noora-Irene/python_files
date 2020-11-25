
sales_file = open("sales.txt", "r")
line = sales_file.readline()

while line != '':
    line = sales_file.readline()
    print(line)

sales_file.close()
