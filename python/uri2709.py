
if __name__ == '__main__':

 while True:

  try:
      entrada = int(input())
      numbers = []
      number = 0
      checkPrime = 0
      for i in range(0,entrada+1):
          numbers.append(int(input()))

      for i in range(len(numbers)-2,-1,-numbers[len(numbers)-1]):
          number+=numbers[i]

      for j in range(2,number):
         if number%j==0:
           checkPrime+=1
         if checkPrime == 1:
              break

      if checkPrime == 0 and number != 1:
          print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
      elif checkPrime!= 0 or number == 1:
          print('Bad boy! I’ll hit you.')


  except EOFError:
     break

