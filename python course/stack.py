def first():
    print(second())
    return 'i am first and i finished'

def second():
    print(third())
    
    return 'i am the second , and i have finished'

def third():
    return 'i am the third , and i have finished'

print(first())
#abs() :kima moutlaka 
