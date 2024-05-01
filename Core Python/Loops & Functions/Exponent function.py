
# Exponent function allows us take a number and raise it to a power
print(2**3)     # basic and simple way

# with function
def raise_2_power(base_num,pow_num):
    result = 1
    for i in range(pow_num):
        result = result * base_num
# we create a variable named result,
# and we wanna power our base number (as power number)
# basically it is like this: base_num ** pow_num
# for every item in range of power number,
# result will be multiplied by our base number (1 * base_num = base num, so our result is now base_num; base_num * base_num= square of base num whic is our result now; ...)
# this continue till "i" reaches to power number
    return result

print(raise_2_power(3, 4))

