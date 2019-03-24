x=1
y=2
if x>y:
    print('x가 y보다 큽니다')
elif x<y:
    print('x가 y보다 작습니다.')
else:
    print('x와 y가 같습니다.')



scope = [1,2,3,4,5]
for x in scope:
    print(x)

str  = 'abcdef'
for c in str:
    print(c)

ascii_codes = {'a':97,'b':98,'c':99}
for c in ascii_codes:
    print(ascii_codes[c])

k = range(10)
for c in range(10):
    print(c)