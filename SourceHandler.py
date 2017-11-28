import os
from scipy import misc
import numpy as np

#this method gets source folder as input and makes a filw for each image in it to train from.
def sortFiles(path):
    list_of_files = {}
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
                list_of_files[filename] = os.sep.join([dirpath, filename])
    print (list_of_files)
    for file in list_of_files:
        arr = misc.imread(file, True)
        np.savetxt(filename, arr)










arr = misc.imread('lena.png') # 640x480x3 array
arr[20, 30] # 3-vector for a pixel
arr[20, 30, 1] # green value for a pixel