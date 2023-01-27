import numpy as np

def calculate(data:list) -> dict:

    if len(data) < 9:
        raise ValueError('List < 9')
    else:
        data_arr = np.array(data).reshape((3,3))
        
        result = {
            'mean': [list(np.mean(data_arr, axis=0)),[data_arr[0].mean(),data_arr[1].mean(),data_arr[2].mean()], data_arr.mean()],
            'variance': [list(np.var(data_arr, axis=0)),[data_arr[0].var(),data_arr[1].var(),data_arr[2].var()], data_arr.var()],
            'standart deviation': [list(np.std(data_arr, axis=0)),[data_arr[0].std(),data_arr[1].std(),data_arr[2].std()], data_arr.std()],
            'max': [list(np.amax(data_arr, axis=0)),[data_arr[0].max(),data_arr[1].max(),data_arr[2].max()], data_arr.max()],
            'min': [list(np.amin(data_arr, axis=0)),[data_arr[0].min(),data_arr[1].min(),data_arr[2].min()], data_arr.min()],
            'sum': [list(sum(data_arr)), [sum(data_arr[0]),sum(data_arr[1]),sum(data_arr[2])],sum(data)],
            }

    return result

print(calculate([0,1,2,3,4,5,6,7,8]))