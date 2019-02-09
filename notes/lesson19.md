# 第19讲：量级-用简单的语言讲解函数的量级
n为规模量  
$T_1(n)=an^2+bn+c$  
$T_2(n)=dn+e$  
常数不太重要，CPU可以忽略掉  
$f(n)=\Theta(g(n))$   
当n超过一定的值时，满足$c_1g(n)\le f(n) \le c_2g(n)$  
$g(n)$代表一类函数  
例：$an^2=\Theta(n^2), b\log n=\Theta(\log n), c=\Theta(1)$  
不讨论复制的\Theta记号  

# 常见的$\Theta$记号
## 高效算法
$\Theta(1)$  
$\Theta(\log n)$  
$\Theta(n)$  
$\Theta(n\log n)$  
$\Theta(n^{1+\epsilon}),0<\epsilon<1$  
$\Theta(n^2)$  
$\Theta(n^d),d>2$  
## 不是高效算法
$\Theta(\lambda ^n)$  
$\Theta(n!)$  
$\Theta(n^n)$  

# 强弱关系
$f(n)\prec F(n)：F(n)强于f(n)$  
$\frac{xF(n)}{yf(n)} \to +\infty, n^2\succ n$  
$\Theta(f(n)) + \Theta(F(n)) = \Theta(F(n))$  
$1 \prec \log n \prec n \prec n\log n \prec n^{1+\epsilon} \prec n^2 \prec n^d \prec \lambda^n \prec n! \prec n^n$  
<br/>
$T_1(n)=an^2+bn+c=\Theta(n^2) + \Theta(n) + \Theta(1) = \Theta(n^2)$  
$T_3(n)=an \log n + bn = \Theta(n \log n) + \Theta(n)=\Theta(n \log n)$  

# $O$记号
$f(n)=O(g(n))$  
当n超过一定值时，$f(n) \le cg(n)$  
依然有强弱关系：$O(f(n))+O(F(n))=O(F(n))$  
$O$记号适合于逐步推进（从表达式进行求和运算得到大$O$记号    
例:for语句，i从1到n，每条语句时间不超过$ci$  
$T(n) \le \sum_{i=1}^nci = \frac{n(n+1)}{2}c=\frac{c}{2}n^2+\frac{1}{2}c$  
$T(n)=O(n^2)+O(1)$  