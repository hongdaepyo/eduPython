n,k=map(int,input().split())
ans=1
for i in range(k):
    ans*=n-i
for i in range(k):
    ans//=k-i
print(ans%10007)