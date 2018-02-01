"""asdfsadf"""
def compute26():
    """test"""
    numArray = range(1, 13)
    aset = set({})
    atuple = tuple()
    alist = []
    asum = 26
    for i in numArray:
        for j in numArray:
            for k in numArray:
                for l in numArray:
                    if (i!=j)&(i!=k)&(i!=l)&(j!=k)&(j!=l)&(k!=l)&(i+j+k+l==asum):
                        alist = [i,j,k,l]
                        atuple = tuple(sorted(alist))
                        aset.add(atuple)
    return sorted(aset)

if __name__ == '__main__':
    print compute26()