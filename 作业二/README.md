# ​Vue+flask实现前后端分离计算器

**目录**

[ Github仓库链接 ](#%C2%A0Github%E4%BB%93%E5%BA%93%E9%93%BE%E6%8E%A5%C2%A0)

[ psp表格](#%C2%A0psp%E8%A1%A8%E6%A0%BC)

[ 成品展示](#%C2%A0%E6%88%90%E5%93%81%E5%B1%95%E7%A4%BA)

[设计实现过程 ](#%E8%AE%BE%E8%AE%A1%E5%AE%9E%E7%8E%B0%E8%BF%87%E7%A8%8B%C2%A0)

[代码说明](#%E4%BB%A3%E7%A0%81%E8%AF%B4%E6%98%8E)

[心路历程和收获](#%C2%A0%E5%BF%83%E8%B7%AF%E5%8E%86%E7%A8%8B%E5%92%8C%E6%94%B6%E8%8E%B7)

---

| 这个作业属于哪个课程 | [作业社区](https://bbs.csdn.net/forums/ssynkqtd-05 "作业社区")                                   |
| ---------- | ---------------------------------------------------------------------------------------- |
| 这个作业要求在哪里  | [第二次作业--前后端交互计算器-CSDN社区](https://bbs.csdn.net/topics/617377308 "第二次作业--前后端交互计算器-CSDN社区") |
| 这个作业的目标    | 完善计算器，添加利率计算器                                                                            |
| 其他参考文献     | 无                                                                                        |

## Github仓库链接

[后端代码](https://github.com/blddzz/2023SoftWare/tree/main/%E4%BD%9C%E4%B8%9A%E4%BA%8C/calculator_backend "后端代码")

[前端代码](https://github.com/blddzz/2023SoftWare/tree/main/%E4%BD%9C%E4%B8%9A%E4%BA%8C/calculator_frontend "前端代码")

## psp表格

| P2P                                     | Personal Software Process Stages | 预估耗时（分钟） | 实际耗时（分钟） |
| --------------------------------------- | -------------------------------- | -------- | -------- |
| Planning                                | 计划                               | 20       | 30       |
| • Estimate:                             | • 估计这个任务需要多少时间                   | 20       | 30       |
| Development                             | 开发                               | 795      | 885      |
| • Analysis                              | • 需求分析 (包括学习新技术）                 | 480      | 500      |
| • Design Spec                           | • 生成设计文档                         | 10       | 30       |
| • Design Review                         | • 设计复审                           | 10       | 30       |
| • Coding Standard:                      | • 代码规范 (为目前的开发制定合适的规范)           | 5        | 5        |
| • Design                                | • 具体设计                           | 40       | 40       |
| • Coding                                | • 具体编码                           | 200      | 230      |
| • Code Review:                          | • 代码复审                           | 20       | 20       |
| • Test                                  | • 测试（自我测试，修改代码，提交修改）             | 30       | 30       |
| Reporting                               | 报告                               | 30       | 40       |
| • Test Repor:                           | • 测试报告:                          | 5        | 5        |
| :• Size Measurement                     | • 计算工作量                          | 10       | 10       |
| • Postmortem & Process Improvement Plan | • 事后总结, 并提出过程改进计划                | 10       | 10       |
|                                         | 合计                               | 845      | 955      |

## 成品展示

* 科学计算器，计算功能，历史记录，清零回退

![](https://img-blog.csdnimg.cn/02c248d223734b9491d4b5dda501fc7d.gif)![]("点击并拖拽以移动")​**编辑**

* 错误提示

![](https://img-blog.csdnimg.cn/4bcab255419f4f6e912c2fa9427a29d7.gif)![]("点击并拖拽以移动")​**编辑**

* 利率计算器，计算存/贷款利率，修改利率，前端展示利率

![](https://img-blog.csdnimg.cn/0ed4028fe65f4c69b6242aec33bd4414.gif)![]("点击并拖拽以移动")​**编辑**

## 设计实现过程

* 思维导图

![](https://img-blog.csdnimg.cn/e867e2a11a3c41958bb354453bba514d.png)![]("点击并拖拽以移动")​**编辑**

* 前端

前端使用Vue作为框架进行开发，同时使用Element-ui的组件加入前端界面中，来方便开发和美化界面，同时使用axios作为网络请求与后端通信

* 后端

使用flask作为后端的框架，数据库使用mysql，同时使用pymysql来进行数据库管理

## 代码说明

后端核心功能代码实现

```python
# 查询历史记录
@app.route("/query",methods=['POST'])
def evaluate():
    if request.method=="POST":
        activities = []
        sql = "SELECT * FROM caculator ORDER BY id DESC LIMIT 10"
        cursor.execute(sql)
        results = cursor.fetchall()
        for result in results:
            expression = result[1]+" = "
            answer = result[2]
            dic = {'expression':expression,'result':answer}
            activities.append(dic)
        print(activities)
        return jsonify(activities)
#计算器计算
@app.route("/calculator",methods=['POST'])
def check():
    if request.method=="POST":
        try:
            deal=Calculation()
            expression = request.form.get("expression")
            result = deal.evaluate(expression)
            sql = "insert into caculator(expression,result) values('%s','%s')"%(expression,result)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            result="Error"
        response={
            'equation':str(result)
        }
        return jsonify(response)
# 查询存款汇率
@app.route("/depositRate",methods=['POST'])
def caculateDepositRate():
    if request.method=="POST":
        money = request.form.get("Money")
        time = request.form.get("Time")        
        numTime = change(time)
        if(flag):
            time="活期"
        sql="SELECT deposit.rate FROM deposit WHERE deposit.time = '%s'"%(time)
        cursor.execute(sql)
        rate = cursor.fetchone()
        print(rate[0])
        result = float(money)*float(rate[0])*numTime*0.01
        return jsonify(round(result,3))
# 查询贷款汇率
@app.route("/loanRate",methods=['POST'])
def caculateLoanRate():
    if request.method=="POST":
        money = request.form.get("Money")
        time = request.form.get("Time")
        selectTime = select(float(time))
        sql="SELECT rate FROM loan WHERE time = '%s'"%(selectTime)
        cursor.execute(sql)
        rate = cursor.fetchone()
        result = float(money)*float(rate[0])*float(time)*0.01
        return jsonify(round(result,3))
# 修改存款汇率
@app.route("/updateDepositRate",methods=['POST'])
def updateDepositRate():
    if request.method=="POST":
        try:
            time = request.form.get("Time")
            rate = request.form.get("Rate")
            sql="UPDATE deposit SET rate = '%f' WHERE time = '%s'"%(float(rate),time)
            cursor.execute(sql)
            db.commit()
            result = "success"
        except Exception as e:
            result= 'error'
        response={'message':result}
        return jsonify(response)
#修改贷款汇率
@app.route("/updateLoanRate",methods=['POST'])
def updateLoanRate():
    if request.method=="POST":
        try:
            time = request.form.get("Time")
            rate = request.form.get("Rate")
            sql="UPDATE loan SET rate = '%f' WHERE time = '%s'"%(float(rate),time)
            cursor.execute(sql)
            db.commit()
            result = "success"
        except Exception as e:
            result = "error"
        response={'message':result}
        return jsonify(response)
#查询所有汇率
@app.route("/displayRate",methods=['POST'])
def displayRate():
    if request.method=="POST":
        tableDate=[]
        sql="SELECT * FROM deposit"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        for result in results:
            deposit_time = result[1]
            deposit_rate = result[2]
            response = {"deposit_time":deposit_time,"deposit_rate":deposit_rate}
            tableDate.append(response)
        sql="SELECT * FROM loan"
        lock.acquire()
        cursor.execute(sql)
        lock.release()
        results = cursor.fetchall()
        for result in results:
            loan_time = result[1]
            loan_rate = result[2]
            response = {"loan_time":loan_time,"loan_rate":loan_rate}
            tableDate.append(response)
        return jsonify(tableDate)
```

![]("点击并拖拽以移动")

前端代码

计算器的前端功能代码

```javascript
//选择定期
const Time = () => {
  time.value = true;
  current.value = false;
};
//选择活期
const Current = () => {
  time.value = false;
  current.value = true;
};
//选择修改利率
const Update = () => {
  update.value = true;
  rate.value = false;
  update_button.value = false;
  back_button.value = true;
  options.push({ value: "活期", label: "活期" });
};
//返回计算
const Back = () => {
  update.value = false;
  rate.value = true;
  update_button.value = true;
  back_button.value = false;
  options.length -= 1;
};
//计算存款利率
const CalculateDepositRate = () => {
  const formData = new FormData();

  formData.append("Money", deposit_money.value);
  if(time.value)
    formData.append("Time", value.value);
  else
    formData.append("Time", deposit_time.value);
  axios
    .post("http://127.0.0.1:5000/depositRate", formData)
    .then((response) => {
      deposit_interest.value=response.data
    })
    .catch((error) => {
      console.error("请求出错", error);
    });
};
//计算贷款利率
const CalculateLoanRate = () => {
  const formData = new FormData();
  formData.append("Money", loan_money.value);
  formData.append("Time", loan_time.value);
  axios
    .post("http://127.0.0.1:5000/loanRate", formData)
    .then((response) => {
      loan_interest.value=response.data
    })
    .catch((error) => {
      console.error("请求出错", error);
    });
};
//修改存款利率
const updateDepositRate = () => {
  const formData = new FormData();
  formData.append("Time", value.value);
  formData.append("Rate", deposit_rate_update.value);
  axios
    .post("http://127.0.0.1:5000/updateDepositRate", formData)
    .then((response)=>{
      console.log(response)
      getTableData()
      depositKey.value = Math.random()
    })
    .catch((error) => {
      console.error("请求出错", error);
    });
};
//修改贷款利率
const updateLoanRate = () => {
  const formData = new FormData();
  formData.append("Time", loan_value.value);
  formData.append("Rate", loan_rate_update.value);
  axios
    .post("http://127.0.0.1:5000/updateLoanRate", formData)
    .then((response)=>{
      console.log(response)
      getTableData()
      loanKey.value = Math.random()
    })
    .catch((error) => {
      console.error("请求出错", error);
    });

};
//获得利率表
const getTableData=()=>{
  axios
    .post("http://127.0.0.1:5000/displayRate")
    .then((response)=>{
      // const deposit:any = []
      depositRate.length = 0
      for(var i=0;i<=6;i++)
      {
        depositRate.push(response.data[i])
      }
      loanRate.length= 0
      for(var i=7;i<=11;i++)
      {
        loanRate.push(response.data[i])
      }
    })
    .catch((error) => {
      console.error("请求出错", error);
    });
}
```

![]("点击并拖拽以移动")

利率计算器的前端功能代码

```javascript
getANS() {
      this.check();
      this.append(this.activities[0]["result"]);
    },
    back() {
      length = this.numList.pop();
      this.equation = this.equation.substring(0, this.equation.length - length);
    },
    // Check if the character is + / - / × / ÷
    isOperator(character) {
      return ["+", "-", "x", "÷", "^"].indexOf(character) > -1;
    },
    // When pressed Operators or Numbers
    append(character) {
      // Start
      if (this.equation === "0" && !this.isOperator(character)) {
        if (character === ".") {
          this.equation += "" + character;
          this.numList.push(character.length);
          this.isDecimalAdded = true;
        } else {
          this.equation = "" + character;
          this.numList.push(character.length);
        }

        this.isStarted = true;
        return;
      }

      // If Number
      if (!this.isOperator(character)) {
        if (character === "." && this.isDecimalAdded) {
          return;
        }

        if (character === ".") {
          this.isDecimalAdded = true;
          this.isOperatorAdded = true;
        } else {
          this.isOperatorAdded = false;
        }

        this.equation += "" + character;
        this.numList.push(character.length);
      }

      // Added Operator
      if (this.isOperator(character) && !this.isOperatorAdded) {
        this.equation += "" + character;
        this.numList.push(character.length);
        this.isDecimalAdded = false;
        this.isOperatorAdded = true;
      }
    },
    // When pressed '='
    calculate() {
      this.numList.length = 0;
      const formData = new FormData();
      let expression = this.equation;
      if (expression != "0") {
        formData.append("expression", expression);
        axios
          .post("http://127.0.0.1:5000/calculator", formData)
          .then((response) => {
            this.equation = response.data.equation;
            this.numList.push(this.equation.length);
            this.check();
          })

          .catch((error) => {
            console.error("请求出错", error);
          });
        this.isDecimalAdded = false;
        this.isOperatorAdded = false;
      }
    },
    // When pressed '+/-'
    calculateToggle() {
      if (this.isOperatorAdded || !this.isStarted) {
        return;
      }

      this.equation = this.equation + "* -1";
      this.calculate();
    },
    // When pressed '%'
    calculatePercentage() {
      if (this.isOperatorAdded || !this.isStarted) {
        return;
      }

      this.equation = this.equation + "* 0.01";
      this.calculate();
    },
    // When pressed 'AC'
    clear() {
      this.equation = "0";
      this.isDecimalAdded = false;
      this.isOperatorAdded = false;
      this.isStarted = false;
    },
    //显示历史记录
    check() {
      axios
        .post("http://127.0.0.1:5000/query")
        .then((response) => {
          this.activities = response.data;
        })
        .catch((error) => {
          console.error("请求出错", error);
        });
    },
```

![]("点击并拖拽以移动")

## 心路历程和收获

这次的作业实现起来相较于上次有了更大的难度，上次要求可视化界面的实现利用了python自带的tkinter来实现较为简单，主要在于科学计算器功能的实现较难，而这次要求前后端分离，后端之前还有所了解，并且计算器的功能上次作业也写完了，写起来比较简单，但是前端的话之前了解不多，因此前端很多都是通过这次作业现学的，为了实现界面能够好看，参考了B站视频中拟态风的实现，由于自己是新手，因此在页面布局上的修改花了很多的时间，通过这次的学习，对前端的知识进行了一次学习，做出自己感觉还可以的界面也挺有成就感的

​
