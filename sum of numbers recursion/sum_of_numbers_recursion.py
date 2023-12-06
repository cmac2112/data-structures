def main():
    #variables
    number = 0
    number_sum = 0

    #get number from the user > 0
    while number <= 0:
        number = int(input('Enter an integer > 0: '))

        # loop
        for x in range(1, number + 1):
            number_sum += x
            #accumulates number
        #display the sum of the nuber
        print("the sum of" (number) "is" (number_sum))


main()