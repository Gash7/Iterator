class Itrator:

    def __init__(self,start,end):
        self.Start=start
        self.End=end

    def __iter__(self):
        return self


    def __next__(self):
        if self.Start<=self.End:
           result = self.Start
           self.Start += 1
           return result
           #print(self.Start)

        else:
         raise StopIteration


iet =Itrator(0,10)


while True:

    try:
        print(next(iet))
    except:
        break

''' 
for item in iet:
    print(item)
     
print(next(iet))
print(next(iet))
print(next(iet))
print(next(iet))
print(next(iet))
'''




