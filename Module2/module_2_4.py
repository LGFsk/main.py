numbers = [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = bool
for i in range(len(numbers)):
    for j in range(2, 4):
        if (numbers[i] == 1):
            is_prime = True
            break
        elif numbers[i] == 2 or numbers[i] == 3:
            is_prime = True
            break
        elif ((numbers[i] % j) == 0):
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime == True:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])

for h in range(primes.count(1)):
    primes.remove((1))
print("Primes:", primes)
print("Not Primes:", not_primes)