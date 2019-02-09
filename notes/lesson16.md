# 第16讲：STL容器一览
vector：向量  
list：列表，双链表（性能不是很好）  
forward_list:单向列表，单链表  
stack：栈，LIFO（历史结构，例如：调用栈）  
queue：队列，FIFO（模拟）  
deque:双端队列  
priority_queue:优先级队列（优先级）  
set:集合  
multiset:多重集合（允许存放重复元素）  
map:映射（键$\Rightarrow$值，下标$\Rightarrow$元素）  
multimap:多重映射  
unordered_set:无序集合（字典，快速进行查找，散列）  
unordered_multiset:无序多重集合  
unordered_map：无序映射（键$\Rightarrow$值）  
unordered_multimap：无序多重映射

# 数据结构思维
算法场景：约10MB英文序列，长度未知，逆置序列存为文本文件  
ADT:栈，LIFO  
DS:vector,deque,list（时间最佳vector）  
调优：reserve预留 10MB$\Rightarrow$20MB