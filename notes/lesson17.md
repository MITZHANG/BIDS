# 第17讲：时空之谜-运行时间和占用空间
主要指标：时间，空间  
计时器（程序运行时间）
运行时间，占用空间（时间复杂度，空间复杂度）

# 三种情况
最坏情况，最好情况，平均情况   
平均情况：给定一个概率模型，得到概率分布  

# 占用空间
模型：输入$\Rightarrow$算法$\Rightarrow$输出
逆置向量:D,例如1,2,3,4,5$\Rightarrow$5,4,3,2,1
```c++
void reverse(const vector<int>& D, vector<int>& R){
    for(size_t i = 0; i < D.size(); ++i)
        R[D.size()-i-1] = D[i]
}
```
占用空间为变量i  
```c++
void reverse(voctor<int>& D){
    vector<int> R(D.size())
    for(size_t i = 0; i < D.size(); ++i)
        R[D.size()-i-1] = D[i]
    for(size_t i = 0; i < R.size(); ++i) // D = R
        D[i] = R[i]
}
```
占用空间为R  
```c++
void reverse(vector<int>& D){
    for(size_t i = 0; i < D.size()/2; ++i)
        swap(D[D.size()-i-1], D[i])
}
```
占用空间为变量i、交换变量temp、函数调用  
