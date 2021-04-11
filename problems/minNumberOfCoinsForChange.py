def minNumberOfCoinsForChange(n, denoms, cache = {}):
  # print(f'called at n={n}')
  if n in cache:
    return cache[n]

  if n == 0:
    return 0

  if n < 0:
    return -1

  minCoinsUsed = -1
  for c in denoms:
    result = minNumberOfCoinsForChange(n-c, denoms, cache)
    if result == -1:
      continue
    
    if minCoinsUsed == -1:
      minCoinsUsed = result + 1
      continue

    minCoinsUsed = min(minCoinsUsed, result + 1)
  
  # print(f'n={n}, result={minCoinsUsed}')
  cache[n] = minCoinsUsed
  return minCoinsUsed

print(minNumberOfCoinsForChange(3, [2, 1]))