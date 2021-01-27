### 知识点
#### Boolean Operators 布尔操作
未掌握知识点：
- short-circuit
例子：

\>>> True or 1 / 0
? True #not error
\>>> True and 13
? 13
It evaluates to True **because Python's and and or operators short-circuit**. 
That is, they don't necessarily evaluate every operand.

|Operator | Operator | Evaluates from left to right up to | Example |
| -----| -----| ------| ------| 
|AND| All values are true | The first false value | False and 1 / 0 evaluates to False|
|OR | At least one value is true | The first true value | True or 1 / 0 evaluates to True |

**If and and or do not short-circuit, they just return the last value; another way to remember this is that and and or always return the last thing they evaluate, whether they short circuit or not**. Keep in mind that and and or don't always return booleans when using values other than True and False.


#### higher-order function 高阶函数
- 未掌握知识点1
高阶函数(高阶函数就是操作函数的函数 )
高阶函数有以下这些特性，的原因是：在Python中function被认为是first-class的
1. 函数作为参数
2. 函数作为返回值
3. 嵌套定义

- 未掌握知识点2
一种交替嵌套的情况：

- 何种情况下使用高阶函数，不太会用

#### 迭代转化为递归

first try implementing pingpong **using assignment statements and a while statement**.
 Then, to convert this into a recursive solution, 
 **write a helper function that has a parameter for each variable that changes values in the body of the while loop**.

#### Data Abstraction
- 未掌握知识点1
如何对数据进行抽象，使得在改变底层的数据结构时不会影响上层函数（调用底层函数的函数）
需要良好的设计

- 未掌握知识点2
Abstraction Barriers
见图片
不要违反abstraction barriers, 这可以在变化时对程序做出最小的改变

However, the point of data abstraction is that we do not need
to know how an abstract data type is implemented, but rather just how we can interact with and use the data type.

#### Tree- cloure property of a data type(数据类型的闭包属性)
In general, a method for combining data values has a closure property if the result of combination can itself be combined using the same method



#### 对Tree的ADT依旧没有搞懂

#### nonlocal
在高阶函数中，如果我们不使用 nonlocal ，那我们只能访问父帧中变量的值，而不能改变父帧中变量的值。否则会报错的。
解释：
For example, the line balance = ... in withdraw, this assignment statement tells Python to expect a variable called balance inside withdraw's frame, so Python will not look in parent frames for this variable. However, notice that we tried to compute balance - amount before the local variable was created! That's why we get the UnboundLocalError

当使用 nonlocal 时一些重要点需要注意：
- 不能用nonlocal修饰全局变量，（全局变量就是定义在全局帧中的变量） 
- 如果 nonlocal 修饰的变量没有被找到，报 SyntaxError
- 当前帧中已经声明的变量不能再声明为 nonlocal 

#### is 与 == 的区别
<pre><code>
>>> lst1 = [1, 2, 3, 4]
>>> lst2 = [1, 2, 3, 4]
>>> lst1 == lst2
True
>>> lst1 is lst2
False
</code></pre>
lst1与lst2 的 identity 不同，尽管里面的内容相同，但用 is 会返回false

我自己理解就是在环境中，他们的指向是不同的，所以identity不同，如果指向同一个对象（比如：list），那么identity就是相同的。



### 易忘点
用文档字符串中的用例进行测试的语法





### 异常分析
#### 异常1
error: local variable [var] reference before assignment
这种情况出现的原因是不允许修改定义在父帧中的变量
解决办法：
1. 建立一个新的变量来存储新值
2. 待定




### lab完成情况
#### lab01
未通过的案例： 最后两个  原因：未知
#### lab02 : 
未完成Q8
#### lab03:
完成
#### lab04
完成
#### lab05
acorn_finder(t)未完成   python中的树不太懂

### homework完成情况
#### HW0
完成
#### HW1
完成
#### HW2
Q6 Q7 Q8 not finished
#### HW3
Q3之后没有完成  还是树不太懂



### project完成情况
#### project1：Hog
on going
