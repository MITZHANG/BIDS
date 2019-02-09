# 第18讲：程序运行时间-不同类型控制语句的运行时间
问题规模量：多大，复杂  
数组，长度为n，向量n
集合：$|S|=n$，各种操作  
图：顶点个数V，边数E，可用于通讯录场景  
大数：二进制表示，长度L
矩阵：m*n，n*n
运行时间随规模量而变化  

# 元操作
CPU指令集(RISC)：每条指令都是等长时间
程序$\Rightarrow$指令，共执行多少条指令？  
## 判断
```c++
if(a > 0)  
    b = 1;
else
    b = -1;
```
至多执行$c$条语句
## while
```c++
i = 0; //1条指令
while(i < n)  
    // do something 内层执行d条指令 //d*n条指令
```
一共执行$wn+c_w$条指令
## for
执行n次for语句
```c++
for(i = 0; i < n; ++i)  //外层执行f*n+c条指令
    // do something 内层执行d条指令 //d*n条指令
```
执行$fn+dn+c_f$条指令
## 双重for循环
```c++
for(i = 0; i < n; ++i)      //fn+c条指令
    for(j = 0; j < n; ++j)  //fn+c条指令
        a *= 2              //1*n条指令 
```
d$\Rightarrow fn+n+c_f$ //d*n  
总共执行时间：$fn+c_f+(fn+n+c_f)n=(f+1)n^2+(f+c_f)n+c_f$