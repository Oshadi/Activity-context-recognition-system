import csv
import feature_module as features
import os.path

#Function to load the csv file
def activity_data(file_path):
    fileExist = os.path.exists(file_path)
    try:
        if fileExist ==True:
            file = open(file_path, "r")
            #reading opened file as a dictionary
            readDictionary = csv.DictReader(file)
            #new dictionary
            row1Dict = {}
            #iterating a dictionary
            for row in readDictionary:
                #iterating row list
                for key, value in row.items():
                    #eliminating unwanted columns from the dictionary
                    if key != "_id" and key != "lux" and key != "soundLevel" and key != "activity":
                        #setting values as the key of the dictionary
                        #checking the value is already in the dictionary as the key
                        if key in row1Dict:
                            row1Dict[key].append(value)
                        #if not set that value as the key
                        else:
                            row1Dict[key] = [value]
            #closing the file stream
            file.close()
            #returning the computed dictionary
            return row1Dict
        else:
            return 0;
    except:
        print("Ohhhhh! Something went wrong! Please try again later!")



def activity_features_individual(data,featurename,axis):
    indDict={}
    if featurename == 'Mean':
        indDict[axis] = features.Mean(data[axis])
    if featurename == 'Median':
        indDict[axis] = features.Median(data[axis])
    if featurename == 'Standard_deviation':
        indDict[axis] = features.Standard_deviation(data[axis])
    if featurename == 'Varience':
        indDict[axis] = features.Varience(data[axis])
    if featurename == 'Root_mean_square':
        indDict[axis] = features.Root_mean_square(data[axis])
    if featurename == 'Sum_Of_Squares':
        indDict[axis] = features.Sum_Of_Squares(data[axis])
    if featurename == 'Covariance':
        if axis =='1':
            indDict[axis] = features.Covariance(data['orX'],data['orY'],data['orZ'])
        elif axis =='2':
            indDict[axis] = features.Covariance(data['rX'],data['rY'],data['rZ'])
        elif axis =='3':
            indDict[axis] = features.Covariance(data['accX'],data['accY'],data['accZ'])
        elif axis =='4':
            indDict[axis] = features.Covariance(data['gX'],data['gY'],data['gZ'])
        elif axis =='5':
            indDict[axis] = features.Covariance(data['mX'],data['mY'],data['mZ'])
    if featurename == 'Zero_Crossing':
        indDict[axis] = features.Zero_Crossing(data[axis])
    return indDict



