def find_prime_numbers(n):
    sum_ = 0
    for i in range(2, n + 1):
        counter = 0
        for j in range(1, i + 1):
            if i % j == 0:
                counter += 1
        if counter == 2:
            sum_ += i

    print("The total is {}".format(sum_))


def main():
    while True:
        try:
            n = int(input("Enter a natural number: "))
            find_prime_numbers(n)
            break
        except ValueError:
            print("It was not a natural number! ")
            continue


main()
