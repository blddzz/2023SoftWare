<template>
  <div class="common-layout">
    <el-container>
      <!-- <el-header>WE4K</el-header> -->
      <el-container>
        <el-aside width="400px">
          <form>
            <button class="red" type="button" @click="Send1()">
              <i class="icon ion-md-lock"></i> 科学计算器
            </button>
            <button class="red" type="button" @click="Send2()">
              <i class="icon ion-md-lock"></i> 利率计算器
            </button>
          </form>
        </el-aside>
        <el-main><component :is="tabComponent"></component></el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script >
import Caculator from "./components/Caculator.vue"
import Rate from "./components/Rate.vue"
export default {
  data() {
    return {
      tabComponent: Caculator
    };
  },
  components: {
    Caculator,
    Rate,
  },
  methods: {
    Send1(){
      this.tabComponent=Caculator
    },
    Send2(){
      this.tabComponent=Rate
    }
  },
};
</script>

<style >
body {
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #eee;
}
body, p, input, select, textarea, button {
  font-family: "Montserrat", sans-serif;
  letter-spacing: -0.2px;
  font-size: 16px;
}
div, p {
  color: #525665;
  text-shadow: 1px 1px 1px #FFF;
}
form {
  padding: 16px;
  width: 320px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.segment {
  padding: 32px 0;
  text-align: center;
}
button{
  border: 0;
 
  outline: 0;
  font-size: 16px;
  border-radius: 320px;
  padding: 16px;
  background-color: #EBECF0;
  text-shadow: 1px 1px 0 #FFF;
}
label {
  display: block;
  margin-bottom: 24px;
  width: 100%;
}

button {
  color: #61677C;
  font-weight: bold;
  box-shadow: -5px -5px 20px #FFF, 5px 5px 20px #BABECC;
  transition: all 0.2s ease-in-out;
  cursor: pointer;
  font-weight: 600;
}
button:hover {
  box-shadow: -2px -2px 5px #FFF, 2px 2px 5px #BABECC;
}
button:active {
  box-shadow: inset 1px 1px 2px #BABECC, inset -1px -1px 2px #FFF;
}
button .icon {
  margin-right: 8px;
}
button.unit {
  border-radius: 8px;
  line-height: 0;
  width: 48px;
  height: 48px;
  display: inline-flex;
  justify-content: center;
  align-items: center;
  margin: 0 8px;
  font-size: 19.2px;
}
button.unit .icon {
  margin-right: 0;
}
button.red {
  display: block;
  width: 100%;
  color: #999;
}
</style>

