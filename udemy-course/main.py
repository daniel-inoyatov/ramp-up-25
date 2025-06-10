def main():
    #gathering users infor
    #name = input("Whats ur name")
    #age = int(input("Whats ur age"))
    #ageInSeconds  =age *365*24*60*60

    #print("\nYour name is:\t" + name +"\nYour age is seconds is:\t"+ str(ageInSeconds))

    #regular division
    #5/2
    #int division
    #print(5//2)

    #Length for rect a
    # lenA = int(input("What is the length of rect A?\t"))
    # #Width for rect a
    # widA = int(input("What is the width for rect A?\t"))

    # #Length for rect b
    # lenB = int(input("What is the length of rect B?\t"))
    # #Width for rect b
    # widB = int(input("What is the width for rect B?\t"))

    # areaA = lenA*widA
    # areaB = lenB*widB
    # print(f"Area for A is {areaA}", 
    #       f"Area for B is {areaB}")
    # if(areaA> areaB):
    #     print("A is larger")
    # elif areaB>areaA:
    #     print("B is larger")
    # else:
    #     print("They are the same")

    guess = input("Guess the word ")
    counter = 0
    while guess.lower() != 'secret':
        print("try again")
        guess = input("Guess the word ")
        if(counter>=3):
            break
        counter+=1

    
if __name__ == '__main__':
    main()  