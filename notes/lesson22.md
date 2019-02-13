# 第22讲：抽象数据类型的性能
## 回顾集合
规模量：n个元素（当前个数），对其进行若干操作。  
最小元素，最大元素，find，insert，erase，下一元素，上一元素的七种操作。  
set集合：最小元素($O(1)$)，最大元素($O(1)$)，find($O(\log n)$)，insert($O(\log n)$)，erase($O(\log n)$)，下一元素($O(\log n)$)，上一元素($O(\log n)$)  
有序向量：最小元素($O(1)$)，最大元素($O(1)$)，find($O(\log n)$)二分查找，insert($O(n)$)，erase($O(n)$)，下一元素($O(1)$)，上一元素($O(1)$)  
以上均为最坏情况分析。  
## 实例分析
```c++
// 现有向量V，内含n个int型元素
set<int> S;
for(size_t i=0; i < V.size(); ++i) //O(n)时间
    S.insert(V[i]);
```
当前S内有r个元素，运行时间每次$O(\log r)$，至多需要$c \log r$时间。  
需要满足条件：$r\neq0, r\neq1$，运行时间为c。  
计算上述插入程序的运行时间：$c+c+c\log2+c\log3+c\log(n-1) \le 2c + c\log(n!) = O(1) + O(n\log n) = O(n \log n)$  
计算for循环时间：$O(n)$  
总时间：$O(n)+O(n \ log n) = O(n \ log n)$  
性能参数$\Rightarrow$求和  
$O(\log r)$累积分析：$O(1)$不影响，$n-1$过渡到$n$ 
$c\log r$分析 $\le \sum_{r=1}^{n}(c \log r)=c \log(n!)=O(n\log n)$