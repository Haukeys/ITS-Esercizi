def sumInRange(a:int, b:int):
        result:int = 0
        for i in range(a, b+1):
            result = result + i
        return result
   # Now, we can just use it:

mysum = sumInRange(1, 10)
print(f"Sum from 1 to 10 is {sumInRange(1, 10)}")

mysum = sumInRange(20, 37)
print(f"Sum from 20 to 37 is {sumInRange(20, 37)}")

mysum = sumInRange(35, 49)
print(f"Sum from 35 to 49 is {sumInRange(35, 49)}")