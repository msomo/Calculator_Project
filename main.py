import Functions
print("my python calculator")

print('''
choose one of the following operations
[1] addition
[2] subtraction
[3] multiplication
[4] division
[5] exponential 
[6] square root
[7] tangent(trigonometry)
[8] sin (trigonometry)
[9] cosine (trigonometry)
''')
choice = int(input("Enter a choice from 1-9: "))


if choice == 1:
    Functions.addition()
elif choice == 2:
    Functions.substraction()
elif choice == 3:
    Functions.multiplication()
elif choice == 4:
    Functions.division()
elif choice == 5:
    Functions.exponential()
elif choice == 6:
    Functions.sqrt()
elif choice == 7:
    Functions.tangent()
elif choice == 8:
    Functions.sin()
    
else:
    print("Invalid choice/entry")

