# 第33讲：栈与队列
## 功能简介
栈，队列，保存时间先后，简便方案
### 栈
```c++
Stack<int> S;
S.push(1);
S.push(2);
S.push(3);
cout << S.top() << endl;
S.pop();
cout << S.top() << endl;
```
**特性：** 后进先出（LIFO）

### 队列
```c++
queue<int> Q;
Q.push(1);
Q.push(2);
Q.push(3);
cout << Q.front() << endl;
Q.pop();
cout << Q.front() << endl;
Q.front() = 4;
```
**特性：** 先进先出（FIFO），可读性   
画法很重要，形象