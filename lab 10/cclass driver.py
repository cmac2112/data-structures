#using coin class from page 750ish
#arrays and recursion
#caden mcarthur
import cclass
import cArray


#put results into array, recursive functions to flip coin
#display head count / tail count, percentage
def main():
    mycoin = cclass.Coin()# create all needed objects
    counter = cArray.Array(50) #create array with 50 spaces
    print('Flipping coin...')
    flipper(counter, mycoin, 0, 0)
    
def flipper(counter, mycoin, flips, index): # make this recursive
    
    
    if flips == 50: #base case, index is used to count index in array
        print('Results, 1 = heads 0 = tails')
        print(counter)
        find_count(counter)
    else:
        mycoin.toss() #toss coin from module
        if mycoin.get_side() == 1:
            counter[index] = 1 # if flip is 1 (heads) 'appends' 1 to array at given index
            return flipper(counter, mycoin, flips + 1, index + 1) #recursive
        
        else:
            counter[index] = 0 #if flip is 0 (tails) 'appends' 0 to array at given index
            
            return flipper(counter, mycoin, flips + 1, index + 1) #recursive

def find_count(counter): #simple for loop to count iterations of 1 in array
    count = 0
    for i in counter:
        if i == 1:
            count += 1
    return calculate(count)
    

def calculate(count): #display results
    print(count)
    print('Calculating results:')
    print('Times landed on heads:', count)
    ratio = (count / 50) #calculate percentage
    percentage = (ratio * 100)
    print('Landed on heads',percentage, '% of the time.')

    
        
    

main()
