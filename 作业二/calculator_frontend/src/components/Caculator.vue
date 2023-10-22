<template>
  <div id="app">
    <div class="calculator">
      <div class="result" style="grid-area: result">
        {{ equation }}
      </div>

      <button style="grid-area: sin" @click="append('sin(')">sin</button>
      <button style="grid-area: ci" @click="append('^')">^</button>
      <button style="grid-area: ac" @click="clear">AC</button>
      <!-- <button style="grid-area: plus-minus" @click="calculateToggle">+/-</button> -->
      <button style="grid-area: percent" @click="calculatePercentage">%</button>
      <button style="grid-area: add" @click="append('+')">+</button>
      <button style="grid-area: subtract" @click="append('-')">-</button>
      <button style="grid-area: multiply" @click="append('x')">×</button>
      <button style="grid-area: divide" @click="append('÷')">÷</button>
      <button style="grid-area: equal" @click="calculate">=</button>

      <button style="grid-area: number-1" @click="append('1')">1</button>
      <button style="grid-area: number-2" @click="append('2')">2</button>
      <button style="grid-area: number-3" @click="append('3')">3</button>
      <button style="grid-area: number-4" @click="append('4')">4</button>
      <button style="grid-area: number-5" @click="append('5')">5</button>
      <button style="grid-area: number-6" @click="append('6')">6</button>
      <button style="grid-area: number-7" @click="append('7')">7</button>
      <button style="grid-area: number-8" @click="append('8')">8</button>
      <button style="grid-area: number-9" @click="append('9')">9</button>
      <button style="grid-area: number-0" @click="append('0')">0</button>

      <button style="grid-area: dot" @click="append('.')">.</button>

      <button style="grid-area: cos" @click="append('cos(')">cos</button>
      <button style="grid-area: tan" @click="append('tan(')">tan</button>
      <button style="grid-area: asin" @click="append('asin(')">asin</button>
      <button style="grid-area: acos" @click="append('acos(')">acos</button>
      <button style="grid-area: atan" @click="append('atan(')">atan</button>

      <button style="grid-area: sqrt" @click="append('√')">√</button>
      <button style="grid-area: jie" @click="append('!')">!</button>
      <button style="grid-area: ln" @click="append('ln(')">ln</button>
      <button style="grid-area: lg" @click="append('lg(')">lg</button>
      <button style="grid-area: pi" @click="append('π')">π</button>
      <button style="grid-area: e" @click="append('e')">e</button>
      <button style="grid-area: le" @click="append('(')">(</button>
      <button style="grid-area: ri" @click="append(')')">)</button>
      <button style="grid-area: back" @click="back">Back</button>
      <button style="grid-area: ans" @click="getANS">ANS</button>
    </div>
    <div class="aside">
      <p class="font">历史记录</p>
      <el-timeline>
        <el-timeline-item
          v-for="(activity, index) in activities"
          :key="index"
          color="#8c8f97"
        > 
          {{ activity.expression }}{{ activity.result }}
        </el-timeline-item>
      </el-timeline>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      equation: "0",
      isDecimalAdded: false,
      isOperatorAdded: false,
      isStarted: false,
      activities: [{ expression: "", result: "" }],
      numList: [],
    };
  },
  mounted() {
    this.check();
  },
  methods: {
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
  },
};
</script>

<style scoped>
#app {
  display: flex;
  justify-content: center;
  gap: 50px;
}
.font {
  font-size: 24px;
  font-family: Helvetica;
  font-weight: normal;
  padding-bottom: 30px;
  color: #424141;
  margin: 0px;
}
.aside {
  width: 400px;
  height: 580px;
  min-width: 400px;
  display: flex;
  flex-direction: column;
  box-shadow: -8px -8px 16px -10px rgba(255, 255, 255, 1),
    8px 8px 16px -10px rgba(0, 0, 0, 0.15);
  padding: 12px;
  border-radius: 20px;
}
.calculator {
  --button-width: 80px;
  --button-height: 80px;
  width: min-content;
  height: fit-content;
  display: grid;
  grid-template-areas:
    "result result result result result result"
    "sin jie ans ac back back"
    "cos sqrt le ri percent divide"
    "tan ci number-7 number-8 number-9 multiply"
    "asin ln number-4 number-5 number-6 subtract"
    "acos lg number-1 number-2 number-3 add"
    "atan pi e number-0 dot equal";
  grid-template-columns: repeat(6, var(--button-width));
  grid-template-rows: repeat(7, var(--button-height));

  box-shadow: -8px -8px 16px -10px rgba(255, 255, 255, 1),
    8px 8px 16px -10px rgba(0, 0, 0, 0.15);
  padding: 24px;
  border-radius: 20px;
}

.calculator button {
  margin: 8px;
  padding: 0;
  border: 0;
  display: block;
  outline: none;
  border-radius: calc(var(--button-height) / 2);
  font-size: 24px;
  font-family: Helvetica;
  font-weight: normal;
  color: #999;
  background: linear-gradient(
    135deg,
    rgba(230, 230, 230, 1) 0%,
    rgba(246, 246, 246, 1) 100%
  );
  box-shadow: -4px -4px 10px -8px rgba(255, 255, 255, 1),
    4px 4px 10px -8px rgba(0, 0, 0, 0.3);
}

.calculator button:active {
  box-shadow: -4px -4px 10px -8px rgba(255, 255, 255, 1) inset,
    4px 4px 10px -8px rgba(0, 0, 0, 0.3) inset;
}

.result {
  text-align: right;
  line-height: var(--button-height);
  font-size: 48px;
  font-family: Helvetica;
  padding: 0 20px;
  color: #666;
}
</style>