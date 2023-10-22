<template>
    <div id="app">
    <div class="calculator">
      <div class="result" style="grid-area: result">
        {{ equation }}
      </div>
  
      <button style="grid-area: sin" @click="append(1)">sin</button>
      <button style="grid-area: ci" @click="append(1)">^</button>
      <button style="grid-area: ac" @click="clear">AC</button>
      <!-- <button style="grid-area: plus-minus" @click="calculateToggle">+/-</button> -->
      <button style="grid-area: percent" @click="calculatePercentage">%</button>
      <button style="grid-area: add" @click="append('+')">+</button>
      <button style="grid-area: subtract" @click="append('-')">-</button>
      <button style="grid-area: multiply" @click="append('×')">×</button>
      <button style="grid-area: divide" @click="append('÷')">÷</button>
      <button style="grid-area: equal" @click="calculate">=</button>
  
      <button style="grid-area: number-1" @click="append(1)">1</button>
      <button style="grid-area: number-2" @click="append(2)">2</button>
      <button style="grid-area: number-3" @click="append(3)">3</button>
      <button style="grid-area: number-4" @click="append(4)">4</button>
      <button style="grid-area: number-5" @click="append(5)">5</button>
      <button style="grid-area: number-6" @click="append(6)">6</button>
      <button style="grid-area: number-7" @click="append(7)">7</button>
      <button style="grid-area: number-8" @click="append(8)">8</button>
      <button style="grid-area: number-9" @click="append(9)">9</button>
      <button style="grid-area: number-0" @click="append(0)">0</button>
  
      <button style="grid-area: dot" @click="append('.')">.</button>
  
      
      <button style="grid-area: cos" @click="append(1)">cos</button>
      <button style="grid-area: tan" @click="append(1)">tan</button>
      <button style="grid-area: asin" @click="append(1)">asin</button>
      <button style="grid-area: acos" @click="append(1)">acos</button>
      <button style="grid-area: atan" @click="append(1)">atan</button>
  
      
      <button style="grid-area: sqrt" @click="append(1)">√</button>
      <button style="grid-area: jie" @click="append(1)">!</button>
      <button style="grid-area: ln" @click="append(1)">ln</button>
      <button style="grid-area: lg" @click="append(1)">lg</button>
      <button style="grid-area: pi" @click="append(1)">pi</button>
      <button style="grid-area: e" @click="append(1)">e</button>
      <button style="grid-area: le" @click="append(1)">(</button>
      <button style="grid-area: ri" @click="append(1)">)</button>
      <button style="grid-area: back" @click="append(1)">Back</button>
      
    </div>
    <div class="aside">
       <p class="font">历史记录</p> 
    </div>
  </div>
  </template>
  
  <style scoped>
  #app{
    display: flex;
    justify-content: center;
    gap: 50px;
  }
  .font{
    font-size: 24px;
    font-family: Helvetica;
    font-weight: normal;
    color: #999;
    margin: 0px;
  }
  .aside{
    
    width: 400px;
    height: 580px;
    min-width: 400px;
    display: flex;
    flex-direction: column;
    box-shadow: -8px -8px 16px -10px rgba(255, 255, 255, 1), 8px 8px 16px -10px rgba(0, 0, 0, .15);
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
      "sin jie ac ac back back"
      "cos sqrt le ri percent divide"
      "tan ci number-7 number-8 number-9 multiply"
      "asin ln number-4 number-5 number-6 subtract"
      "acos lg number-1 number-2 number-3 add"
      "atan pi e number-0 dot equal";
    grid-template-columns: repeat(6, var(--button-width));
    grid-template-rows: repeat(7, var(--button-height));
    
    
    box-shadow: -8px -8px 16px -10px rgba(255, 255, 255, 1), 8px 8px 16px -10px rgba(0, 0, 0, .15);
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
    background: linear-gradient(135deg, rgba(230, 230, 230, 1) 0%, rgba(246, 246, 246, 1) 100%);
    box-shadow: -4px -4px 10px -8px rgba(255, 255, 255, 1), 4px 4px 10px -8px rgba(0, 0, 0, .3);
  }
  
  .calculator button:active {
    box-shadow: -4px -4px 10px -8px rgba(255, 255, 255, 1) inset, 4px 4px 10px -8px rgba(0, 0, 0, .3) inset;
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
  
  <script>
  export default{
    data(){
      return{
        equation: '0',
      isDecimalAdded: false,
      isOperatorAdded: false,
      isStarted: false,
      } 
    },
    methods: {
      // Check if the character is + / - / × / ÷
      isOperator(character) {
        return ['+', '-', '×', '÷'].indexOf(character) > -1
      },
      // When pressed Operators or Numbers
      append(character) {
        // Start
        if (this.equation === '0' && !this.isOperator(character)) {
          if (character === '.') {
            this.equation += '' + character
            this.isDecimalAdded = true
          } else {
            this.equation = '' + character
          }
          
          this.isStarted = true
          return
        }
        
        // If Number
        if (!this.isOperator(character)) {
          if (character === '.' && this.isDecimalAdded) {
            return
          }
          
          if (character === '.') {
            this.isDecimalAdded = true
            this.isOperatorAdded = true
          } else {
            this.isOperatorAdded = false
          }
          
          this.equation += '' + character
        }
        
        // Added Operator
        if (this.isOperator(character) && !this.isOperatorAdded) {
          this.equation += '' + character
          this.isDecimalAdded = false
          this.isOperatorAdded = true
        }
      },
      // When pressed '='
      calculate() {
        let result = this.equation.replace(new RegExp('×', 'g'), '*').replace(new RegExp('÷', 'g'), '/')
        
        this.equation = parseFloat(eval(result).toFixed(9)).toString()
        this.isDecimalAdded = false
        this.isOperatorAdded = false
      },
      // When pressed '+/-'
      calculateToggle() {
        if (this.isOperatorAdded || !this.isStarted) {
          return
        }
        
        this.equation = this.equation + '* -1'
        this.calculate()
      },
      // When pressed '%'
      calculatePercentage() {
        if (this.isOperatorAdded || !this.isStarted) {
          return
        }
        
        this.equation = this.equation + '* 0.01'
        this.calculate()
      },
      // When pressed 'AC'
      clear() {
        this.equation = '0'
        this.isDecimalAdded = false
        this.isOperatorAdded = false
        this.isStarted = false
      }
    }
  }
  </script>