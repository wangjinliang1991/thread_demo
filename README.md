# threading

## 比较采用传统方式和多线程方式

## 注意：
1. 查看总共多少线程 print(threading.enumerate())
demo1的结果 [<_MainThread(MainThread, started 8008)>, <Thread(Thread-1, started 18320)>, <Thread(Thread-2, started 6132)>]
2. 查看当前线程名字
3. 封装为类，更加独立
4. 多线程的缺陷，修改全局变量时，执行多次可能线程间代码会冲突，demo3，同时给VALUE+1，需要加锁
5. Lock生产者消费者模式，demo4，如何跳出循环，gTotalTimes=10 gTimes=0生产者消费者条件
6. threading.Condition可以再没有数据的时候处于阻塞等待状态,wait(),ntify_all()通知机制，更加高效，省内存
7. queue 线程安全，原子性

## 应用：斗图吧获取表情包

### url：https://www.doutula.com/photo/list/?page=%d
### 注意：
1. 框架： 先写main函数，里面写url，再写parse函数
2. demo8 为异步，多线程，结构：生产者消费者模式
   每一页的url→生产者（获取表情url）→每个表情url→消费者（下载表情）