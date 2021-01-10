def lists_intersection(biglst1,smalllst2):
    
    """Returns the lenght of intersection of two lists"""

    print(lists_intersection.__doc__)
    #help(list_intersection)  """We can also get the Documentation of the function with the help of this """

    print (len(set(biglst1).intersection(smalllst2))) #Using the function named as intersection1d from numpy.

    
def read_txt_file(filename):

    """Reads the data of the txt file and returs the file by seperating them line by line"""
    print(read_txt_file.__doc__)
    with open(filename) as f:
        return f.read().split('\n')

    
import numpy as np
"""imports numpy as np. Numpy is an python library used for working with arrays 
it also has functions for working in domain of linear algebra,matrices.
This library must be installed from the web,Or by using "pip install numpy" 

"""

import pandas as pd
"""imports pandas as pd. Pandas is an python library used for data manipulation and analysis.
This library must be installed from the web,Or by using "pip install pandas"

"""

import time 
"""imports time module which comes with python by defualt."""


subset_elements=read_txt_file('subset_elemets.txt')
all_elements=read_txt_file('all_elements.txt')

start = time.time()
lists_intersection(all_elements,subset_elements)
print('Duration: {} seconds'.format(time.time() - start))

