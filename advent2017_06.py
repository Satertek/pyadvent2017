#Brian Irelan
#sloppy solution for day 6

#data = [0,2,7,0]

data = [10,3,15,10,5,15,5,15,9,2,5,8,5,2,3,6]

data_list = []
data_list.append(data.copy())
print("Input: {}".format(data))
counter = 0
high_loc = 0
while(True):
    counter += 1
    high = max(data)
    #print("Data: {}, Max: {}, Counter: {}".format(data,high,counter))
    for i, each in enumerate(data):
        if each == max(data):
            data[i] = 0
            loc = i
            break
    while(True):
        if high < 1:
            break
        for i, each in enumerate(data):
            if high < 1:
                break
            loc+=1
            loc%=len(data)

            data[loc] += 1
            high -= 1
            #print("{}.{}) Data: {}".format(counter,high,data))
    #print("{}) Data: {} in Data_List: {}".format(counter, data, data_list))
    if data in data_list:
        print("Duplicate: {}, Counter: {}".format(data, counter))
        #print(data_list)
        id1 = data_list.index(data)
        id2 = len(data_list)
        id3 = id2 - id1
        #print("First Location: {}, Last Location: {}, Difference: {}".format(id1, id2, id3))
        break
    data_list.append(data.copy())

print("Day 6\nAnswer 1: {}\nAnswer 2: {}".format(counter, id3))