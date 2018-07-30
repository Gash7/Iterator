#A function defined inside another function is called a nested function. Nested functions can access variables of the enclosing scope.
#In Python, these non-local variables are read only by default and we must declare them explicitly as non-local (using nonlocal keyword) in order to modify them.
#The criteria that must be met to create closure in Python are summarized in the following points.
'''
We must have a nested function (function inside a function).
The nested function must refer to a value defined in the enclosing function.
The enclosing function must return the nested function.
'''

def print_msg(msg):
    # This is the outer enclosing function

    def printer(msg):
        # This is the nested function
        print(msg)

    printer()

# We execute the function
# Output: Hello
print_msg("Hello")


def print_msg(msg):
    # This is the outer enclosing function

    def printer(meg):
        # This is the nested function
        print(msg)

    return printer  # this got changed

# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
another()
another()



print('-------------------')
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

print('-------------------')


#Pass By Refrence
a=[1,2,3,4,5,6]
def Hello(x):
    x[0]=12
    print(x)
    return
Hello(a)
print(a)




#Pass by Value
def hello(x):
    print(x)
    return
x=13
hello(x)


def f1():
    print('1')

    def f2():
        print('2')

        def f3():
            print('3')

            def f4():
                print('4')
            f4()
        f3()
    f2()
f1()





count=10
def clouser():
    #global count
    #count=20
    print('Inside Out Function',count)

    def Clouser():
     global count
     #nonlocal count
     #count=30
     print('Outsie Out Function',count)
    return Clouser



p =clouser()
p()
