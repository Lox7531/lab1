import numpy as np
H=np.array([[1,100,3,4,5,6,0 ],
   [8,9,101,11,12,13,0 ],
   [14,15,16,102,18,19,0 ],
   [20,21,22,23,103,25, 0],
   [26,27,28,29,30,104, 0]
   ])
print(H)
maxi=[max(H[0]),max(H[1]),max(H[2]),max(H[3]),max(H[4])]
for i in range(len(H)):
   H[i][6]=H[i][5]
   H[i][5]=maxi[i]
print(H)