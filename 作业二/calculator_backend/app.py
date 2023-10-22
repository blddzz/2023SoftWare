from flask import Flask,request,jsonify
import pymysql 
from flask_cors import CORS
from Calculation import *
import threading
lock = threading.Lock()

db = pymysql.connect(host="127.0.0.1",user="root",passwd="963.",database="caculator")
cursor = db.cursor()
print(type(db))
flag = False
app = Flask(__name__)
CORS(app,resources=r'/*')

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

def change(time):
    temp =time
    global flag
    flag =False
    if(temp=='三个月'):
        temp = 0.25
    elif(temp=='半年'):
        temp = 0.5
    elif(temp=='一年'):
        temp = 1.0
    elif (temp=='二年'):
        temp = 2.0
    elif (temp=='三年'):
        temp = 3.0
    elif (temp=='五年'):
        temp = 5.0
    else:
        flag=True
        temp = float(temp)
    return temp
def select(time):
    temp = time
    if(time<1):
        temp = "六个月"
    elif(time==1):
        temp = "一年"
    elif(time>1 and time<=3):
        temp = "一至三年"
    elif(time>3 and time<=5):
        temp = "三至五年"
    elif(time>=5):
        temp = "五年"
    return temp
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    db.close()
