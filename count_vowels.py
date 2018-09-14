def my_vowels():
    string=input( "Enter a string: ")
    vowels = ["a","i", "e","o","u"]
    # vowl is a string of vowels that are in the input
    vowl=""
    # count is the unduplicated list
    count = set(string)
    # count-x is the number of duplicated characters
    count_x=len(string)-len(count)
    
    for i in vowels:
        if i in string:
            vowl += i
    print((vowl,count_x))
my_vowels()