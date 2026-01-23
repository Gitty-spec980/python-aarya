#Write a Python program that takes a name as an input from the user and then creates a function that accepts the same name as a parameter and greets the user.

# def greet(n):
#     print("Hello",n,", Good evening.")

# name=input("Enter a name:")
# greet(name)



#Write a Python program that will take a number as an input from the user and then creates a function that accepts the same number as a parameter and returns its absolute value. (Example - a negative number is converted to a positive number, the positive number remains the same).

def isPalindrome(str):
    lp=0
    rp=len(str)-1

    while rp>=lp:
        if not str[lp]==str[rp]:
            return False
        lp=lp+1
        rp-=1
    return True

name=input("Enter a word:")
print("Is this a Palindrome?")
print(isPalindrome(name))