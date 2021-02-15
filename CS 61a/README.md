### 知识点

#### 熟练使用环境图
熟练使用 Environment Diagram 来分析Python 代码，可以方便理解很多问题。理解为函数调用帧在内存中状态（近似吧）
非常有用!!!
环境图分析的链接: http://pythontutor.com/composingprograms.html#mode=edit

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

#### Pure function 与 Non-pure function
Non-Pure Function 会有一定的副作用，会产生除返回值之外的额外的输出。
<pre><code>
>>>a = print("123")
123
>>>print(a)
None
</code></pre>
print函数的返回总是None，代表什么都没有。
有一个图很形象：见picture

#### 迭代器 
产生的需求：
不是一次性生成所有的值（所有的值不同时存在），而是按需计算，这样就不需要大块的内存来存放所有的值。类似于惰性计算，就是推迟数值的计算，直到需要的时候再进行计算。

迭代器：能够一个接一个、按顺序获取值

iter(iterable)   会调用对象中的__iter__方法 
next(iterator)   会调用对象中的__next__方法

调用next时，当容器中没有下一个值可以获取时会抛出 StopIteration 异常

for语句的背后的实现：
<pre><code>
items = iter(list)
try:
    while True:
        item = next(items)  // items.__next__()也可
        print(item)
except StopIteration as e:
    pass

</code></pre>

对迭代器调用 iter() 返回的还是这个迭代器，不是副本。

生成一个迭代器的方法：
- 调用 iter() 函数
- 生成器函数返回生成器
- 通过类(有 __iter__ 方法)实例化

实现1：通过yield
<pre><code>
class Letter:
    def __init__(self, start='a', end='d'):
        self.start = start
        self.end = end
    def __iter__(self):
        current = self.start
        while current <= self.end:
            yield current
            current = chr(ord(current)+1
</code></pre>

实现2：__iter__ 和 __next__
<pre><code>
#__iter__被称为 iterable interface
#__next__被称为 iteration interface
class LetterIterator():
    def __init__(self, start='a', end='d'):
        self.next_letter = start
        self.end = end
    def __next__(self):
        if self.next_letter == self.end:
            raise StopIteration
        letter = self.next_letter
        self.next_letter = chr(ord(letter)+1)
        return letter

class Letter:
    def __init__(self, start='a', end='d'):
        self.start = start
        self.end = end
    def __iter__(self):
        return LetterIterator(self.start, self.end)
</code></pre>


#### 生成器
生成器（generator): 迭代器的一种(设计更复杂的迭代器)，通过生成器函数产生的
生成器函数：包含yield关键词的函数(没有return语句)，返回一个生成器，通过next(returned generator)进入生成器函数内部
生成器对象有 __iter__ 和 __next__ 方法。
当生成器函数返回时，生成器抛出一个 StopIteration 异常

yield关键词：在当前位置暂停(所有的本地变量都会被保存),返回yeild之后表达式的值,在下一次调用继续从当前位置下一句继续执行

yield from:
yield from a 等价于 
for i in a:  
   yield i

4.2.9 看不太懂

#### class  and  object
`__init__ `是Python类中的构造器   （C++中有构造和析构）

self 和该类实例化的对象相关联（the first one, self, is bound to the newly created Account object），当方法被调用时， self会自动与对象名称进行关联。

类属性（也叫静态变量），在任何方法之外进行定义，类属性值可以在由同一个类实例化的所有对象之间共享，通过`类名.属性名`进行再赋值可以改变所有对象中相应属性的值，但是如果已经通过`实例名.属性名`进行赋值，优先使用这一个。

接口：

#### generic function
实现通用函数的方法：shared interfaces, type dispatching , type coercion

##### shared interfaces
通过使用接口和信息传递实现通用函数
###### special method
`__repr__`
`__str__`
`__init__`
`__bool__`
`__call__`
<pre><code>
class Addr:
    def __init__(self, n):
        self.n = n
    def __call__(self, k):
        return self.n + k

add_three = Addr(4)
add_three(4) #类似于函数调用
</code></pre>
``
``
###### 属性
通过 `@property` 装饰器和函数（计算其他属性的零参数函数）来实现类中的一些属性和其他的属性保持固定的关系
<pre><code>
from math import atan2

class ComplexRI:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    @property
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5
    @property
    def angle(self):
        return atan2(self.imag, self.real)
    def __repr__(self):
        return 'ComplexRI({0:g}, {1:g})'.format(self.real, self.imag)

ri = ComplexRI(5, 12)
ri.real

ri.magnitude  #不需要函数调用

</code></pre>
装饰器： 有4种类型：
函数装饰函数
函数装饰类
类装饰函数
类装饰类

装饰器本质上是高阶函数，@语法只是将函数传入装饰器函数，要想理解的更深刻，恢复普通的函数调用即可。
Python中的函数是第一公民，函数是对象、变量、作为参数、作为返回值，体现了函数式编程的特性。

##### Type dispatching





##### Type coercion






### 易忘点
用文档字符串中的用例进行测试的语法
python3 -m doctest file.py



### 异常分析
Debugging   推荐看一下 : https://inst.eecs.berkeley.edu/~cs61a/su19/articles/debugging.html

#### 异常1
error: local variable [var] reference before assignment
这种情况出现的原因是不允许修改定义在父帧中的变量
解决办法：
1. 建立一个新的变量来存储新值
2. 使用 nonlocal




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
#### lab06
完成
#### lab07
Q4 Q5 树不清楚
#### lab08
Q4 go on 
#### lab09
没开始

### homework完成情况
#### HW0
完成
#### HW1
完成
#### HW2
Q6 Q7 Q8 not finished
#### HW3
Q3之后没有完成  还是树
#### HW4
Q5 Q6 没做
#### HW5
没法做，

### project完成情况
#### project1：Hog
on going
#### project2: typing_test
not start
#### project3: ants
not start

