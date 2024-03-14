from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Name", "Age", "City"]

# Adding different rows
table.add_row(["Alice", 30, "London"])
table.add_row(["Bob", 25, "New York"])
table.add_row(["Charlie", 35, "Paris"])
table.add_row(["David", 28, "Tokyo"])
table.add_row(["Eve", 40, "Berlin"])

print(table)
