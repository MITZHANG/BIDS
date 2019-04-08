# 第26讲：自然数映射与下标
向量V，下标x，V[x]，V(x)映射在常数时间$O(1)$能完成  
**实例：** 学生的成绩统计vector<int>型 Scores，值范围0-100  
统计0-9,10-19,20-29,...,80-89,90-100  
**简单处理：**  
```c++
vector<int> Nums(10, 0);
for(size_t i=0; i<Scores.size(); ++i)
    if(Scores[i]<10)
        Nums[0]++;
    else if(Score[i]<20)
        Nums[1]++;
    else if(Score[i]<20)
        Nums[1]++;
        30)
        Nums[2]++;
    else if(Score[i]<40)
        Nums[3]++;
    else if(Score[i]<50)
        Nums[4]++;
    else if(Score[i]<60)
        Nums[5]++;
    else if(Score[i]<70)
        Nums[6]++;
    else if(Score[i]<80)
        Nums[7]++;
    else if(Scores[i]<90)
        Nums[8]++;
    else
        Nums[9]++;
```
平均5.44次判断  
<img src="https://latex.codecogs.com/gif.latex?\underbrace&space;{\frac{10}{101}*1&plus;\frac{10}{101}*2&plus;...&plus;\frac{10}{101}*9&plus;\frac{11}{101}*9}_{5.44}"/>  
**下标方法：**  
```c++
vector<int> Nums(11, 0);
for(size_t i = 0; i < Scores.size(); ++i)
    Nums[Scores[i]/10]++;
Nums[9] += Nums[10];
Nums.pop_back();
```
**推广：** 0-100，区间分段[0,46), [46, 53), [53, 79), [79,101)  
```c++
vector<int> Nums(101, 0);
for(size_t i = 0; i < Scores.size(); ++i)
    Nums[Scores[i]]++;
```
**前缀和：** <img src="https://latex.codecogs.com/gif.latex?\left&space;\{&space;\begin{array}{c}&space;P(x)=\sum_{i=0}^xNums[i]&space;\\&space;P(x&plus;1)=P(x)&plus;Nums[x]&space;\end{array}&space;\right."/>   
**例如：** $P(53)-P(46)$可以一次求出累积
## 模拟自然数（字符型）
DNA计数  
```c++
String DNA = "ACGGCTA";
vector<int> Nums(26, 0);
for(Size_t i = 0; i < DNA.size(); ++i)
    Nums[DNA[i] - 'A']++;
cout << Nums['A' - 'A'];
cout << Nums['C' - 'A'];
cout << Nums['G' - 'A'];
cout << Nums['T' - 'A'];
```
**推广：** 三联子个数，例如：AAA，AAC,..., TTT一共有$4^3=64$  
第一个方法：4进制数表示$A\rightarrow 0,C\rightarrow 1,G\rightarrow 2,T\rightarrow 3$  
再将4进制数再转化为10进制数表示$(103)_4\Rightarrow 10进制数 \Rightarrow 下标$
26个字母的向量做映射