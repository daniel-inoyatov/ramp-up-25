def sum_odd_and_even(nums:list)-> list:
    output = [0,0]
    for n in nums:
        if n%2==0:
            output[0]+=n
        else:
            output[1]+=n
    return output
def main():
    print(sum_odd_and_even([1,2,3,4,5,6]))
if __name__ == '__main__':
    main() 