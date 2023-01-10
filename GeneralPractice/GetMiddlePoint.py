#Getting middle point...

def getMiddlePoint(cordA, cordB):
    xA = cordA[0]
    yA = cordA[1]
    xB = cordB[0]
    yB = cordB[1]

    xM = (xA + xB)/2
    yM = (yA + yB)/2

    M = (xM, yM)

    return M


from tkinter import Y
import matplotlib as mp
from matplotlib import pyplot

def function(x):
    y = 4*x + 2
    
    return y



def lineal():

    # x = range(-0, 30)
    # y = range(-10, 20)

    x = [0,1,2,3,4,5,6,7,8,9,10]
    y = [0,1,2,3,4,5,6,7,8,9,10]

    pyplot.plot(x, y)

    pyplot.axhline(0, color="pink")
    pyplot.axvline(0, color="pink")

    pyplot.xlim(-20, 30)
    pyplot.ylim(-20, 30)

    pyplot.show()


def plotLineal(cordA, cordB):
    
    xList = [0,1,2,3,4,5,6,7,8,9,10]
    y = [0,1,2,3,4,5,6,7,8,9,10]






if __name__ == '__main__':
   lineal()