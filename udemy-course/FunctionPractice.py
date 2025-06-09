import random as r
# 1. Function Alpha
# Create a function called Alpha that takes in a number and uses a 
# while loop to count from 1 to that number, inclusive. 
# The function should output each number to the console.

def alpha(num):
    x = 1
    while x <= num:
        print(x, end = " ")
        x+=1
    print()

# 2. Function Bravo
# Create a function called Bravo that uses a 
# for loop to return the total of the numbers 1 through 10.

def bravo():
    print(*range(1,11))

# 3. Function Charlie
# Create a function called Charlie that accepts a list x 
# and outputs the cube root of each number in the list.
def charlie(x):
    return [round(n**(1/3), 2) for n in x]

# 4. Function Delta
# Create a function called Delta that uses a while loop to ask the user for their age until they give an age between 0 and 100, inclusive.
# The function should return the variable age to main.
# Show how this function is called in main.
def delta():
    age = int(input("What is your age?\n"))
    while age <=0 or age>=100:
        age = int(input("Age must be between 0 and 100 inclusive. Put your age "))
    return age

# 5. Function Echo
# Create a function called Echo that outputs 
# 20 random numbers to a file called theFile.txt.
def echo():
    with open('theFile.txt', 'w') as f:
        for n in range(20):
            f.write(str(r.randint(1,20)) +" ")

# 6. Function Foxtrot
# Create a function called Foxtrot that takes in a float number and returns number * 2.
# Use this function in main to output the powers of 2 from 2⁰ through 2¹⁰.
def foxtrot(num: float) -> float:
    return num*2

# 7. Favorite Color (if/else)
# Ask the user for their favorite color.
# Store it in a variable named color.

# If they choose "blue" → output "Great choice."

# If "red" → output "Poor choice."

# If "green" → output "Not a bad choice."

# Otherwise → output "Sorry, that's not a primary color."

# Use an if / else-if / else statement.
def getColor(color:str) -> None:
    low = color.lower()
    if(low=='blue'):
        print("Great choice!")
    elif(low=='green'):
        print("Not a bad choice.")
    elif low=='red':
        print("Poor choice.")
    else:
        print('Sorry, that\'s not a primary color.')

# 8. Favorite Color (switch statement)
# Do the same as above, but use a switch statement.
# Present the choices as:

# blue

# red

# green
def halo(color:str) -> None:
        match color.lower():
            case 'blue':
                return "Great choice!"
            case 'green':
                return "Not a bad choice."
            case 'red':
                return "Poor choice."
            case _:
                return "Sorry, that's not a primary color."
            
# 9. Random Number < 50 or > 50
# Generate a random number between 1 and 100.

# If the number is less than 50 → output: "You chose a number less than 50."

# If more than 50 → output: "You chose a number more than 50."

def numRan() -> int:
    num = r.randint(1,100)
    if num<50:
        print("You chose a number less than 50.")
    elif num>50:
        print('You chose a number more than 50.')
    return num 

# 10. Functions Golf and Hotel
# Create a function called Golf that returns a random number between 1 and 6.
# Create a function called Hotel that uses Golf to simulate rolling two dice.
# Hotel should count how many turns it takes until both dice show the same number (e.g. both return 3).
# Output the total number of turns taken.

def golf()-> int:
    return r.randint(1,6)

def hotel():
    count = 1
    rolls = [golf(), golf()]
    while rolls[0] != rolls[1]:
        rolls = [golf(), golf()]
        count+=1
    return count

# 11. Function India
# Create a function called India that takes in a list x.
# It should traverse the list and output 0 for even numbers and 1 for odd numbers.
def india(ls:[]):
    return [0 if n % 2 == 0 else 1 for n in ls]

# 12. Function Juliett
# Create a function called Juliett that takes in an int number and returns:

# True if the number is even

# False if the number is odd
def juliet(n:int)-> bool:
    return n%2==0

