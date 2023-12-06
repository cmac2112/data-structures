#caden mcarthur
#lab 12 dictionairy comprehension

def main():
    pretax = {'bread': 1.00, 'milk': 3.00, 'Soda': 1.20, 'phone': 600.00, 'charger': 20.00}

    taxes = 0.15
    posttax = {item: ((value*taxes) + value) for (item, value) in pretax.items()}
    print(posttax)
main()
