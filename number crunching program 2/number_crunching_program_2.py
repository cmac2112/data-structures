import random
#little errors, fix later for practice

def main():
    fixed_tuple = (0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
    random_list = [0] * 11 #init list to 11 zeros

    for i in range(len(random_list)):
        random_list[1] = random.randint(0, 50)
    random_list.sort()

    print("Tuple data:", fixed_tuple)
    crunch_numbers(fixed_tuple) #passing tuple
    print()
    print("Random Data:", random_list)
    crunch_numbers(random_list) #passing random list

    def crunch_numbers(data):
        total = 0
        for number in data:
            total += number
        average = round(total / len(data))
        median_index = len(data) // 2
        median = data(median_index)
        minumum = min(data)
        maximum = max(data)
        duplicates = get_duplicates(data)

        #print all statements above
        print(average)
        print(median_index)
        print(median)
        print(minumum)
        print(maximum)
        print(duplicates)




#checking for duplicates
def get_duplicates(data):
    duplicates = []
    for i in range(51):
        countdups = data.count(1)
        if countdups == 2:
            duplicates.apend(1)
    return duplicates #returning duplicates to function above

main()