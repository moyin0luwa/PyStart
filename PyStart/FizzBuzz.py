def fizzbuzz_solution(num):
    for n in range(num):
        word = ""
        word += "Fizz" if (n % 3) == 0 else ''
        word += "Buzz" if (n % 5) == 0 else ''
        print(word or n)


fizzbuzz_solution(100)
