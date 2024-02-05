import feature_module
import load_dataset_module
import traceback
def main():
    try:
        print("====================================================")
        print("   Welcome to Activity context recognition system   ")
        print("====================================================")

        print("Please enter a name for you output file: ")
        file_name = raw_input()
        print("Please enter the path with file name of your input file: ")
        file_path = raw_input()

        print("Do you wish to calculate all features for all axis? (enter 'Y' if yes /enter 'N' if no): ")
        calculate_All = raw_input()
        full_fea_list={}
        full_cov_list=[]
        activity_data_OBJ = load_dataset_module.activity_data(file_path)
        if calculate_All == 'Y' or calculate_All == 'y':
            if activity_data_OBJ != 0:
                # ======================================
                # print("Please enter two axis for calculate Covariance in orientation. eg:orX-orY")
                # orienAxis = raw_input()
                # full_cov_list.append(orienAxis)
                # print("Please enter two axis for calculate Covariance in rotation. eg:rX-rY")
                # roteAxis = raw_input()
                # full_cov_list.append(roteAxis)
                # print("Please enter two axis for calculate Covariance in accelerometer. eg:accX-accY")
                # accelAxis = raw_input()
                # full_cov_list.append(accelAxis)
                # print("Please enter two axis for calculate Covariance in gyroscope. eg:gX-gY")
                # gyroAxis = raw_input()
                # full_cov_list.append(gyroAxis)
                # print("Please enter two axis for calculate Covariance in magnetic sensors. eg:mX-mY")
                # msAxis = raw_input()
                # full_cov_list.append(msAxis)
                # ======================================

                feature_module_OBJ = load_dataset_module.activity_features(activity_data_OBJ)
                feature_module.WriteCSV(feature_module_OBJ, file_name)
                #list_of_str = ['Feature', 'Mean', 'Median', 'Standard_deviation', 'Varience', 'Root_mean_square','Sum_Of_Squares', 'Covariance', 'Zero_Crossing']
                #feature_module.add_column_in_csv("fileToDelete.csv", file_name + ".csv",lambda row, line_num: row.append(list_of_str[line_num - 1]))
                #os.remove("fileToDelete.csv")
                print("Your result calculations can be found in your current working directory.")
            else:
                print("The file is not exist in the given path!")

        elif calculate_All == 'N' or calculate_All == 'n':
            if activity_data_OBJ != 0:
                print("Please select the features You need. Enter the numbers as relevent. eg: 12578 :")
                print("Please enter,")
                print("1 to calculate Mean, 2 to calculate Median, 3 to calculate Standard Deviation, 4 to calculate Varience,")
                print("5 to calculate Root Mean Square, 6 to calculate Sum Of Squares, 7 to calculate Covariance, "
                      "8 to calculate Zero Crossing")

                feature_list_input=raw_input()
                feature_list = list(feature_list_input)
                individual_fea_list={}
                for feature in feature_list:
                    if feature == '1' :
                        print("Which axis would you like to calculate Mean? Use ',' to separate axis. eg: orX,mZ,rY " )
                        axis_mean_input =raw_input()
                        axis_list = axis_mean_input.split(",")
                        axis_mean_list = list(axis_list)
                        activity_data_OBJ = load_dataset_module.activity_data(file_path)
                        meanDict=[]
                        for axis in axis_mean_list:
                            mean_result = load_dataset_module.activity_features_individual(activity_data_OBJ,"Mean",axis)
                            meanDict.append(mean_result)
                        individual_fea_list["Mean"]=meanDict
                    elif feature == '2' :
                        print("Which axis would you like to calculate Median? Use ',' to separate axis. eg: orX,mZ,rY ")
                        axis_mean_input = raw_input()
                        axis_list = axis_mean_input.split(",")
                        axis_mean_list = list(axis_list)
                        activity_data_OBJ = load_dataset_module.activity_data(file_path)
                        medianDict = []
                        for axis in axis_mean_list:
                            mean_result = load_dataset_module.activity_features_individual(activity_data_OBJ,"Median", axis)
                            medianDict.append(mean_result)
                        individual_fea_list["Median"]=medianDict
                    elif feature == '3' :
                        print("Which axis would you like to calculate Standard deviation? Use ',' to separate axis. eg: orX,mZ,rY ")
                        axis_mean_input = raw_input()
                        axis_list = axis_mean_input.split(",")
                        axis_mean_list = list(axis_list)
                        activity_data_OBJ = load_dataset_module.activity_data(file_path)
                        stanDevDict = []
                        for axis in axis_mean_list:
                            mean_result = load_dataset_module.activity_features_individual(activity_data_OBJ,"Standard_deviation",axis)
                            stanDevDict.append(mean_result)
                        individual_fea_list["Standard Deviation"]=stanDevDict
                    elif feature == '4' :
                        print("Which axis would you like to calculate Varience? Use ',' to separate axis. eg: orX,mZ,rY ")
                        axis_mean_input = raw_input()
                        axis_list = axis_mean_input.split(",")
                        axis_mean_list = list(axis_list)
                        activity_data_OBJ = load_dataset_module.activity_data(file_path)
                        varienceDict = []
                        for axis in axis_mean_list:
                            mean_result = load_dataset_module.activity_features_individual(activity_data_OBJ,"Varience", axis)
                            varienceDict.append(mean_result)
                        individual_fea_list["Varience"]=varienceDict
                    elif feature == '5' :
                        print("Which axis would you like to calculate Root Mean Square? Use ',' to separate axis. eg: orX,mZ,rY ")
                        axis_mean_input = raw_input()
                        axis_list = axis_mean_input.split(",")
                        axis_mean_list = list(axis_list)
                        activity_data_OBJ = load_dataset_module.activity_data(file_path)
                        rooMeSqDict = []
                        for axis in axis_mean_list:
                            mean_result = load_dataset_module.activity_features_individual(activity_data_OBJ,"Root_mean_square",axis)
                            rooMeSqDict.append(mean_result)
                        individual_fea_list["Root Mean Square"]=rooMeSqDict
                    elif feature == '6' :
                        print("Which axis would you like to calculate Sum of Square? Use ',' to separate axis. eg: orX,mZ,rY ")
                        axis_mean_input = raw_input()
                        axis_list = axis_mean_input.split(",")
                        axis_mean_list = list(axis_list)
                        activity_data_OBJ = load_dataset_module.activity_data(file_path)
                        sumOfSqDict = []
                        for axis in axis_mean_list:
                            mean_result = load_dataset_module.activity_features_individual(activity_data_OBJ,"Sum_Of_Squares", axis)
                            sumOfSqDict.append(mean_result)
                        individual_fea_list["Sum of Square"]=sumOfSqDict
                    elif feature == '7' :
                        print("Which sensor would you like to calculate Covariance? Use ',' to separate the sensor. eg: 1,5,3 ")
                        print("Please enter,")
                        print("1 for Orientation, 2 for Rotation, 3 for Accelerometer, 4 for gyroscope, 5 for magnetic sensors")
                        axis_mean_input = raw_input()
                        axis_list = axis_mean_input.split(",")
                        axis_mean_list = list(axis_list)
                        activity_data_OBJ = load_dataset_module.activity_data(file_path)
                        covariDict = []
                        for axis in axis_mean_list:
                            mean_result = load_dataset_module.activity_features_individual(activity_data_OBJ,"Covariance", axis)
                            covariDict.append(mean_result)
                        individual_fea_list["Covariance"] = covariDict
                    elif feature == '8' :
                        print("Which axis would you like to calculate Zero Crossing? Use ',' to separate axis. eg: orX,mZ,rY ")
                        axis_mean_input = raw_input()
                        axis_list = axis_mean_input.split(",")
                        axis_mean_list = list(axis_list)
                        activity_data_OBJ = load_dataset_module.activity_data(file_path)
                        zerCrDict = []
                        for axis in axis_mean_list:
                            mean_result = load_dataset_module.activity_features_individual(activity_data_OBJ,"Zero_Crossing", axis)
                            zerCrDict.append(mean_result)
                        individual_fea_list["Zero Crossing"]=zerCrDict
                    else:
                        print("Please enter a valid input!")

                feature_module.WriteCSV(individual_fea_list, file_name)
            else:
                print("The file is not exist in the given path!")

        else:
            print("Please enter a valid input!")
    except:
        traceback.print_exc()

        print("=====================================================")
        print("Ohhhhh! Something went wrong! Please try again later!")
        print("=====================================================")
    finally:
        print("=========================================================================")
        print("Thank you for using Activity context recognition system. Have a good day!")
        print("=========================================================================")

main()
