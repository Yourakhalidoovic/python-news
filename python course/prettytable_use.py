from prettytable import PrettyTable

# Create a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Create a PrettyTable instance
table = PrettyTable()

# Add columns
table.field_names = ["A", "B", "C"]
for row in matrix:
    table.add_row(row)

# Print the table
print(table)