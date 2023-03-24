
import numpy
my_array = numpy.array([input().split() for _ in range(int(input().split()[0]))],int)
print(numpy.max(numpy.min(my_array, axis=1), axis=0))