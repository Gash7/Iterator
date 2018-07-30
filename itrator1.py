
'''

list=[]
for item in range(0,16):
 list.append(item)
 print(item)

'''

'''
class ite:

    def __init__(self,start,end):
        self.start=start
        self.end=end

    def __iter__(self):
        return self

    def __next__(self):

        if self.start<=self.end:
            result=self.start
            self.start +=1
            return result

my_it=ite(0,20)

my_iter1 =iter(my_it)
print(next(my_iter1))
print(next(my_iter1))
print(next(my_iter1))
print(next(my_iter1))








list =[10,20,30,40,50,60]
print('!st Element -------------')


my_iter=iter(list)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
'''