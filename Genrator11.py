def GetPower(max=1):
    n=0

    while n<=max:
        yield 2**n
        n +=1
    else:
      Exception

it=GetPower(10)

while True:

        try:
            print(next(it))
        except:
            break





def GenMax(max=0):
    n=0
    while n<=max:
        yield 2**n
        n += 1

p = GenMax(5)


while True:

    try:
        print('Don not print',next(p))
    except:
        break


def showDetails():
    #User_Input=input('Enter the Str "a"---------')
    #User_Input=input('Enter the Str "b"---------')



    print('Content Equality')
    yield


    print('Refrence Equlity')
    yield


    print('Invalid Entery')

obj = showDetails()

print(next(obj))
print(next(obj))