# 第23讲：抽象数据类型选用
去除不必要的元素：输入u个自然数，以-1作为终结（以负数终结即可）  
现有集合C（内有v个元素），将输入之中不在C中的数存入集合D之中，C和D应如何选择？  
在集合视角上思考问题  
```c++
int data;
for(cin >> data; data != -1; cin >> data)
    if(C.find(data) != c.end())
        D.insert(data)
```
关键在find，insert操作  
最坏情况：u次find操作，u次insert操作  
## 抽象数据类型若干选项
有两个find，insert操作，分别考虑set、有序向量、无序向量  
set：find($O(\log n)$)，insert($O(\log n)$)  
有序向量：find($O(\log n)$)，insert($O(n)$)   
无序向量：find($O(n)$)[线性查找]，insert($O(1)$)[push_back分摊意义]   
C：可选set、有序向量  
D：无序向量  
需要组合起来，综合考虑，将数据类型排列组合，推出最短时间
## 总运行时间
u次find<img src="http://latex.codecogs.com/gif.latex?\left \{ \begin{array}{c} O(1) \Rightarrow uc=O(u)\\ O(\log n) \Rightarrow uc \log v=O(u\log v) \\ O(n) \Rightarrow ucv = O(uv) \end{array}\right."/>  
u次insert<img src="http://latex.codecogs.com/gif.latex?\left \{ \begin{array}{c} O(1) \Rightarrow \sum_{j=1}^uc=O(u)\\ O(\log n) \Rightarrow \sum_{j=1}^uc\log j=O(u\log u) \\ O(n) \Rightarrow \sum_{j=1}^ucj = O(u^2) \end{array}\right."/>  
## 神秘选手
特定问题：自然数范围在[0，U]之间，可让find和insert都只用$O(1)$时间，这个是最快的操作。  
如何实现：用长为U的向量V。  
V[x]为0时，x不在集合中；V[x]为1，x在集合中  
进一步可用计数器实现多重集合  
集合 $\Rightarrow$ 位向量，节约空间
