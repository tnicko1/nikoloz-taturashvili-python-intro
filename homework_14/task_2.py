def midpoint(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2

def main():
    # test cases for midpoint function
    print(midpoint(1, 4, 2, 8))
    print(midpoint(2, 3, 4, 6))
    print(midpoint(3, 2, 6, 4))
    print(midpoint(4, 1, 8, 2))

if __name__ == '__main__':
    main()