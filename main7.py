import sys
sys.set_int_max_str_digits(999999999)
def raise_to_the_degrees(number):
    i=0
    while True:
        yield number**i
        i+=1

res = raise_to_the_degrees(122345)
print(res)
for _ in res:
    print(_)