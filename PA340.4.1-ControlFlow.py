# Problem 1
x = 7
# x = 15
if x < 10:
    print("Less than 10")    

# Problem 2    
x = 15
if x < 10:
    print("Less than 10")    
elif x > 10:
    print("Greater than 10")

# Problem 3
x = 15
if x < 10:
    print("Less than 10")    
elif 10 <= x > 20:
    print("Between 10 and 20")
else: 
    print("Greater than or equal to 20")

# Problem 4
x = 15
if 10 <= x >= 20:
    print("In range")
else:         
    print("Out of range")


# Problem 5
grade = int(input("Enter your grade: "))

if 90 <= grade <= 100:
    print("A")
elif 80 <= grade > 89:
    print("B")    
elif 70 <= grade < 79:
    print("C")
elif 60 <= grade < 69:
    print("D")        
elif  grade < 60:
    print("F")    
else:
    print("Score out of range!")    




