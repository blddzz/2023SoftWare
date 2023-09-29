| 作业属于课程 | <https://bbs.csdn.net/forums/ssynkqtd-05> |
| ------ | ----------------------------------------- |
| 作业要求   | <https://bbs.csdn.net/topics/617294583>   |
| 作业目标   | 实现可视化计算器                                  |
| 其他参考文献 | ...                                       |

## 项目链接

[源码](https://github.com/blddzz/2023SoftWare)

## 可视化界面

![在这里插入图片描述](https://img-blog.csdnimg.cn/cc5369dfbb5240eba2fde07bdf704e95.gif#pic_center)

## 1.PSP表格

| PSP阶段                                   | Personal Software Process Stages | 预估耗时（分钟） | 实际耗时（分钟） |
| --------------------------------------- | -------------------------------- | -------- | -------- |
| **Planning**                            | 计划                               | 20       | 30       |
| • Estimate                              | • 估计这个任务需要多少时间                   | 20       | 30       |
| **Development**                         | 开发                               | 590      | 620      |
| • Analysis                              | • 需求分析 (包括学习新技术）                 | 20       | 25       |
| • Design Spec                           | • 生成设计文档                         | 70       | 80       |
| • Design Review                         | • 设计复审                           | 10       | 15       |
| • Coding Standard                       | • 代码规范 (为目前的开发制定合适的规范)           | 10       | 10       |
| • Design                                | • 具体设计                           | 30       | 40       |
| • Coding                                | • 具体编码                           | 300      | 360      |
| • Code Review                           | • 代码复审                           | 60       | 40       |
| • Test                                  | • 测试（自我测试，修改代码，提交修改）             | 100      | 50       |
| **Reporting**                           | 报告                               | 120      | 105      |
| • Test Report                           | • 测试报告                           | 20       | 20       |
| • Size Measurement                      | • 计算工作量                          | 10       | 15       |
| • Postmortem & Process Improvement Plan | • 事后总结, 并提出过程改进计划                | 90       | 70       |
|                                         | **合计**                           | 730      | 755      |

## 2.解题思路描述

一开始看到要做一个可视化界面时，我第一时间想到是是用html+css+js，但是之前没做过与前端相关的，感觉不好上手，后来了解到Python有自带tkinter可以生成图形化界面，于是决定用Python来完成这次的作业，并且GitHub上有模块可以优化一下tkinter的显示模块，比原本的tkinter更加美化。

## 3.设计与实现过程

- 运算逻辑代码

```python
class Calculation:
    def __init__(self):
        # 定义一个 _symbols 属性，用于存储定义的运算符，下文实现 defined_operator 会用到
        self._symbols = {}
        self.defined_operator("+", self.add, 1, 2)
        self.defined_operator("-", self.sub, 1, 2)
        self.defined_operator("x", self.multi, 2, 2)
        self.defined_operator("÷", self.div, 2, 2)
        self.defined_operator("(", None, 0, 0)
        self.defined_operator(")", None, 0, 0)
        self.defined_operator("%", self.mod, 2, 2)  # 求余
        self.defined_operator("!", self.fac, 4, 1)  # 阶乘
        self.defined_operator("^", self.pow, 3, 2)  # 指数
        self.defined_operator("sin", self.sin, 4, 1)  # 自定义sin函数
        self.defined_operator("cos", self.cos, 4, 1)  # 自定义cos函数
        self.defined_operator("tan", self.tan, 4, 1)  # 自定义tan函数
        self.defined_operator("asin", math.asin, 4, 1)  # 自定义asin函数
        self.defined_operator("acos", math.acos, 4, 1)  # 自定义acos函数
        self.defined_operator("atan", math.atan, 4, 1)  # 自定义atan函数
        self.defined_operator("ln", math.log, 4, 1)  # 自定义ln函数
        self.defined_operator("lg", math.log10, 4, 1)  # 自定义lg函数
        self.defined_operator("√", math.sqrt, 4, 1)  # 自定义根号函数
        self.defined_operator("π", None, 0, 0)
        self.defined_operator("e", None, 0, 0)
        # 计算正则
        self.calc_reg()

    # 定义运算符的方法
    def defined_operator(self, symbol, handle=None, precedence=0, arg_count=0):
        self._symbols[symbol] = {
            'symbol': symbol,
            'handle': handle,
            'precedence': precedence,
            'argCount': arg_count,
        }



    # 计算正则
    def calc_reg(self):
        regstr = r"\d+(?:\.\d+)?|" + "|".join(re.escape(val['symbol']) for val in self._symbols.values())
        regstr += r"|."
        self.pattern = re.compile(regstr)
        #print(self.pattern)


    def parse(self, s):
        # 操作符栈，输出栈
        operators, result = [], []
        # 正则匹配的结果，当前匹配到的符号
        match, token = None, None
        # 去除空格的处理
        s = re.sub(r'\s', '', s)
        l=1
        last_number=None
        flag = 0
        while True:            
            # 没有匹配到，结束匹配
            match = self.pattern.match(s)
            if(match==None):
                break
            l=len(match.group(0))
            s = s[l:]
            # print(match)
            token = match.group(0) if match else None
            #pi和e
            if(token=='π'):
                result.append(math.pi)
                continue
            if(token=='e'):
                result.append(math.e)
                continue


            if not token.replace(".", "").isdigit():  # 如果不是一个数字

                if token == "(" :
                    # 如果是一个左括号或者是一个函数，则直接入操作符栈
                    operators.append(token)
                elif token == ")":
                    # 当匹配到的是一个右括号
                    # 循环弹出操作符栈，并压入输出栈，
                    # 直到遇到左括号为止
                    o = operators.pop()
                    while o != "(":
                        result.append(o)
                        o = operators.pop()
                elif not operators:  # 操作符为空，直接入操作符栈
                    if token == '-':
                        if(last_number==None or last_number=='(' or not last_number.isdigit() and last_number!=')' ):
                            result.append(0)
                            operators.append('-')
                            continue
                    operators.append(token)
                else:  # 操作符栈不为空，需要比较优先级
                    # 获取前一个操作符
                    if token == '-':
                        if(last_number==None or last_number=='(' or not last_number.isdigit() and last_number!=')' ):
                            result.append(0)
                            operators.append('-')
                            continue
                    prev = operators[-1]
                    while prev and self._symbols[token]['precedence'] <= self._symbols[prev]['precedence']:
                        # 如果当前操作符的优先级不比栈顶元素操作符的优先级高，
                        # 则将栈顶的操作符弹出并压入输出栈，
                        # 循环与剩余的栈的栈顶元素做比较直到当前元素的优先级比栈顶元素高
                        result.append(operators.pop())
                        if(len(operators)==0):
                            break
                        prev = operators[-1]
                    # 压入当前操作符压入操作符栈
                    operators.append(token)
            else:  # token 是一个数字，直接进入输出栈
                result.append(float(token))
            last_number = token
        # 将操作符栈剩余的操作符全部弹出并压入输出栈
        result.extend(reversed(operators))
        # 得到输出栈，转为字符串即为后缀表达式
        return result

    def evaluate(self,r):
        # 输出栈
        result = []
        # 获取当前解析的结果
        r = self.parse(r)
        i = 0
        while i < len(r):
            c = r[i]
            if not isinstance(c, (int, float)):  # 如果不是数字
            # 从 result 中截取出 argCount 个数字，展开后传入运算符的处理方法
                token = self._symbols[c]
                args = []
                for _ in range(token['argCount']):
                    if not result:
                        raise ValueError("Insufficient operands for operator")
                    args.append(result.pop())

                args.reverse()
                result.append(token['handle'](*args))
            else:
                result.append(c)
                #print(result)
            i += 1
        return result.pop()


    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def multi(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def mod(self, a, b):
        return a % b

    def pow(self, a, b):
        return math.pow(a, b)

    def sin(self,a):
        return sy.sin(math.pi/180*a)

    def cos(self,a):
        return sy.cos(math.pi/180*a)

    def tan(self,a):
        return sy.tan(math.pi/180*a)

    def fac(self,a):
        b=a%1
        if(b or a < 0):
            raise ValueError("NaN")
        result = 1
        i=1
        while(i<=a):
            result *= i
            i+=1
        return result
```

代码逻辑：首先定义了各种符号绑定的运算函数，优先级，所需要的参数，然后写一个正则表达式对给出的计算表达式进行匹配，获取数字和符号用，进行运算主要由两个方法来完成一个parse函数，用来将表达式转成后缀形式，转换的方式是通过栈来完成的，首先有两个栈，一个是操作符栈，一个是输出栈，对表达式进行正则匹配后，取出每一个元素，如果该元素是数字，则直接加入输出栈，如果是操作符则要进行几种情况的判断，如果操作符是左括号，则直接入栈，如果操作符是右括号，则循环将操作符栈中的元素弹出并压入输出栈直到遇到左括号为止，如果操作符栈为空，则直接入栈，如果操作符不为空，则需要比较优先级，优先级比栈顶高则直接入栈，否则循环弹出栈顶元素并压入输出栈直到栈顶元素优先级低于目前的操作符，然后再将其压入操作符栈，最后表达式处理结束，将操作符栈中的元素全部弹出压入输出栈中，还有一个则是用来计算的后缀表达式的函数evaluate，将栈中的元素依次弹出，如果是数字，则加入计算的栈中，遇到操作符，则从栈中取出所需参数个数的数字进行运算。

- 异常处理

```python
def evaluate_expression():
    try:
        list.clear()
        deal=Calculation()
        expression = result_num.get()
        result = deal.evaluate(expression)
        result_num.set(result)
        list.append(str(result))
    except Exception as e:
        result_num.set("Error")
```

捕获该函数运行中出现的错误异常并抛出，在可视化界面上显示Error

## 4.程序性能改进

1.思路的转变
在刚开始做这个计算器时，因为了解到Python自带的eval函数可以直接计算得到结果，所以一开始的思路就是直接把要算的表达式写进eval函数就可以实现计算的功能，但是刚开始时实现加减乘除这些四则运算是没有问题的，但是如果要实现科学计算，就没有那么简单，因为eval函数在计算时不能直接识别三角函数“sin”，需要你写进表达式的是math.sin()，而如果只是写三角函数这种右结合的运算其实也能用eval加上正则表达式轻松解决，但是如果加上阶乘这种左结合的运算，就需要对字符串从左到右扫描然后更改，但是当时的我没有想到，觉得这个办法不好做，于是我想起来了后缀表达式，后缀表达式可以将原先算式中的括号去掉，同时也能保证运算的优先级
2.在学习了中缀表达式转后缀表达式，并且在我的代码上实现了该效果时，我认为是没有问题的，但是在测试有没有bug时，发现对“-”需要进行特判，因为“-”可以是做减法，也可以是负数，于是我第一次尝试是对“-”进行判断，如果是操作符，就正常进行判断进入操作符栈，如果是负号，就进行标记，这个办法在刚开始时感觉没有问题，但是后来发现这样子无法判断这个负号是谁的，因为我是将负号标记，然后在遇到下一个是数字时，将那个数字转成相反数，但是如果遇到（-cos（-4)）这种，就会给4判断有两个负号，从而变成正的，于是我就想对“-”这个符号定义两个函数处理方法，这样负号也是操作符，会压入栈中，有优先级的判定，这样就可以先把后面的式子算出来再对整体做相反数操作，好巧不巧，当时遇到这个bug是，对面宿舍的同学也在做负号的处理，但是他和我不一样，他是用堆栈对计算式先计算局部，最后合起来得到结果，而我是先将一个计算式全部转成后缀，再运算，尽管思路不同，但是他处理负号是，是将“-”压栈，同时数字栈中压入一个0，这个思路当时听到我就觉得很妙，这样子的做法比我之前想到的对“-”绑定两个处理函数要巧妙的多，因为这样就使得负号也能够看成是减法，bug也得以解决。

## 5.单元测试展示

![](https://img-blog.csdnimg.cn/295857c69c78413188d627cc7e858db5.png#pic_center)

- 单元测试代码
  
  ```python
  import unittest
  from Calculation import *
  
  ```

## 6.心路历程与收获

这次的软件工程实践是第一次做出一个可视化的工具出来，做出来后还是非常有成就感的，而且在整个的过程中，不断的去思考怎么做出一个功能，然后进行测试再debug，同时也有和同学一起商讨bug的解决办法，互相交流想法，让自己的思路也得到了拓展，在最开始的简单的四则运算，再到后来能够支持科学运算，看着自己写的工具支持的功能变多，自己也感到开心，同时编写这次的作业也提升了我对python的了解以及应用能力，同时也学习了如何进行单元测试来对自己的代码进行测试保证其可行度。
