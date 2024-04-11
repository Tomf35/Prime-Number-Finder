def prime_finder(n):
  prime_list = []
  for num in range(2, n+1):
    for x in range(2, num):
      if num % x == 0:
        break
    else:
        prime_list.append(num)
  return(prime_list)       

 
print(prime_finder(120))
