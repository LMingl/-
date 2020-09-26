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

### homework完成情况
#### HW0
完成
#### HW1
完成

### project完成情况
#### project1：Hog
on going
