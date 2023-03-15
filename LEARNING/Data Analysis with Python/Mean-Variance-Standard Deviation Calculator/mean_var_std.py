import numpy as np

def calculate(lis):
    if len(lis) != 9 : 
        raise ValueError ( "List must contain nine numbers.") 
        return 
    else : 
        lis = np.array(lis, dtype=float).reshape(3,3)
        ans = {
            'mean' :                [lis.mean(axis=0).tolist(), lis.mean(axis=1).tolist(), lis.mean()],
            'variance':             [lis.var(axis=0).tolist(),  lis.var(axis=1).tolist(),  lis.var()],    
            'standard deviation' :  [lis.std(axis=0).tolist(),  lis.std(axis=1).tolist(),  lis.std()],   
            'max' :                 [lis.max(axis=0).tolist(),  lis.max(axis=1).tolist(),  lis.max()],
            'min' :                 [lis.min(axis=0).tolist(),  lis.min(axis=1).tolist(),  lis.min()],
            'sum' :                 [lis.sum(axis=0).tolist(),  lis.sum(axis=1).tolist(),  lis.sum()]
        } 
       
    return ans

#print(calculate([2,6,2,8,4,0,1,5,7]))