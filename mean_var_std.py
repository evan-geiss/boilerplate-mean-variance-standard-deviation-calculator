import numpy as np

def calculate(list):
    # convert list into numpy 3 x 3 array
    arr = np.array(list).reshape(3,3)

    # Calc mean and store in format: 'mean': [axis1, axis2, flattened]
    calculations = {
        'mean': [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), arr.mean().tolist()]
    }
    
    # calc variance and store in format: 'variance': [axis1, axis2, flattened]
    calculations['variance'] = [arr.var(axis=0).tolist(), arr.var(axis=1).tolist(), arr.var().tolist()]

    # calc standard deviation and store in format: 'standard deviation': [axis1, axis2, flattened]
    calculations['standard deviation'] = [arr.std(axis=0).tolist(), arr.std(axis=1).tolist(), arr.std().tolist()]

    # Max and store in format: 'max': [axis1, axis2, flattened]
    calculations['max'] = [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), arr.max().tolist()]

    # Min
    calculations['min'] = [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), arr.min().tolist()]

    # Sum
    calculations['sum'] = [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), arr.sum().tolist()]


    return calculations