import os
import math
def convertToCelsius(tempInFarenheit):
    inCelsius = (tempInFarenheit - 32) * (5/9)
    print(inCelsius)
    return round(inCelsius,2)

assert convertToCelsius(0) == -17.78

def convertToFarenheit(tempInCelsius):
    inFarenheit = (tempInCelsius * 9/5) + 32
    print(inFarenheit)
    return round(inFarenheit, 2)

assert convertToFarenheit(0) == 32