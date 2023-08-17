import functions
print("my python calculator")
choice = int(input('''
choose one of the following choices
[1] addition
[2] subtraction
[3] multiplication
[4] division
[5] exponential 
[6] square root
[7] tangent(trigonometry)
[8] sin (trigonometry)
[9] cosine (trigonometry)
'''))

if choice == 1:
    functions.addition()

