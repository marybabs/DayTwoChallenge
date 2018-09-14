
def fizzbuzz():
    x=[1,2,4.5]
    y=[6,7,0]
    z=len(x)+len(y)
    if z%3==0 and z%5==0:
        print("FizzBuzz")
    elif z%3==0:
        print("Fizz")
    elif z%5==0:
        print("Buzz")
    
    else:
        print(z)

fizzbuzz()

