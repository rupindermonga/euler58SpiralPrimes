'''
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

'''


def isPrime(n):
    result = True
    if n == 1:
        result = False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            result = False
            break
    return result 

def SideLength(n):
    # n is the %age
    final_percent = 1
    side_length = 5
    no_primes = 5
    while final_percent > n:
        side_length += 2
        for i in range(4):
            number = side_length**2 - (side_length - 1)*i
            no_primes += isPrime(number)
        final_percent = no_primes/(2*side_length - 1)        
    return side_length


final = SideLength(0.1)
print(final)