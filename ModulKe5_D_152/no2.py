""" NAMA = CORRY LUQMA ZUNIRA
    KELAS = D
    NIM = L200170152 """


A = ["AYASHA", "BONDAN" , "CORRY" , "DIKA" , "EKA"]
B = ["A01" , "B02 " , "C03" , "D04" , "E05"]
C =[]
C.extend(A)
C.extend(B)

def insertionSort(A) :
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1] :
            A[pos] = A[pos-1]
            pos = pos - 1
        A[pos] =  nilai
insertionSort(C)
print("Nilai C yang telah urut adalah : ","\n",C,"\n")
