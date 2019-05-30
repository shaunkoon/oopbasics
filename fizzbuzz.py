def fizz(num3):
    if num3 % 3 == 0:
        return 'Fizz'
    else: return num3

def buzz(num5):
    if num5 % 5 == 0:
        return 'Buzz'
    else: return num5

def fzbz(num15):
    if num15 % 15 == 0:
        return 'FizzBuzz'
    else: return num15




num = 1
while num <= 100:
    if type(fzbz(num)) == type('poop'):
        print(fzbz(num))
    elif type(buzz(num)) == type('poop'):
        print(buzz(num))
    elif type(fizz(num)) == type('poop'):
        print(fizz(num))
    else: print(num)
    num += 1
###########################################################
# def fizzbuzz():
#     num = 1
#     while num <= 100:
#         if num % 15 == 0:
#             print('FizzBuzz')
#         elif num % 5 == 0:
#             print('Buzz')
#         elif num % 3 == 0:
#             print('Fizz')
#         else: print(num)
#         num += 1
# print(fizzbuzz())

