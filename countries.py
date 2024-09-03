import os
import math

countries = ['INDIA', 'USA', 'UNITED KINGDOM']
for country in countries:
    print(country)

countries.append('USA')
print(countries)


squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
    print(squares)

sliced = squares[:]
print(sliced)