# 13. Function Kilo
# Create a function called Kilo that takes in a list x.
# It should traverse the list and output half of each value to a file called theFile.txt.
def kilo(ls:list):
    with open('theFile2.txt', 'w') as f:
        f.write(' '.join(str(n/2) for n in ls))

# 14. Ternary Operator Pay Calculator
# Use the conditional operator (ternary operator) for this problem:

# Let PAY_RATE = 50 (a global constant)

# Ask the user for their HOURS_WORKED

# If HOURS_WORKED > 10, output: PAY_RATE * HOURS_WORKED

#Otherwise, output 0
def ter():
    global PAY_RATE
    PAY_RATE = 50
    HOURS_WORKED = int(input("How many hours did u work?"))
    return (PAY_RATE*HOURS_WORKED if HOURS_WORKED>10  else 0)

# 15. Function Lima (by reference)
# Create a function called Lima.
# It should take in name and age by reference.
# Ask the user for their name and age.
# Allow them three tries to enter a valid age (between 0 and 100, inclusive).
# If they fail, set age = 0.
def lima(nameAge:list):
    nameAge.insert(0,input("What is your name?"))
    age = -1
    atp  =0
    while atp < 3 and not(age >=0 and age <= 100):
        age = int(input("How old are you?"))
        atp+=1
    if age >=0 and age <= 100:
        nameAge.insert(1,age)
        return nameAge
    else:
        print("Age did not fall into range")
        return None

# 16. Celsius-Fahrenheit Table
# Use a for loop to list Celsius and Fahrenheit temperatures.

# Celsius (C) should go from -20 to 20

# Use the formula: F = (9/5) * C + 32
def cs():
    cel = [x for x in range(-20, 21)]
    far = [(9/5)*cels +32 for cels in cel]
    output  =[cel, far]
    return output
# 17. Fibonacci Sequence
# Use a for loop to list the first 20 Fibonacci numbers:
# 1, 1, 2, 3, 5, 8, 13, ...
def fib():
    nums = []
    nums.append(0)
    nums.append(1)
    nums.append(1)
    while len(nums)<20:
        nums.append(nums[-1]+nums[-2])
    return nums

# 18. Function Mike
# Create a function called Mike that takes in an int number.
# Return True if the number is prime, otherwise return False.
def mike(num:int)-> bool:
    return not any(num % n == 0 for n in range(2, num))

# 19. Function November
# Create a function called November that takes in an int grade.

# If 90–100 → output "You got an A"

# If 80–89 → output "You got a B"

# If 70–79 → output "You got a C"

# Below 70 → output "You did not pass"
def november(grade:int):
    if(grade>= 90):
        print("You got an A")
    elif grade>= 80:
        print("You got a B")
    elif grade>=70:
        print("You got a C")
    else:
        print("You did not pass")


def main():
    print("Question 1")
    alpha(5)
    print("Question 2")
    bravo()
    print("Question 3")
    print(charlie([3,2,4]))
    print("Question 4")
    print(delta())
    print("Question 5 in file")
    print("Question 6")
    echo()
    nums = []
    cur =1
    for n in range(10):
        nums.append(cur)
        cur =foxtrot(cur)
    print(' '.join(str(n) for n in nums))
    print("Question 7" )
    getColor(input('What is your favorite color '))
    print("Question 8" )
    print(halo(input('What is your favorite color ')))
    print('Question 9')
    print(f"Random number = {numRan()}")
    print("Question 10")
    print(hotel())
    print("Question 11")
    print(india([4,2,6,3]))
    print("Question 13 in theFIle2.txt")
    kilo([2,4])
    print("Question 14")
    print(ter())
    print("Question 15")
    nameAge = []
    print(lima(nameAge))
    print("Question 16")
    print(cs())
    print("Question 17")
    print(fib())
    print("Question 18")
    print(mike(3))
    print("Question 19")
    november(97)
main()