class Solution(object):
    # USING A REVERSED LIST
    # def plusOne(self, digits):
    #     digits = digits[::-1]
    #     one, i = 1, 0

    #     while one:
    #         if i < len(digits):
    #             if digits[i] == 9:
    #                 digits[i] == 0
    #             else:
    #                 digits[i] += 1
    #                 one = 0
            
    #         else:
    #             digits.append(1)
    #             one = 0
    #         i += 1

    #     return digits[::-1]


    def plusone(self, digits):
         n = len(digits)

         for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

         return [1] + digits
            
                   
              

    


                       
        