def sum(n:int) -> int:
    # n is negative
    if n < 0:
        print("Error! Inserted number is negative!")
        return 0
        # n is positive
    else :
        # define a sum
        sum:int = 0
        # compute sum until n >= 0
        while n:
            sum = sum + n
            n = n-1
            # return sum as int
            return int(sum)
        
print(sum(5))