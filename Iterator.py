#In python Iterator is an object ,which returns one element at a time from data containers.
int(0)
inf =iter(int,1)
next(inf)
next(inf)

'''
#Internal Structre of For loop

for element in iterable:
    #Do something with element
# create an iterator object from that iterable
iter_obj = iter(iterable)

# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break

# define a list
my_list = [4, 7, 0, 3]


my_iter = iter(my_list)
print(next(my_iter))
print(next(my_iter))
print(my_iter.__next__())

print(my_iter.__next__())

## This will raise error, no items left
#next(my_iter)
'''

'''

from itertools import cycle
dessert = cycle(['1','2','3','4','5','6','7','8','9','10'])
count = 0
while(count != 7):
    print('Q. What do we have for dessert? A: ' + next(dessert))
    count+=1




from itertools import count
sequence = count(start=0, step=1)
while(next(sequence) <= 10):
    print(next(sequence))
    '''

'''
list=[10,20,30]
iter1=iter(list)
print(next(iter1))
print(type(list))#<class 'list'>

print(type(iter1))#<class 'list_iterator'>

class Series():


    def __init__(self,low,high):
        self.Low = low
        self.High = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.Low <= self.High:
            result = self.Low
            self.Low+=1
            return result
        else:
         raise StopIteration


n_list =Series(1,10)
my_iter=iter(n_list)
'''
'''
print(next(my_iter))
print(my_iter.__next__())
print(my_iter.__next__())
'''

'''
for item in n_list:
    print(item)
'''


'''
while True:
    try:
        print(next(my_iter))
    except:

        print('Element Finished')
        break;
'''
