# 第21讲:运行时间的差异-对比各种时间的巨大差异并给出渐近记号的两个定理
## 时间差异
千亿条指令计算机（指令总数$\log n, n,n \log n, n^2, 2^n, n!$）  
当n取10亿，计算运行时间  
$\log n$(0.3ns)，$n$(10ms)，$n \log n$(0.3s)，$n^2$(116天)  
可以看到上述的强弱关系    
$1 \prec \log n \prec n \prec n\log n \prec n^{1+\epsilon} \prec n^2 \prec n^d \prec \lambda^n \prec n! \prec n^n$  
## 若干定理
$1+2+...+n=\frac{n(n+1)}{2}$  
$1^2+2^2+...+n^2=\frac{n(n+1)(2n+1)}{6}$   
$\left. \begin{array}{c}
(n+1)^3-n^3=3n^2+3n+1 \\
n^3-(n-1)^3=3(n-1)^2+3(n-1)+1 \\
\vdots \\
2^3-1^3 = 3(1)^2+3(1)+1 
\end{array} \right\} \Rightarrow $  
**定理1:** $1^d+2^d+...+n^d=\Theta(n^d+1), \sum_{i=1}^{n}i^d=\Theta(n^d+1)$  
**定理2:** $log1+log2+...+logn=log(n!)=\Theta(n \log n)$  
使用：已知$T(n) \le c\log 1+c\log 2+...+c\log n=c \log (n!)$ 所以可得$T(n)=O(n \ log n)$  
&emsp;&emsp;借助这两个定理，能够忽略一些推导的细节，能够更快地完成算法分析的工作，基本上常见的数据结构可以完成分析，在归结到常用的运行时间量级上面，可以更好地比较算法的差异。
