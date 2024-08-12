


def palindrome(x):
   n = len(x)
   y = 0
   for i in range(n-1, -1, -1):
        if x[i] == x[y]:
            y += 1

        else: 
            return False
   if y == n:
       return True

x = '3223'

print(palindrome(x))