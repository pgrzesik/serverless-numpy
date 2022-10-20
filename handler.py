import numpy as np


def hello(event, context):
    print(np.__version__)

    sample_array = np.array([[1. ,2. ,3.], [4. ,5. ,6.]])
    print(sample_array)
