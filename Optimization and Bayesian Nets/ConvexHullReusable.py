c = [-1, -2, 0, 0, 0]
A = [[1, 1, 1, 0, 0],[-2, 1, 0, 1, 0],[2, 1, 0, 0, 1]]
b = np.array([4, 2, 6])

s = {1,2,3,4,5}
combtn = itertools.combinations(s,3)

active = [list(x) for x in combtn]
def build(comb):
    
    B = [[],[],[]]
    for i in range(3):
        
        ind = comb[i]-1
        for j in range(3):
            
            B[j].append(A[j][ind])
        
    return np.array(B)

count = 1
for x in active:
    
    B = build(x)
    B_inv = np.linalg.inv(B)
    bs = B_inv@b
    cost = [(c[i-1]) for i in x]
    
    print("\n\nBasic Solution ",count,": ","Variables: ",x)
    print("\nBasic Matrix:")
    print("\t",B)
    print("\n\nBasic Solution: ")
    print("\t",bs)
    print("\nActive Cost Matrix:")
    print("\t",cost)
    print("\nRemaining variables and costs (inactive) assigned to 0")
    
    count += 1
    
