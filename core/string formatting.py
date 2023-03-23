def print_formatted(number):
    # Find length of longest binary number
    length = len(bin(number)) - 1

    # Print values
    for i in range(1, number + 1):
        print(str(i).rjust(length - 1), end="")
        print(str(oct(i))[2:].rjust(length), end="")
        print(str(hex(i))[2:].rjust(length).upper(), end="")
        print(str(bin(i))[2:].rjust(length), end="")
        print("")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)