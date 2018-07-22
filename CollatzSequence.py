# This script will explore a Collatz sequence

def collatz(number):
    
    # Determine if input is even or odd 
    if (number % 2) == 0 :

        # Even so Divide by 2
        # Note: '//' is interger division single '/' is float division
        nextNumber = number//2  
    else:
        
        # Odd so Multiply by 3 then add 1
        nextNumber = number*3 + 1

    # Print Next number
    print(nextNumber)

    if nextNumber == 1: 
        
        # Done, Exit the program
        return 1

    else:

        # Run through sequence again
        collatz(nextNumber)

def main():
    
    print('Please Enter an Interger')

    # Check if user input a positive integer 
    try:
        userinput = int(input())
        collatz(userinput)
    except ValueError:
        print('\nYou must enter an Integer!\n')

if __name__ == "__main__":
    main()