import csv

#function to calculate Mean
def Mean(dataSet):
    #variable to hold the sum of the data set
    tot = 0
    #reading Each Value in the given data set
    for value in dataSet:
        tot = tot+float(value)
    #deviding the sum by the data set length to get the mean
    mean = tot / (len(dataSet))
    #returning the mean of the dataset
    return round(mean,3)


# calculate Median
def Median(dataset):
    #sorting the value set minimum to highest
    dataset.sort()
    #get the length of the data set
    length = len(dataset)
    #if the length can be devided by two and remains 0 we need to get the middle two vallues
    if length % 2 == 0:
        #middle two values
        median1 = dataset[length // 2]
        median2 = dataset[length // 2 - 1]
        #getting the median by summing the two values and devide by 2
        median = (float(median1)+ float(median2)) / 2
    else:
        # if the length cannot be devided by two and remains other than zero,
        # devide the dataset by two to get the median
        median = round((float(dataset[length // 2])),3)
    #returning the median
    return median


# calculate Standard_deviation
def Standard_deviation(dataSet):
    #calling the mean function to get the mean of the data set
    mean = Mean(dataSet)
    #get the length of the dataset
    length = len(dataSet)
    #ceating a variable to hold the calculating value
    findStV = 0
    #for every value in the dataset
    for value in dataSet:
        #summing the previous findStV value to each value - mean and get the square root of it
        findStV = findStV + ((float(value) - mean) ** 2)
    #after going through the loop findStV value will devide by the length of the dataset
    # and assign it to a new variable
    standDev = findStV / length
    #rounding the number in to two decimal points
    finalresult = round(float((standDev)**0.5),3)
    #return the standard deviation of the data set
    return finalresult


# calculate Varience
def Varience(dataSet):
    #get the length of the dataset
    length = len(dataSet)
    # calling the mean function to get the mean of the data set
    mean = Mean(dataSet)
    # ceating a variable to hold the calculating value
    calValue = 0
    #calculating the variance by deviding the standard deviation by the lengthof the data set
    # and assign it to a new variable
    for value in dataSet:
        #summing the previous calValue value to each value - mean and get the square root of it
        calValue = calValue + ((float(value) - mean) ** 2)
    varience = calValue / length
    #returning the variance of the data set
    return round(varience,3)


# calculate Root mean square
def Root_mean_square(dataSet):
    #new variable to hold the square root
    squreRoo = 0
    # new variable to hold the sum of square root
    sumSquareRoo = 0
    #getting the length of the dataset
    length = len(dataSet)
    #looping every value in the dataset
    for value in dataSet:
        #calculating the square root of each value
        squreRoo = (float(value) ** 2)
        #get the sum of all square root value
        sumSquareRoo = sumSquareRoo + squreRoo
    #deviding the sum of the square root by the length assign it to a new variable
    devide = sumSquareRoo / length
    #get the square root mean
    sqrtMean = devide ** 0.5
    #returning the rootMeanSquare
    return round(sqrtMean,3)


# calculate Sum of squares
def Sum_Of_Squares(dataSet):
    # geth the length of the data set
    length = len(dataSet)
    #calculating the mean of the data set by calling the Mean function
    mean = Mean(dataSet)
    #variable for individual deviation
    indiviDevia = 0
    #variable for hold the square of each value
    squareEach = 0
    #variable to hold the sum of each square
    sumSqEach = 0
    #for each value in the dataset
    for value in dataSet:
        #get the individual deviation
        indiviDevia = mean - float(value)
        #get the square of the each value
        squareEach = (float(indiviDevia)) * (float(indiviDevia))
        #summing the square each value
        sumSqEach = sumSqEach + squareEach
    #return sum of square
    return round(sumSqEach,3)


# calculate Zero Crossing
def Zero_Crossing(dataSet):
    #creating the new variable to hold the zerocrossing value
    zeroCrossing = 0
    #getting the value via a for loop within the range of 0 to lengthof the dataset
    for value in range(1, len(dataSet)):
        #checking each value whether the value -1 is greater than to zer oand value is less than 0,
        #if so there will be a zeroCrossing (lower curve)
        if dataSet[value - 1] > 0 and dataSet[value] < 0:
            zeroCrossing = zeroCrossing+1
        # checking each value whether the value -1 is less than to zero and value is greater than 0,
        # if so there will be a zeroCrossing (upper curve)
        if dataSet[value - 1] < 0 and dataSet[value] > 0:
            zeroCrossing = zeroCrossing+1
    #returning the count of zerocrossing
    return zeroCrossing


#write the CSV File
def WriteCSV(row1Dict,fileName):
    #openning the csv file with the given name
    #this will save as a .csv file
    if '.csv' in fileName:
        newFileName =fileName
    else:
        newFileName =fileName+".csv"
    with open(newFileName, "w") as outfile:
        #writing the csv.
        writer = csv.writer(outfile)
        #writer.writeheader()
        writer.writerow((row1Dict.keys()))
        writer.writerows(zip(*row1Dict.values()))


# calculate Covariance
def Covariance(dataSet1, dataSet2,dataSet3):
   # try:
        if len(dataSet1)==len(dataSet2)==len(dataSet3):
            #get the length of the data set
            length = len(dataSet1)
            sumOf1 = 0
            #get the mean of the data set one
            dataSet1Mn = Mean(dataSet1)
            # get the mean of the data set two
            dataSet2Mn = Mean(dataSet2)
            dataSet3Mn = Mean(dataSet3)
            #creating empty array lists
            row1List = []
            row2List = []
            row3List=[]
            fullList = []
            #get the difference for each value of the dataset1 by substracting the mean from each value
            for value in dataSet1:
                row1 = float(value) - dataSet1Mn
                #appending the value to the pre definded list
                row1List.append(row1)
            # get the difference for each value of the dataset2 by substracting the mean from each value
            for value2 in dataSet2:
                row2 = float(value2) - dataSet2Mn
                # appending the value to the pre definded list
                row2List.append(row2)
            for value3 in dataSet3:
                row3 = float(value3) - dataSet3Mn
                # appending the value to the pre definded list
                row3List.append(row3)
            #using zip function to parallel iteratiion of the above two lists
            for entry1, entry2, entry3 in zip(row1List, row2List,row3List):
                #then append them in to another list which is the final list
                fullList.append(entry1 * entry2 * entry3 )
            #get the sum of the final list after iteration
            mutiplyTwo = (sum(fullList))
            #calculate the covariance of the two lists by deviding the sum of the final list by the length of the data set
            covarience = mutiplyTwo / (length - 1)
            #returning the covariance of the given data set
            return round(covarience,3)
        else:
            print("Row lengths are not equal")
    # except:
    #     print("=====================================================")
    #     print("Ohhhhh! Something went wrong! Please try again later!")
    #     print("=====================================================")
    # finally:
    #     print("=========================================================================")
    #     print("Thank you for using Activity context recognition system. Have a good day!")
    #     print("=========================================================================")

# calculate Covariance
# def Covariance2(dataSet1, dataSet2):
#     #get the length of the data set
#     length = len(dataSet1)
#     sumOf1 = 0
#     #get the mean of the data set one
#     dataSet1Mn = Mean(dataSet1)
#     # get the mean of the data set two
#     dataSet2Mn = Mean(dataSet2)
#     #creating empty array lists
#     row1List = []
#     row2List = []
#     fullList = []
#     #get the difference for each value of the dataset1 by substracting the mean from each value
#     for value in dataSet1:
#         row1 = float(value) - dataSet1Mn
#         #appending the value to the pre definded list
#         row1List.append(row1)
#     # get the difference for each value of the dataset2 by substracting the mean from each value
#     for value2 in dataSet2:
#         row2 = float(value2) - dataSet2Mn
#         # appending the value to the pre definded list
#         row2List.append(row2)
#     #using zip function to parallel iteratiion of the above two lists
#     for entry1, entry2 in zip(row1List, row2List):
#         #then append them in to another list which is the final list
#         fullList.append(entry1 * entry2)
#     #get the sum of the final list after iteration
#     mutiplyTwo = (sum(fullList))
#     #calculate the covariance of the two lists by deviding the sum of the final list by the length of the data set
#     covarience = mutiplyTwo / (length - 1)
#     #returning the covariance of the given data set
#     return round(covarience,3)


#def add_column_in_csv(input_file, output_file, transform_row):
    #with open(input_file, 'r') as read_obj, \
            #open(output_file, 'w') as write_obj:
        #csv_reader = reader(read_obj)
        #csv_writer = writer(write_obj)
        #for row in csv_reader:
            #transform_row(row, csv_reader.line_num)
            #csv_writer.writerows(row)












