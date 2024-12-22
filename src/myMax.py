def myMax(*nums): # Function definded with nums 
    numList = nums # capture parameter in variable
    max = numList[0] # set the first value in list
    for i in numList: #make sure loop terminates with last value
        if i > max: # check each value in list  and replace if new number is greater than previous
            max = i
    print(max) #Print value
myMax(100,10, 69)
