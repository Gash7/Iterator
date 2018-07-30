
'''An Iterator which share one element at a time from contianer of elements'''
'''For loop internal Structure----for an Iterator'''

class Iterator:

    def __init__(self,First,Last):
        self.First = First
        self.Last = Last

    def __iter__(self):
        return self

    def __next__(self):
         if self.First <= self.Last:
             result =self.First
             self.First +=1
             return result

         else:
          Exception



ob = Iterator(0,20)
ob_iter =iter(ob)

while True:
    try:
        print(next(ob_iter))
    except:
     break





'''
print('Method First-------')
ob_iter=iter(ob)
print(next(ob_iter))
print(next(ob_iter))
print(next(ob_iter))
print(next(ob_iter))
print(next(ob_iter))
print(next(ob_iter))
'''
