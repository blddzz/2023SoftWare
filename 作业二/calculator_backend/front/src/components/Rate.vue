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
          <el-input v-model="input" placeholder="输入存款金额" />
          <div class="special"><label>时间</label>
            <el-button color="#eee"  plain @click="Time">定期</el-button>
            <el-button color="#eee"  plain @click="Current">活期</el-button>
            <!-- <div @click="Time">定期</div>
            <div @click="Current">活期</div> -->
            <!-- <button @click="Time">定期</button>
            <button @click="Current">活期</button> -->
          </div>
          <el-input v-model="input" placeholder="输入存款时间" v-if="current" />
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
        <button type="submit">计算</button>
      </div>
      <div class="loan">
        <div class="title">贷款</div>
        <div class="inputs">
          <label>金额</label>
          <el-input v-model="input" placeholder="输入贷款金额" />
          <!-- <input type="text" name="money" placeholder="输入贷款金额" /> -->
          <label>时间</label>
          <el-input v-model="input" placeholder="输入贷款时间" />
          <!-- <input type="text" name="money" placeholder="输入贷款时间" /> -->
        </div>
        <button type="submit">计算</button>
      </div>
    </div>
    <div class="update_rate" v-if="update">
      <div class="deposit">
        <div class="title">存款利率修改</div>
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
          
          <label>时间</label>
          <el-input v-model="input" placeholder="输入存款时间" v-if="current" />
          
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
          <label>利率</label>
          <el-input v-model="input" placeholder="修改利率为" />
          <div class="special">
            <button @click="Time">定期</button>
            <button @click="Current">活期</button>
          </div>
        </div>
        <button type="submit">修改</button>
      </div>
      <div class="loan">
        <div class="title">贷款利率修改</div>
        <div class="inputs">
          
          <label>时间</label>
          <el-input v-model="input" placeholder="输入贷款时间" />
          <label>利率</label>
          <el-input v-model="input" placeholder="修改利率为" />
        </div>
        <button type="submit">修改</button>
      </div>
      
    </div>
    <div class="rate_table">
      <el-table :data="tableData" height="550" style="width: 100%;background-color: #eee;" :header-cell-style="{background:'#eef1f6',color:'#606266'}">
        <el-table-column prop="date" label="Date" width="180" />
        <el-table-column prop="name" label="Name" width="180" />
        <el-table-column prop="address" label="Address" />
      </el-table>
      <button @click="Update" v-if="update_button">修改利率</button>
      <button @click="Back" v-if="back_button">返回计算</button>
    </div>
    
  </div>
</template>
<style scoped>
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
.update_rate{
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
.rate_table{
  width: 480px;
  min-width: 480px;
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
import { ref } from "vue";
const input = ref("");
const time = ref(true);
const current = ref(false);
const update = ref(false);
const rate = ref(true);
const update_button = ref(true)
const back_button = ref(false)
const Time = () => {
  time.value = true;
  current.value = false;
};
const Current = () => {
  time.value = false;
  current.value = true;
};
const Update=()=>{
  update.value=true
  rate.value=false
  update_button.value=false
  back_button.value=true
}
const Back=()=>{
  update.value=false
  rate.value=true
  update_button.value=true
  back_button.value=false
}

const value = ref("");

const options = [
  {
    value: "Option1",
    label: "Option1",
  },
  {
    value: "Option2",
    label: "Option2",
  },
  {
    value: "Option3",
    label: "Option3",
  },
  {
    value: "Option4",
    label: "Option4",
  },
  {
    value: "Option5",
    label: "Option5",
  },
];
const tableData = [
  {
    date: '2016-05-03',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-02',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-04',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-01',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-08',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-06',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-07',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
]
</script>