"""ЛР8 вариант 4. Булова Екатерина, БИ 2-1."""
import random,statistics,matplotlib.pyplot as plt
COINS=[1,6,9]
def greedy(S,desc=True):
 rem=S;out=[]
 for c in sorted(COINS,reverse=desc):
  out += [c]*(rem//c);rem%=c
 return out
def dp(S):
 d=[S+1]*(S+1);p=[0]*(S+1);d[0]=0
 for s in range(1,S+1):
  for c in COINS:
   if c<=s and d[s-c]+1<d[s]:d[s]=d[s-c]+1;p[s]=c
 out=[];s=S
 while s:c=p[s];out.append(c);s-=c
 return out
def main():
 rng=random.Random(2026);res={"max":[],"min":[]};hits={"max":0,"min":0}
 for _ in range(300):
  S=rng.randint(1,150);opt=len(dp(S))
  for name,desc in [('max',True),('min',False)]:
   got=greedy(S,desc);res[name].append((len(got)-opt)/opt*100);hits[name]+=len(got)==opt
 for name,v in res.items():print(name,statistics.mean(v),statistics.median(v),max(v),hits[name]/300)
 print('S=12',greedy(12),dp(12))
 ns=[5,10,20,40,80];rng=random.Random(2027);means=[]
 for N in ns:
  vals=[]
  for _ in range(N):
   S=rng.randint(1,150);opt=len(dp(S));vals.append((len(greedy(S))-opt)/opt*100)
  means.append(statistics.mean(vals))
 plt.plot(ns,means,marker='o');plt.grid();plt.xlabel('N — число тестовых сумм');plt.ylabel('Отклонение, %');plt.savefig('j4_deviation.png')
if __name__=='__main__':main()
