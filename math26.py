def compute26():
    num_array = range(1, 13)
    aset = set({})
    atuple = tuple()
    alist = []
    asum = 26
    for i in num_array:
        for j in num_array:
            for k in num_array:
                for l in num_array:
                    if (i!=j)&(i!=k)&(i!=l)&(j!=k)&(j!=l)&(k!=l)&(i+j+k+l==asum):
                        alist = [i,j,k,l]
                        atuple = tuple(sorted(alist))
                        aset.add(atuple)
    return sorted(aset)

if __name__ == '__main__':
   print compute26()