s = "younes is a good boy"

print(len(s))
print(len('\n'))
with open('budgetTracker', 'w') as f:
    
    for i in range(10):
        f.write(s+"\n")
    



with open('budgetTracker', 'r') as f:
    lines = f.readlines() # read all lines at once
    line = f.readline() # read one line at a time
    print(line)