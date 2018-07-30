from builtins import print


def yield_Base():

    print('Hi')
    yield

    print('Hello')
    yield

    print('World')

y=yield_Base()

print(next(y))

print(next(y))




'''

    def GenMax(max=0):
        n=0
        while n<=max:
            yield 2**n
            n += 1
    
    p = GenMax(5)
    
    
    while True:
    
        try:
            print(next(p))
        except:
            break

'''