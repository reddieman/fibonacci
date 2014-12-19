# Allows user to decide how many fibonacci numbers is desired to be listed
fibo_range = int(raw_input("Enter how many \
Fibonacci numbers you want listed: "))
# starts off with '0' in a list
fibo_list = [0]

'''
Function defined with an If to catch condition when only 1 number is desired (starts with '0' by default and therefore prints '0').

For all else
'1' is appended directly first to start off the Fibo sequence.

Since two numbers are already defined the fibo_range, it must be deducted by '2' for the end list to match the number requested by user during input.

As I am writting this I noticed plenty of trimming can be done, but for now it works :)
'''
def fibo_numbers(fibo_range):
    if fibo_range == 1:
        print fibo_list
    else:
        fibo_list.append(1)
        for number in range(2, fibo_range):
            fibo_list.append(\
            fibo_list[len(fibo_list) - 1] + \
            fibo_list[len(fibo_list) - 2]
            )
        print fibo_list
        
fibo_numbers(fibo_range)
