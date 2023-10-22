<template>
  <div class="app">
    <div class="rate" v-if="rate">
      <div class="deposit">
        <div class="title">存款</div>
        <!-- <el-dropdown :hide-on-click="false">
            <span class="el-dropdown-link" style="font-size: 16px;font-family: Montserrat, sans-serif;">
              存款方式<el-icon class="el-icon--right"><arrow-down /></el-icon>
            </span>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item>定期</el-dropdown-item>
                <el-dropdown-item>活期</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown> -->

        <div class="inputs">
          <label>金额</label>
          <!-- <input type="text" name="money" placeholder="输入存款金额" /> -->
          <el-input v-model="deposit_money" placeholder="输入存款金额" />
          <div class="special">
            <label>时间</label>
            <el-button color="#eee" plain @click="Time">定期</el-button>
            <el-button color="#eee" plain @click="Current">活期</el-button>
            <!-- <div @click="Time">定期</div>
            <div @click="Current">活期</div> -->
            <!-- <button @click="Time">定期</button>
            <button @click="Current">活期</button> -->
          </div>
          <el-input
            v-model="deposit_time"
            placeholder="输入存款时间/年"
            v-if="current"
          />
          <el-select
            v-model="value"
            class="m-2"
            placeholder="选择存款时间"
            v-if="time"
            
          >
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
          <!-- <input type="text" name="money" placeholder="输入存款时间" /> -->
        </div>
        <button type="submit" @click="CalculateDepositRate">计算</button>
        <div>利息为：{{ deposit_interest }}</div>
      </div>
      <div class="loan">
        <div class="title">贷款</div>
        <div class="inputs">
          <label>金额</label>
          <el-input v-model="loan_money" placeholder="输入贷款金额" />
          <!-- <input type="text" name="money" placeholder="输入贷款金额" /> -->
          <label>时间</label>
          <el-input v-model="loan_time" placeholder="输入贷款时间/年" />
          <!-- <input type="text" name="money" placeholder="输入贷款时间" /> -->
        </div>
        <button type="submit" @click="CalculateLoanRate">计算</button>
        <div>利息为：{{ loan_interest }}</div>
      </div>
    </div>
    <div class="update_rate" v-if="update">
      <div class="deposit">
        <div class="title">存款利率修改</div>
        <div class="inputs">
          <label>时间</label>
          <!-- <el-input
            v-model="deposit_time_update"
            placeholder="输入存款时间"
            v-if="current"
          /> -->

          <el-select v-model="value" class="m-2" placeholder="选择存款时间">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
          <label>利率</label>
          <el-input v-model="deposit_rate_update" placeholder="修改利率为" />
          <!-- <div class="special">
            <button @click="Time">定期</button>
            <button @click="Current">活期</button>
          </div> -->
        </div>
        <button type="submit" @click="updateDepositRate">修改</button>
      </div>
      <div class="loan">
        <div class="title">贷款利率修改</div>
        <div class="inputs">
          <label>时间</label>
          <!-- <el-input v-model="loan_time_update" placeholder="输入贷款时间" /> -->
          <el-select
            v-model="loan_value"
            class="m-2"
            placeholder="选择贷款时间"
            
            
          >
            <el-option
              v-for="item in loan_options"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
          <label>利率</label>
          <el-input v-model="loan_rate_update" placeholder="修改利率为" />
        </div>
        <button type="submit" @click="updateLoanRate">修改</button>
      </div>
    </div>
    <div class="rate_table">
      <div class="table">
        <el-table
        :data="depositRate"
        :key="depositKey"
        height="550"
        style="width: 100%; background-color: #eee"
        :header-cell-style="{ background: '#eef1f6', color: '#606266' }"
      >
        <el-table-column prop="deposit_time" label="存款时长" width="80" />
        <el-table-column prop="deposit_rate" label="存款利率" width="80" />
      </el-table>
      <el-table
        :data="loanRate"
        :key="loanKey"
        height="550"
        style="width: 100%; background-color: #eee"
        :header-cell-style="{ background: '#eef1f6', color: '#606266' }"
      >
        <el-table-column prop="loan_time" label="贷款时长" width="80" />
        <el-table-column prop="loan_rate" label="贷款利率" width="80" />
      </el-table>
      
      </div>
      <button @click="Update" v-if="update_button">修改利率</button>
      <button @click="Back" v-if="back_button">返回计算</button>
    </div>
  </div>