#calling the
def activity_features(data):
    row1Dict = {}
    # for axis in full_cov_list:
    #     set1, set2 = axis.split('-')
    #     if set1 == 'orX' or set1 == 'orY' or set1 == 'orZ':
    #         covariOrien= features.Covariance(data[set1], data[set1])
    #     if set1 == 'rX' or set1 == 'rY' or set1 == 'rZ':
    #         covariRote= features.Covariance(data[set1], data[set1])
    #     if set1 == 'accX' or set1 == 'accY' or set1 == 'accZ':
    #         covariAccs= features.Covariance(data[set1], data[set1])
    #     if set1 == 'gX' or set1 == 'gY' or set1 == 'gZ':
    #         covariGyr= features.Covariance(data[set1], data[set1])
    #     if set1 == 'mX' or set1 == 'mY' or set1 == 'mZ':
    #         covariMs= features.Covariance(data[set1], data[set1])

    # setting a new dictionary item for various mathematical functions
    row1Dict[" "] = ['Mean', 'Median', 'Standard_deviation', 'Varience', 'Root_mean_square',
                            'Sum_Of_Squares', 'Covariance', 'Zero_Crossing']
    row1Dict['orX'] = [features.Mean(data['orX']), features.Median(data['orX']),
                       features.Standard_deviation(data['orX']),
                       features.Varience(data['orX']), features.Root_mean_square(data['orX']),
                       features.Sum_Of_Squares(data['orX']),
                       features.Covariance(data['orX'], data['orY'],data['orZ']),
                       features.Zero_Crossing(data['orX'])]

    row1Dict['orY'] = [features.Mean(data['orY']), features.Median(data['orY']),
                       features.Standard_deviation(data['orY']),
                       features.Varience(data['orY']), features.Root_mean_square(data['orY']),
                       features.Sum_Of_Squares(data['orY']),
                       "Refer X axis of Orientation",
                       features.Zero_Crossing(data['orY'])]

    row1Dict['orZ'] = [features.Mean(data['orZ']), features.Median(data['orZ']),
                       features.Standard_deviation(data['orZ']),
                       features.Varience(data['orZ']), features.Root_mean_square(data['orZ']),
                       features.Sum_Of_Squares(data['orZ']),
                       "Refer X axis of Orientation",
                       features.Zero_Crossing(data['orZ'])]

    row1Dict['rX'] = [features.Mean(data['rX']), features.Median(data['rX']),
                      features.Standard_deviation(data['rX']),
                      features.Varience(data['rX']), features.Root_mean_square(data['rX']),
                      features.Sum_Of_Squares(data['rX']),
                      features.Covariance(data['rX'], data['rY'],data['rZ']), features.Zero_Crossing(data['rX'])]

    row1Dict['rY'] = [features.Mean(data['rY']), features.Median(data['rY']),
                      features.Standard_deviation(data['rY']),
                      features.Varience(data['rY']), features.Root_mean_square(data['rY']),
                      features.Sum_Of_Squares(data['rY']),
                      "Refer X axis of rotation", features.Zero_Crossing(data['rY'])]

    row1Dict['rZ'] = [features.Mean(data['rZ']), features.Median(data['rZ']),
                      features.Standard_deviation(data['rZ']),
                      features.Varience(data['rZ']), features.Root_mean_square(data['rZ']),
                      features.Sum_Of_Squares(data['rZ']),
                      "Refer X axis of rotation", features.Zero_Crossing(data['rZ'])]

    row1Dict['accX'] = [features.Mean(data['accX']), features.Median(data['accX']),
                        features.Standard_deviation(data['accX']),
                        features.Varience(data['accX']), features.Root_mean_square(data['accX']),
                        features.Sum_Of_Squares(data['accX']),
                        features.Covariance(data['accX'], data['accY'],data['accZ']),
                        features.Zero_Crossing(data['accX'])]

    row1Dict['accY'] = [features.Mean(data['accY']), features.Median(data['accY']),
                        features.Standard_deviation(data['accY']),
                        features.Varience(data['accY']), features.Root_mean_square(data['accY']),
                        features.Sum_Of_Squares(data['accY']),
                        "Refer X axis of accelerometer",
                        features.Zero_Crossing(data['accY'])]

    row1Dict['accZ'] = [features.Mean(data['accZ']), features.Median(data['accZ']),
                        features.Standard_deviation(data['accZ']),
                        features.Varience(data['accZ']), features.Root_mean_square(data['accZ']),
                        features.Sum_Of_Squares(data['accZ']),
                        "Refer X axis of accelerometer",
                        features.Zero_Crossing(data['accZ'])]

    row1Dict['gX'] = [features.Mean(data['gX']), features.Median(data['gX']),
                      features.Standard_deviation(data['gX']),
                      features.Varience(data['gX']), features.Root_mean_square(data['gX']),
                      features.Sum_Of_Squares(data['gX']),
                      features.Covariance(data['gX'], data['gY'],data['gZ']), features.Zero_Crossing(data['gX'])]

    row1Dict['gY'] = [features.Mean(data['gY']), features.Median(data['gY']),
                      features.Standard_deviation(data['gY']),
                      features.Varience(data['gY']), features.Root_mean_square(data['gY']),
                      features.Sum_Of_Squares(data['gY']),
                      "Refer X axis of gyroscope", features.Zero_Crossing(data['gY'])]

    row1Dict['gZ'] = [features.Mean(data['gZ']), features.Median(data['gZ']),
                      features.Standard_deviation(data['gZ']),
                      features.Varience(data['gZ']), features.Root_mean_square(data['gZ']),
                      features.Sum_Of_Squares(data['gZ']),
                      "Refer X axis of gyroscope", features.Zero_Crossing(data['gZ'])]

    row1Dict['mX'] = [features.Mean(data['mX']), features.Median(data['mX']),
                      features.Standard_deviation(data['mX']),
                      features.Varience(data['mX']), features.Root_mean_square(data['mX']),
                      features.Sum_Of_Squares(data['mX']),
                      features.Covariance(data['mX'], data['mY'],data['mZ']), features.Zero_Crossing(data['mX'])]

    row1Dict['mY'] = [features.Mean(data['mY']), features.Median(data['mY']),
                      features.Standard_deviation(data['mY']),
                      features.Varience(data['mY']), features.Root_mean_square(data['mY']),
                      features.Sum_Of_Squares(data['mY']),
                      "Refer X axis of magnetic sensors", features.Zero_Crossing(data['mY'])]

    row1Dict['mZ'] = [features.Mean(data['mZ']), features.Median(data['mZ']),
                      features.Standard_deviation(data['mZ']),
                      features.Varience(data['mZ']), features.Root_mean_square(data['mZ']),
                      features.Sum_Of_Squares(data['mZ']),
                      "Refer X axis of magnetic sensors", features.Zero_Crossing(data['mZ'])]

    return row1Dict


