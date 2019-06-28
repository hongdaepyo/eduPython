#bool -> True, False

a = True
b = False

1 == 1
2 > 1
2 < 1

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

bool('python')

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

a = [1, 2, 3]
b = a[:]

a[1] = 4
