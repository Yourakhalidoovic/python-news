from tabulate import tabulate
data=[
 {"name":"ali","age":"30","wilya":"alger"},
 {"name":"souad","age":"34","wilya":"batna"}
 ]
print(tabulate(data,headers="keys",tablefmt="grid"))