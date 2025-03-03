def fib():
    terms = int(input("Enter the number of terms: "))
    fib_sequence = [0, 1]
    for i in range(2, terms):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    print(fib_sequence[:terms])