import numpy as np

def tallest_skyscraper(skyline: list):
    numPy = np.array(skyline).T
    skyline = numPy.tolist()
    max = 0
    for row in skyline:
        max  = max if max > sum(row) else sum(row)
    return max


def main():
    skyline = [
                [0, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 1, 0],
                [1, 1, 1, 1]
                ]
    print(tallest_skyscraper(skyline))
if __name__ == '__main__':
    main() 