# -*- coding: utf-8 -*-
import sys

def readFile(fileName):
    f = open(fileName,'r')
    newArray = []
    for string in f:
        myArray =  string.split(' ')
        myArray = myArray[:len(myArray)]
        newArray.append(map(int, myArray))
    f.close()
    return newArray

def findUser(x):
    for i in DBArray:
        if i[0] == x:
            return i
        
def merge_sort(li):
    if len(li) < 2: return li 
    m = len(li) / 2 
    return merge(merge_sort(li[:m]), merge_sort(li[m:]))

def merge(l, r):
    global count
    result = [] 
    i = j = 0 
    while i < len(l) and j < len(r): 
        if l[i] < r[j]: 
            result.append(l[i])
            i += 1 
        else: 
            result.append(r[j])
            count = count + (len(l) - i)
            j += 1
    result.extend(l[i:]) 
    result.extend(r[j:]) 
    return result 

def findInversions(DBArray, userArray):  
    for i in DBArray:
        num = i.pop(0)
        k=0    
        count=0
        for j in i:
            tempArray[userArray[k]-1] = j;
            k+=1
        print(merge_sort(tempArray))
        print count    
        string = str(num)+" "+str(count)+"\n"
        f.write(string)

def createTempArray(tempArray):
    l=0
    while l<m :
        tempArray.append(0)
        l+=1

def returnTempIndexArray(tempArray,i):
    k=0
    for j in i:
        tempArray[userArray[k]-1] = j;
        k+=1
        
        
argv = []
for param in sys.argv:
    argv.append(param)
fileToRead = argv[1]
x = int(argv[2])
DBArray = readFile(fileToRead)
u = DBArray[0][0]
m = DBArray[0][1]
tempArray = []
createTempArray(tempArray)
DBArray.pop(0)
userArray = findUser(x)
userArray.pop(0)
DBArray.pop(x-1)
f = open('output.txt','w')
f.write(str(x))
f.write("\n")
sortedArrays = []
for i in DBArray:
    num = i.pop(0)        
    count=0
    returnTempIndexArray(tempArray,i)
    merge_sort(tempArray)
    string = str(num)+" "+str(count)+"\n" 
    f.write(string)
f.close();   

        
      
        
        
        
        
        
        
        
        