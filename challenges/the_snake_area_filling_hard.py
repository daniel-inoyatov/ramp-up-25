def snakefill(n:int)->int:
    area = n**2
    count =0
    snake =1
    while snake <area:
        snake*=2
        count+=1
    return count if snake==area else count-1
def main():
    print(snakefill(2))
if __name__ == '__main__':
    main() 