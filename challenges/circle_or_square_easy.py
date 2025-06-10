import math

def circle_or_square(rad:int, area:int):
    return (2*rad*round(math.pi,2))> (math.sqrt(area) * 4)

def main():
    print(circle_or_square(5,100))
if __name__ == '__main__':
    main() 