def odd():
    number = 1
    while True:
        yield number
        number += 2


odd_num = odd()

for i in range(1, 100):
    print(next(odd_num))