def prime_checker(number):
    in_prime = True
    for i in range(2, number):
        if number % i == 0:
            in_prime = False
    if in_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number")


n = int(input())  # Check this number
prime_checker(number=n)