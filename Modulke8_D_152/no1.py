class Stack(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.items)
    def peek(self):
        assert not self.isEmpty();
        return self.items[-1]
    def pop(self):
        assert not self.isEmpty();
        return self.items.pop()
    def push(self,data):
        self.items.append(data)

def cetakHexa(d):
    f = Stack()
    g = "0123456789ABCDEF"
    while d !=0:
        sisa = d%16
        d = d//16
        f.push(g[sisa])
    st =""
    for i in range (len(f)):
        st = st + str(f.pop())
    return st
