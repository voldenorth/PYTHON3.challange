import numpy as np 


a=[0,1,2,3,4,5,6,7,8]

def calculate(list):
    if len(list)==9:
        x=np.array(list).reshape(3,3)
        calculation={
            'mean':[np.mean(x,0),np.mean(x,1),np.mean(x)],
            'variance':[np.var(x,0),np.var(x,1),np.var(x)],
            'standar deviation':[np.std(x,0),np.std(x,1),np.std(x)],
            'max':[np.max(x,0),np.max(x,1),np.max(x)],
            'min':[np.min(x,0),np.min(x,1),np.min(x)],
            'sum':[np.sum(x,0),np.sum(x,1),np.sum(x)]
            }
        
    else:
        calculation='valueerror'
    
    return calculation

b=calculate(a)
print(b)