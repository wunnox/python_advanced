
class Sieve:
    def __init__(self, max_n):
        self.MaxN = max_n
        self.Primes = []

    def __iter__(self):
        self.N = 1
        self.Prime = 2
        return self

    def __next__(self):
        if self.N == 1:
            self.Primes.append(2)
            self.N = 2
            return self.Prime
        elif self.N <= self.MaxN:
            self.Prime += 1
            primesearch=1
            while primesearch:
                isprime=True
                for divisor in self.Primes:
                    if self.Prime % divisor == 0:
                        isprime=False
                        break
                if isprime:
                    self.Primes.append(self.Prime)
                    self.N += 1
                    return self.Prime

                else:
                    self.Prime += 1
        else:
            raise StopIteration

if __name__ == "__main__":
    for f in Sieve(25):
        print(f, end=" ")
    print()

    print(list(Sieve(16)))
    print(sum(Sieve(100)))
