def reurgcd(a,b):
    low=min(a,b)
    high=max(a,b)
    if low==0:
        return high
    elif low==1:
        return 1
    else:
        return reurgcd(low,high%low)
print(reurgcd(12,14))
