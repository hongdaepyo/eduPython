abs(-1.2) #1.2

all([1,2,3]) #True
all([1,2,3,0]) #False

any([1,2,3,0]) #True
any(["",0]) #False

chr(97) #a
chr(48) #0
chr(65) #A

dir(1) #['__abs__', '__add__', '__and__', '__bool__', '__ceil__',

divmod(999,4) #(249, 3)

for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

# 0 body
# 1 foo
# 2 bar

list(filter(lambda x: x > 0, [1, -3, 2 , 0, -5, 6]))

hex(2,3,4)

int(3.4)
int('1A', 16)

id(3)

class Person: pass
a = Person()
isinstance(a, Person)

len("python")
len([1,2,3])
len((1, 'a'))

list("python")
list((1,2,3))

def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result

result = two_times([1, 2, 3, 4])
print(result)

def two_times(x):
    return x * 2

list(map(two_times, [1, 2, 3, 4]))

list(map(lambda x: x * 2, [1, 2, 3, 4]))

max([1, 2, 3])
max("python123A")

min([1, 2, 3])
min("python123A")

oct(34)
oct(1234)

f = open("binary_file", "rb")

ord('a')
ord('0')

pow(3, 3)
pow(7, 4)

list(range(5))
list(range(5, 10))
list(range(5, 10, 2))

round(4.6)
round(5.3)

sorted([3, 2, 1])
sorted(['a', 'c', 'b'])

str(3)
str('hi')
str('hi'.upper())

sum([2, 3, 5])

tuple("abc")
tuple([1, 2, 3])

type("abc")
type([])
type(set())
type({})

list(zip([1,2,3], [4,5,6]))
list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
list(zip(["a", "b", "c"], [1, 2, 3]))

all([1, 2, abs(-3)-3])
chr(ord('a')) == 'a'

#list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3]))

#hex(234)
#int('0xea', 16)

list(map(lambda x: x * 3, [1,2,3,4]))
