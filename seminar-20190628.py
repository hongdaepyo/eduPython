#bool -> True, False

a = True
b = False

1 == 1
2 > 1
2 < 1
a = [1, 2 ,3]

while a:
    print(a.pop())

if []:
    print("참")
else:
    print("거짓")

if [1, 2, 3]:
    print("참")
else:
    print("거짓")

type(bool('python'))

bool('')

bool([1, 2, 3])
bool([])
bool(0)
bool(3)

a = [1, 2, 3]
id(a)

b = a

id(b)

a[1] = 4
a
b

a = [1, 2, 3]

b = a[:]

a[1] = 4

a, b = ('python', 'life')
(a, b) = 'python', 'life'
a, b = 'python3', 'life3'
a
b
a, b = "test다들어간다"
a, b = 1, 2
a, b = b, a
a , b = 1, 2, 3

money = False
print(1 | 2)
1 = 01(2)
2 = 10(2)