num=int(input("Enter a number"))
original_number=num
reversed_number=0
while(num!=0):
    remainder=num%10
    reversed_number=reversed_number*10 + remainder
    num=num/10
if(reversed_number == original_number):
    print("{}is a palindrome number".format(original_number))
else:
    print("{}is not a palindrome number".format(original_number))