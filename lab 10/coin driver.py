#coin driver
import coinclass
def main():
    #create object
    mycoin = coinclass.Coin()
    print('----')
    print('Side up:', mycoin.get_sideup()) #shows what side is up

    #toss coin
    mycoin.toss()

    #display coin side

    print('Side up:', mycoin.get_sideup())

main()
    
