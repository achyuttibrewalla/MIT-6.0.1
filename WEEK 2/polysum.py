def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   l=[]
   for item in list_of_numbers:
        l.append([[simple_divide(item, denom)]])
        
   return l

def simple_divide(item, denom):
   return item / denom