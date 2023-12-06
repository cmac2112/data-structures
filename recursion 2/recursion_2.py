def main():
    number = 0
    while number <= 0:
        number = int(input('Enter integer > 0:'))

    #get sum of number
    num_sum = sum_number(number)

    print(num_sum)
    print(number)
def sum_number(num):
   if num == 1:
      return 1
   else:
         return num + sum_number(num - 1)

main()

