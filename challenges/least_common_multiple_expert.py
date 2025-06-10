import math
from functools import reduce
def lcmTwoNum(a:int, b:int):
    return (a*b)//math.gcd(a,b)
def lcm(nums:list):
    return reduce(lcmTwoNum, nums)
def main():
    print(lcm([1, 2, 3, 4, 5, 6, 7, 8, 9]))
main()
    