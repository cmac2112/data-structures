def main():
    acc = [5658845, 4520125, 7895122, 8777541, 8451277, 1302850,
           8080152, 4562555, 5552012, 5050552, 7825877, 1250255,
           1005231, 6545231, 3852085, 7576651, 7881200, 4581002]

    #sort list






def binarySearch(acc, low, high, Ans):
    #looking for ans in using binary recursive
    mid = 0
    if low <= high:
        mid = (high + low) // 2
        #if element is present at midpoint
        if acc[mid] == Ans:
            return mid #return the midpoint as found
        #if element is smaller, look to left
        elif acc[mid] > Ans:
            return binarySearch(acc, low, mid - 1, Ans) #recursive loop to look again only using left side
        else:
            #if not in left, then look right again
            return binarySearch(acc, mid + 1, high, Ans)
    else:
        #can not find element
        return -1

def swap(wlist, i, j):
    # Exchange the items at positions i and j.
    temp = wlist[i]
    wlist[i] = wlist[j]
    wlist[j] = temp
    
def selectionSort(wlist):

    for i in range(len(wlist)): # loop though each item in the list
        minIndex = i
        for j in range(i + 1, len(wlist)):  # loop to compare each items in the list
            if wlist[j] < wlist[minIndex]:
                minIndex = j
        if minIndex != i:
            swap(wlist,minIndex, i)  # Exchange item in the list
        i += 1
