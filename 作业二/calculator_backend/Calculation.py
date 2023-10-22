import re
import sympy as sy
import math
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
        # s = re.sub(r'\s', '', s)
        # print(s)
        #print(self.pattern)
        l=1
        last_number=None
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
                        if(last_number==None or last_number=='(' or not last_number.replace('.','').isdigit() and last_number!=')' ):
                            result.append(0)
                            operators.append('-')
                            continue
                    operators.append(token)
                # elif token == ",":  # 如果是参数分隔符，不断弹出操作符压入输出队列
                #     prev = operators[-1]
                #     while prev != "(":
                #         result.append(operators.pop())
                #         prev = operators[-1]
                #     # 将参数分隔符入栈
                #     operators.append(token)
                else:  # 操作符栈不为空，需要比较优先级
                    # 获取前一个操作符
                    if token == '-':
                        if(last_number==None or last_number=='(' or not last_number.replace('.','').isdigit() and last_number!=')' ):
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
        # if not result:
        #     raise ValueError("No result")
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
        # if b == 0:
        #     raise ValueError("Modulo by zero")
        return a % b

    # def fac(self, a):
    #     if a < 0:
    #         raise ValueError("Factorial input must be non-negative")
    #     return math.factorial(a)

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
        # if a > 170:
        #     return ValueError("Inf")
        result = 1
        i=1
        while(i<=a):
            result *= i
            i+=1
        return result
    
# deal=Calculation()
# print(deal.evaluate("1+1"))
