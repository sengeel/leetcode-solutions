def isSubquence(s, t):
    S = len(s)
    T = len(t)

    if s == '':
        return True
    
    if S > T :
        return False
    

    j = 0
    for i in range (T):
        if s[j] == t[i]:
            if j == S - 1:
                return True
            
            else:
                j += 1

    return False


