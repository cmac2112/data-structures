#array module

class Array(object):
    def __init__ (self, capacity, fillValue = None):
        self.items = list() #defining static array, replaces none elemnts with
        #filler values
        for count in range(capacity):
            self.items.append(fillValue)

    def __len__(self): #capacity of array
        return len(self.items)

    def __str__(self):
        #string of array
        return str(self.items)

    def __iter__(self):
        #supports traversal with for loop
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index] #access at index

    def __setitem__(self, index, newItem):
        self.items[index] = newItem #replacement at index