</template>
<style scoped>
.table{
  display: flex;
}
.deposit {
  display: flex;
  flex-direction: column;
  gap: 10px;
  height: 80%;
}
.loan {
  display: flex;
  flex-direction: column;
  gap: 10px;
  height: 80%;
}
.app {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 50px;
}
.rate {
  width: 480px;
  min-width: 480px;
  height: 583px;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: -8px -8px 16px -10px rgba(255, 255, 255, 1),
    8px 8px 16px -10px rgba(0, 0, 0, 0.15);
  padding: 24px;
  border-radius: 20px;
  gap: 20px;
}
.update_rate {
  width: 480px;
  min-width: 480px;
  height: 583px;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: -8px -8px 16px -10px rgba(255, 255, 255, 1),
    8px 8px 16px -10px rgba(0, 0, 0, 0.15);
  padding: 24px;
  border-radius: 20px;
  gap: 20px;
}
.rate_table {
  width: min-content;
  height: 583px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  box-shadow: -8px -8px 16px -10px rgba(255, 255, 255, 1),
    8px 8px 16px -10px rgba(0, 0, 0, 0.15);
  padding: 24px;
  border-radius: 20px;
  gap: 20px;
}
.title {
  font-size: 24px;
}
.inputs {
  text-align: left;
  display: flex;
  flex-direction: column;
  min-width: 202px;
  gap: 10px;
}
.special {
  display: flex;
  gap: 10px;
  min-height: 38px;
}
.special button {
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  font-weight: 500;
  letter-spacing: 2px;
  color: #5a84a2;
  font-size: 12px;
  border-radius: 60px;
  background-color: #eee;
  box-shadow: -2px -2px 8px rgba(255, 255, 255, 1),
    -2px -2px 12px rgba(255, 255, 255, 0.5),
    inset 2px 2px 4px rgba(255, 255, 255, 0.1), 2px 2px 8px rgba(0, 0, 0, 0.15);
}
label {
  display: block;
  width: 100%;
  padding: 0;
  border: none;
  outline: none;
  box-sizing: border-box;
}
label {
  margin-bottom: 4px;
  font-size: 16px;
}
label:nth-of-type(2) {
  margin-top: 14px;
}
/* input {
  margin-bottom: 15px;
  background: #eee;
  padding: 10px;
  padding-left: 20px;
  font-size: 14px;
  border-radius: 50px;
  height: 50px;
  box-shadow: -4px -4px 10px -8px rgba(255, 255, 255, 1) inset,
    4px 4px 10px -8px rgba(0, 0, 0, 0.3) inset;
} */

button {
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  font-weight: 500;
  letter-spacing: 2px;
  color: #5a84a2;
  font-size: 18px;
  border-radius: 60px;
  background-color: #eee;
  box-shadow: -2px -2px 8px rgba(255, 255, 255, 1),
    -2px -2px 12px rgba(255, 255, 255, 0.5),
    inset 2px 2px 4px rgba(255, 255, 255, 0.1), 2px 2px 8px rgba(0, 0, 0, 0.15);
}
button:active {
  box-shadow: inset -2px -2px 8px rgba(255, 255, 255, 1),
    inset -2px -2px 12px rgba(255, 255, 255, 0.5),
    inset 2px 2px 4px rgba(255, 255, 255, 0.1),
    inset 2px 2px 8px rgba(0, 0, 0, 0.15);
}
::v-deep .el-table__expanded-cell {
  background-color: transparent !important;
}

::v-deep .el-table th,
::v-deep .el-table tr,
::v-deep .el-table td {
  background-color: transparent;
}
</style>

<script lang="ts" setup>
import { rateEmits } from "element-plus";
import { flattedChildren } from "element-plus/es/utils";
import { onMounted, ref } from "vue";
import axios from "axios";
const depositKey = ref()
const loanKey = ref()
const deposit_interest = ref(0.0)
const loan_interest = ref(0.0)
const deposit_money = ref("");
const deposit_time = ref("");
const loan_money = ref("");
const loan_time = ref("");
const deposit_rate_update = ref("");
const loan_rate_update = ref("");
const time = ref(true);
const current = ref(false);
const update = ref(false);
const rate = ref(true);
const update_button = ref(true);
const back_button = ref(false);
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
const value = ref("");
const options = [
  {
    value: "三个月",
    label: "三个月",
  },
  {
    value: "半年",
    label: "半年",
  },
  {
    value: "一年",
    label: "一年",
  },
  {
    value: "二年",
    label: "二年",
  },
  {
    value: "三年",
    label: "三年",
  },
  {
    value: "五年",
    label: "五年",
  },
];
const loan_value = ref("");
const loan_options = [
  {
    value: "六个月",
    label: "六个月",
  },
  {
    value: "一年",
    label: "一年",
  },
  {
    value: "一至三年",
    label: "一至三年",
  },
  {
    value: "三至五年",
    label: "三至五年",
  },
  {
    value: "五年",
    label: "五年",
  },
];
let depositRate = [
  {
    deposit_time: "",
    deposit_rate: "",
  },
];
const loanRate = [
  {
    loan_time:"",
    loan_rate:""
  },
];
onMounted(()=>{
  getTableData()
})
</script>