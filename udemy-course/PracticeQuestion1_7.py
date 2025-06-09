def main():
    # 1. Compound Interest Calculation
    # Ask the user for the interest rate, principal, and number of years they are investing.
    # Output the final amount earned.
    # Use the formula:
    # final amount = principal * (1 + interest_rate) ^ years
    ##########################################################
    # interestRate = float(input("What\'s the interest rate? "))
    # principal = float(input("What\'s the the principal? "))
    # year = int(input("How many years do plan on investing for? "))

    # print(f"\nInterest Rate:\t{interestRate:,.2f}%",
    #       f"Principal Amount:\t${principal:,.2f}",
    #       f"Number Of Years:\t{year:,}",
    #       f"\nYour final amount is:\t${principal*((1+interestRate/100)**year):,.2f}",sep="\n" ,end = "\n")
    #######################################################################################################
    
    #2. Name and Age Validation
    # Ask a user for their name and age.

    # Ensure that they give letters for their name.

    # Ensure that they give numbers for their age.

    # Ensure that the age is between 1 and 100, inclusive.

    # Give them three chances to provide valid input.

    # If they fail after three attempts, output:
    # "Unacceptable"

    # If both name and age are valid, output:
    # "Acceptable"
    ###################################################################################################
    # name = input("What is your name?\n")
    # validName = name.isalpha()
    # validAge =False
    # try:
    #     age = int(input("How old are you?\n"))
    #     if age>0 and age <100:
    #         validAge = True
    #     else:
    #         validAge =False

    # except ValueError:
    #     validAge = False
    
    # tries =1
    # while (not validAge or not validName) and tries<3:
    #     if  not validAge and not validName:
    #         name = input("What is your name? Only letters excepted!\n")
    #         validName = name.isalpha()
    #         try:
    #             age = int(input("How old are you?\n"))
    #             if age>0 and age <100:
    #                 validAge = True
    #             else:
    #                 validAge =False
    #         except ValueError:
    #             validAge = False
    #     elif not validName:
    #         name = input("What is your name? Only letters excepted!\n")
    #         validName = name.isalpha()
    #     else:
    #         try:
    #             age = int(input("How old are you?\n"))
    #             if age>0 and age <100:
    #                 validAge = True
    #             else:
    #                 validAge =False
    #         except ValueError:
    #             validAge = False
    #     tries+=1
    # if tries ==3:
    #     print("Too many attempts")
    # else:
    #     print("Accepatable")
    ########################################################################################

    # 3. Password Validation
    # Ask the user to create a password that meets the following criteria:

    # At least 8 characters long

    # Contains a number

    # Contains an uppercase letter

    # Contains a lowercase letter

    # Contains a special character

    # If the password is invalid, tell them which specific requirement is not met.
    # Give them unlimited attempts to get it correct.

    #######################################################################################
    # password = input("Whats the potenial password? Must have a upper case, lower case, number, and special character.\n")
    # properLen= len(password)>=8
    # hasUpper =False
    # hasLower = False
    # hasNum = False
    # hasSpecial=False
    
    # for let in password:
    #     if(let.isupper()):
    #         hasUpper = True
    #     if let.islower():
    #         hasLower = True
    #     if let.isnumeric():
    #         hasNum = True
    #     if not let.isalnum():
    #         hasSpecial = True
    
    # while not properLen or not hasUpper or not hasLower or not hasNum or not hasSpecial:
    #     if not properLen:
    #         print("Password must be 8 or more characters")
    #     if not hasUpper:
    #         print("Password must have an upper case letter.")
    #     if not hasLower:
    #         print("Password must have a lower case letter.")
    #     if not hasNum:
    #         print("Password must have a number.")
    #     if not hasSpecial:
    #         print("Password must have a special character")
    #     password = input("Whats the potenial password? Must have a upper case, lower case, number, and special character.\n")
    #     properLen = len(password)>=8
    #     hasUpper =False
    #     hasLower = False
    #     hasNum = False
    #     hasSpecial=False
    #     for let in password:
    #         if(let.isupper()):
    #             hasUpper = True
    #         if let.islower():
    #             hasLower = True
    #         if let.isnumeric():
    #             hasNum = True
    #         if not let.isalnum():
    #             hasSpecial = True
    # print("Password accepted!")
    ######################################################################################################

    #4. Numbers with the Digit "3"
    # Use a for loop to output every number between 1 and 1000 that contains the digit 3.
    # Separate the numbers with a bar |, like this:
    # 3 | 13 | 23 | ..
    # # ###################################################.
    # nums = []
    # for n in range(1,1000):
    #     for digit in str(n):
    #         if(digit=='3'):
    #             nums.append(n)
    # print(" | ".join(str(n) for n in nums))
    # ############################################################

    #5. Even Numbers Backwards
    # Use a while loop to output all the even numbers between 1 and 100, in reverse order, like this:
    # 100, 98, 96, ...
    num =100
    evens = []
    while num>=1:
        evens.append(num)
        num-=2
    print(", ".join(str(n) for n in evens))

if __name__ == '__main__':
    main() 