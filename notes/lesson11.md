# 第11讲：查找问题的抽象数据类型视角
线性查找？  
1. 长度受限制
需要长度实时可变。可以采用向量
```c++
size_t LinearSearch(int k, const vector<int>& v){
    for(size_t pos=0; pos < v.size(); ++pos)
        if(v[pos] == k)
            return pos;
    return v.size(); //0, 1, ..., v.size()-1
}
```
2. 有序则难变  
采用链表  
3. 查变难两全  
采用二叉查找树  
4. ADT视角  
功能、性能、分析、实现  
操作：查找、插入、删除  
内部实现结构：数组、链表、树