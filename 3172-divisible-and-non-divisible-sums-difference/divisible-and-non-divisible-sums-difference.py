class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # num1=[]
        # num2=[]
        # for i in range(1,n+1):
        #     if i % m !=0:
        #         num1.append(i)
        #     if i %m == 0:
        #         num2.append(i)
        # nums= sum(num1) - sum(num2)
        # return nums

        num1=0
        num2=0

        for i in range(1,n+1):
            if i %m != 0:
                num1=num1+i
        for i in range(1,n+1):
            if i% m == 0:
                num2= num2+i
        nums= num1-num2
        return nums
        

