import numpy as np 

n, m = list(map(int, input().split()))
string_eye = str(np.eye(n,m))
print(string_eye.replace("0"," 0").replace("1"," 1"))
