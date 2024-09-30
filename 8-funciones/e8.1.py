import typing

def is_prime(n):
    i = 2
    while i < n:
      if n % i == 0:
        return False
      i += 1
    return True

def main():
  print(is_prime(2)) # True
  print(is_prime(6)) # False

main()