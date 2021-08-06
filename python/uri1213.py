if __name__ == '__main__':
 while True:
  try:
    n = input()
    x = 1
    c = 1
    while x % int(n) != 0:
        x = (10 * x + 1) % int(n)
        c += 1
    print(c)
  except EOFError:
      break