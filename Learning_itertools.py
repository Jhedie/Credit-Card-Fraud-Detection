import itertools

'''
Inbuilt iterators:

* lists,
* Tuples
* Dictionaries
* Sets

The above can be said to be exhaustive
'''
'''

#Itertools can provide infinite iterators



#the below almost works like a for loop
print('count(start, step) it starts printing from the start number and prints infinitely')

for number in itertools.count(2,2):
    #limit is 10
    if number == 10:
        break
    else:
        print(number, end = ', ')


print('itertools.cycle(iterable) prints all values(iterable) in order in a cyclic manner')
count = 16
print('Example 1')
for i in itertools.cycle('JedAwuku'):
    if count <= 0:
        break
    else:
        print(i, end= ' ')
        count -=1
print()
print('-----------------------------------')
print('Example 2 implementing the next function')
list1 = ['eggs', 'bacon', 'hashbrowns', 'chocolate', 'bread']
#set list as  a cycle
iterators = itertools.cycle(list1)

for i in range(10):
    #use the next function
    print(next(iterators), end = ' ')
print()
print('------------------------------------------------------')
print('itertools.repeat(val, num) repeatedly prints the passed value "num" times')
print('Printing the numbers repeatedly :' + str(list(itertools.repeat(10, 5))))

print('\n\n\n')
'''
print('The cartesian product using repeat: ')
print(list(itertools.product([1,2], repeat = 2)))
print()
          
print('The cartesian product of the containers: ')
print(list(itertools.product(['a','b','c'], ['d', 'e', 'f'])))
print()


