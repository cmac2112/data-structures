def main():
    diction = {k1: {k2: k1 + k2 for k2 in range(1, 6)} for k1 in range(2,5)}
    print(diction)
main()
