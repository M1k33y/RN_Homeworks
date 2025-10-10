def recognise_input(filename):
    A = []
    B =[]

    with open(filename, 'r') as f:
        for line in f:
            line=line.strip()
            
            left,right=line.split("=")


            B.append((float)(right))
            left=left.replace(" ","")
            left=left.replace("x"," ")
            left=left.replace("y"," ")
            left=left.replace("z"," ")

            
            tokens=left.split()
          
            if(len(tokens)<3):
                tokens=["1"]+tokens

            for i,token in enumerate(tokens):                
                t = token.strip("+*/")
                tokens[i] = t or "1"
                if tokens[i] == "-":
                    tokens[i] = "-1"

            A.append(tokens)
    return A,B

def determinant(A):
    if len(A) == 2:
        return (float)(A[0][0])*(float)(A[1][1]) - (float)(A[0][1])*(float)(A[1][0])

    rez =(float)(A[0][0])*((float)(A[1][1])*(float)(A[2][2])-(float)(A[1][2])*(float)(A[2][1])) - (float)(A[0][1])*((float)(A[1][0])*(float)(A[2][2])-(float)(A[1][2])*(float)(A[2][0])) + (float)(A[0][2])*((float)(A[1][0])*(float)(A[2][1])-(float)(A[1][1])*(float)(A[2][0]))
    return rez

def trace(A):
    rez=(float)(A[0][0])+(float)(A[1][1])+(float)(A[2][2])
    return rez

def norma_euclidiana(B):
    rez=0
    for i in range(len(B)):
        B[i]=(float)(B[i])
        rez+=B[i]**2
    return (float)(rez**0.5)

def transpose(A):
    rez=[]
    for i in range(len(A)):
        linie=[]
        for j in range(len(A)):
            linie.append(A[j][i])
        rez.append(linie)
    return rez

def multiply(A,B):
    rez=[]
    for i in range(len(A)):
        suma=0
        for j in range(len(A)):
            suma+= (float)(A[i][j])*(float)(B[j])
        rez.append(suma)
    return rez

def solve_cramer(A,B):
    detA=determinant(A)
    if(detA==0):
        return "Sistemul nu are solutie unica"
    
    copyA = [row[:] for row in A]
    for i in range(3):
        copyA[i][0] = B[i]
    x = determinant(copyA) / detA

    copyA = [row[:] for row in A]
    for i in range(3):
        copyA[i][1] = B[i]
    y = determinant(copyA) / detA

    copyA = [row[:] for row in A]
    for i in range(3):
        copyA[i][2] = B[i]
    z = determinant(copyA) / detA

    return x,y,z

def adjuncta(A):
    C = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
                C[i][j] = (-1)**(i+j) * determinant(minor(A, i, j))
    return C

def minor(A, i, j):
    return [row[:j] + row[j+1:] for row in (A[:i] + A[i+1:])]

def inversa(A):
    detA = determinant(A)
    if detA == 0:
        return "Matricea nu este inversabila"
    
    adj = adjuncta(A)
    inv = [[(adj[j][i]) / detA for j in range(3)] for i in range(3)]
    return inv

def solvingWithInversa(A,B):
    invA = inversa(A)
    if invA == "Matricea nu este inversabila":
        return "Sistemul nu are solutie unica"
    return multiply(invA,B)

A,B=recognise_input("input.txt")

print("Matricea A:",A)
print("Vectorul B:",B)
print("Determinantul A:\n",determinant(A))
print("Trace A:\n",trace(A))
print("Norma B:\n",norma_euclidiana(B))
print("Transpose A:\n",transpose(A))
print("Multiplicarea A si B:\n",multiply(A,B))
print("Solutia sistemului A*X=B:\n",solve_cramer(A,B))
print("Minor 2,1: ",minor(A,1,0))
print("Inversa A:\n",inversa(A))
print("Solutia sistemului A*X=B:\n",solvingWithInversa(A,B))

###BONUS
#Determinantul este suma dintre elementele de pe primul rand inmultite cu cofactorii lor