# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import matplotlib.pyplot as plt
import numpy as np
import csv

def readFile(fileName):

    data = np.genfromtxt(fileName, delimiter=',', skip_header = 1)
    xVals=[]
    yVals=[]
    data = np.array(data)
    for pair in data:
        if (pair[0]!='year'):
            xVals.append(pair[0])
            yVals.append(pair[1])
    plotfig(xVals,yVals)
    ques3(xVals,yVals)


def plotfig(x,y):
    plt.plot(x, y)

    # Set chart title.
    plt.title("Number of frozen days form 1855-2021")

    # Set x, y label text.
    plt.xlabel("Year")
    plt.ylabel("Number of Frozen Days")
    plt.savefig("plot.jpg")
    plt.show()

def ques3(xVals,yVals):
    X = []
    xModif=np.array(xVals, int)
    for x in xModif:
        X.append([1,x])
    print("Q3a:")
    print(np.array(X,int))
    Y=np.array(yVals, int)
    print("Q3b:")
    print(Y)
    Z=np.dot(np.transpose(X), X)
    print("Q3c:")
    print(Z)
    I=np.linalg.inv(Z)
    print("Q3d:")
    print(I)
    PI=np.dot(I, np.transpose(X))
    print("Q3e:")
    print(PI)
    hat_beta=np.dot(I, np.dot(np.transpose(X),Y))
    print("Q3f:")
    print(hat_beta)
    y_test=hat_beta[0]+(hat_beta[1]*2021)
    print("Q4: " + str(y_test))
    symbol=""
    shortAnswer=""
    if(hat_beta[1]<0):
        symbol="<"
        shortAnswer="Hat beta (1) is less than zero. This indicates that Mendota will freeze less often (less freeze days)."
    elif(hat_beta[1]>0):
        symbol=">"
        shortAnswer = "Hat beta (1) is greater than zero. This indicates that Mendota will freeze more often (more freeze days)."
    else:
        symbol="="
        shortAnswer = "Hat beta (1) is equal to  zero. This indicates that Mendota will freeze as often (same number of freeze days)."
    print("Q5a: "+symbol)
    print("Q5b: "+shortAnswer)
    prediction=(0-hat_beta[0])/hat_beta[1]
    explanation="X* is a compelling prediction based on the trends. X* indicates the year that Mendota will have zero freeze days. \n If a line of best fit is visualized on the graph, following the linear trends, \n the line would intersect with the x-axis at about x=2040, which is on par with the X* value of 2455.5838."
    print("Q6a: "+ str(prediction))
    print("Q6b: " + explanation)
fName=sys.argv[1]  #this contains the first argument as string
#fName='hw5.csv'
readFile(fName)



