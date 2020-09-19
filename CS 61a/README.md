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

#### lab01
未通过的案例： 最后两个  原因：未知

#### higher-order function 高阶函数
- 未掌握知识点
