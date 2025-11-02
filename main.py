# Positif, Negatif or Zero

num = int(input("Enter a random number?: "))

def check_of_number():
    if num > 0:
        return "Number is positif"
    elif num < 0:
        return "Number is negatif"
    else:
        return "Number is zero"
    
print(check_of_number())