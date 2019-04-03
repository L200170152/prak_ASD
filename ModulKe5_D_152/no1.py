""" NAMA = CORRY LUQMA ZUNIRA
    KELAS = D
    NIM = L200170152 """


class MhsTIF(object):
    def __init__(self, nim):
        self.nim = nim

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        MhsTIF = i
        while MhsTIF > 0 and nilai < A[MhsTIF - 1]:
            A[MhsTIF] = A[MhsTIF-1]
            MhsTIF = MhsTIF-1
        A[MhsTIF] = nilai

   
c0 = 200170001
c1 = 200170003
c2 = 200170007
c3 = 200170005
c4 = 200170002
c5 = 200170006

Daftar = [c0, c1, c2, c3, c4, c5]
insertionSort(Daftar)
print("Berikut adalah NIM Mahasiswa secara urut :","\n",Daftar, "\n")
