def adding(numA:str, numB:str)->str:
    try:
        return str(int(numA)+int(numB))
    except ValueError:
        return 'Invalid Operation'
def main():
    print(adding('5','3244'))
if __name__ == '__main__':
    main() 