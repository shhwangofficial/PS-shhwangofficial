import sys
N = int(sys.stdin.readline())
mod = 1000000
my_dict = {
    0: 0,
    1: 1,
    2: 1,
}
def fibo(N):
    if my_dict.get(N, 0):
        return my_dict[N]
    if N % 2 == 1:
        a = fibo((N+1)//2) % mod
        b = fibo((N-1)//2) % mod
        my_dict[N] = ((a*a)%mod + (b*b)%mod) % mod
        
    else:
        a = fibo(N//2) % mod
        b = fibo(N//2+1) % mod
        c = fibo(N//2-1) % mod

        my_dict[N] = a*((b+c)%mod) % mod
        
    return my_dict[N]




print(fibo(N))
