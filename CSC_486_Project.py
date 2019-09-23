#TODO import file
#TODO have it take data from the csv file
#TODO Find Linear regression
#TODO Find Multiple Regression
#TODO Make a csv file in excel
#TODO Import CSV file
#Author: Bryan Epperson

import matplotlib.pyplot as plt



def read_csv(filename):
    """ This function takes a csv file and reads off the data type of the file
        This will take the x and y cordinate of the graph and read them off into their respective list
        Each x vaule should match with each of its respect y-value.

        x list = [x1,x2,x3,xi]
        y list = [y1,y2,y3,yi]

        """
    f = open(filename,'r')
    data = [i[:-1].split(',') for i in f.readlines()]
    f.close()
    return data
def intercept(x_cordinate, y_cordinate, b1):
    y_avg = sum(y_cordinate)/len(y_cordinate)
    x_avg = sum(x_cordinate)/len(x_cordinate)
    # return y_sum
    # print(y_sum)
    y_intercept = (y_avg - (b1 * x_avg))
    return float(y_intercept)
    # return float(y_intercept)

def line_forumula(b0, b1, x_cordinate):
    y_value = b0 + b1 * x_cordinate
    return y_value



def slope(x_cordinate, y_cordinate):
    x_result = []
    y_result = []
    x_mean = (sum(x_cordinate) / len(x_cordinate))
    y_mean = (sum(y_cordinate) / len(y_cordinate))
    numerator = 0
    denominator = 0
    multXY = []
    for i in range(0, len(x_cordinate)):
        x_result = (x_cordinate[i] - x_mean)
        y_result = (y_cordinate[i] - y_mean)
        numerator += (x_result * y_result)
        denominator += (x_result * x_result)


    slope = numerator / denominator
    return slope
    # print(multXY)

# def line_formula():
#     equation_of_line = intercept(x_cordinate,y_cordinate, result_slope) + slope(x_cordinate, y_cordinate)
#     return float(equation_of_line





def main():
    filename = 'Agg_data.csv'
    data = read_csv(filename)
    x_cordinate = [1,2,3,4,5]
    y_cordinate = [1.1,1.9,3.4,4.6,4.9]
    #x_cordinate = [float(i[8]) for i in data[1:]]
    #y_cordinate = [float(i[9]) for i in data[1:]]
    # print(x_cordinate, y_cordinate)
    # print_intercept = intercept(x_cordinate,y_cordinate)
    result_slope = slope(x_cordinate, y_cordinate)
    result_intercept = intercept(x_cordinate,y_cordinate,result_slope)
    print(result_intercept)
    print(result_slope)
    plt.scatter(x_cordinate,y_cordinate)
    plt.plot( [x_cordinate[0], x_cordinate[-1]], [line_forumula(result_intercept, result_slope, x_cordinate[0]),
                                                  line_forumula(result_intercept, result_slope, x_cordinate[-1])] )
    plt.show()
    # print(result_slope)
    # # print(x_cordinate)
    # print(y_cordinate)





main()



