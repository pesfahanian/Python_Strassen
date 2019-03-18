import numpy as np
import time

_start_time = time.time()

def tic():
    global _start_time 
    _start_time = time.time()

def toc():
    milliseconds = time.time() - _start_time
    print(milliseconds)

def ikj_matrix_product(A, B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def add(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def subtract(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] - B[i][j]
    return C

def strassen(A, B):
      
    LEAF_SIZE = ls
    n = len(A)

    if n <= LEAF_SIZE:
        return ikj_matrix_product(A, B)
    else:
        new_size = n/2
        a11 = [[0 for j in range(0, int(new_size))] for i in range(0, int(new_size))]
        a12 = [[0 for j in range(0, int(new_size))] for i in range(0, int(new_size))]
        a21 = [[0 for j in range(0, int(new_size))] for i in range(0, int(new_size))]
        a22 = [[0 for j in range(0, int(new_size))] for i in range(0, int(new_size))]

        b11 = [[0 for j in range(0, int(new_size))] for i in range(0, int(new_size))]
        b12 = [[0 for j in range(0, int(new_size))] for i in range(0, int(new_size))]
        b21 = [[0 for j in range(0, int(new_size))] for i in range(0, int(new_size))]
        b22 = [[0 for j in range(0, int(new_size))] for i in range(0, int(new_size))]

        aResult = [[0 for j in range(0, int(new_size))] for i in range(0, int(new_size))]
        bResult = [[0 for j in range(0, int(new_size))] for i in range(0, int(new_size))]

        for i in range(0, int(new_size)):
            for j in range(0, int(new_size)):
                a11[i][j] = A[i][j]                                    
                a12[i][j] = A[i][j + int(new_size)]                    
                a21[i][j] = A[i + int(new_size)][j]                    
                a22[i][j] = A[i + int(new_size)][j + int(new_size)]    

                b11[i][j] = B[i][j]                                    
                b12[i][j] = B[i][j + int(new_size)]                   
                b21[i][j] = B[i + int(new_size)][j]                    
                b22[i][j] = B[i + int(new_size)][j + int(new_size)]    

        aResult = add(a11, a22)
        bResult = add(b11, b22)
        p1 = strassen(aResult, bResult)    

        aResult = add(a21, a22)             
        p2 = strassen(aResult, b11)       

        bResult = subtract(b12, b22)       
        p3 = strassen(a11, bResult)  

        bResult = subtract(b21, b11)     
        p4 =strassen(a22, bResult)        

        aResult = add(a11, a12)            
        p5 = strassen(aResult, b22)      

        aResult = subtract(a21, a11)     
        bResult = add(b11, b12)            
        p6 = strassen(aResult, bResult)  

        aResult = subtract(a12, a22)     
        bResult = add(b21, b22)          
        p7 = strassen(aResult, bResult)    

        c12 = add(p3, p5)                  
        c21 = add(p2, p4)                  

        aResult = add(p1, p4)              
        bResult = add(aResult, p7)          
        c11 = subtract(bResult, p5)         

        aResult = add(p1, p3)             
        bResult = add(aResult, p6)          
        c22 = subtract(bResult, p2)         

        C = [[0 for j in range(0, n)] for i in range(0, n)]
        for i in range(0, int(new_size)):
            for j in range(0, int(new_size)):
                C[i][j] = c11[i][j]
                C[i][j + int(new_size)] = c12[i][j]
                C[i + int(new_size)][j] = c21[i][j]
                C[i + int(new_size)][j + int(new_size)] = c22[i][j]
        return C

def main():
      
    size = 1024
          
    A = np.random.randint(0, 10, size=(size, size))
    B = np.random.randint(0, 10, size=(size, size))
        
    tic()
    C = strassen(A, B)
    toc()

    A = [2 , 4 , 8 , 16 , 32 , 64 , 128, 256 , 512 , 1024]
    for ls in A:
      print('ls = %d' %ls)
      main()
      print('')