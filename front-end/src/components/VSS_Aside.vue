<script setup lang="ts">
import router from "../router/index.js";
import axios from 'axios'
</script>

<template>
    <link rel="stylesheet" href="./VSS.css">
    <el-aside id="aside" width="200px">
      <!-- 側邊 -->
      <el-menu default-active="1" class="el-menu-vertical-demo" @select="handleSelect">
        <el-button class="aside-button" @click="visit_form_s">學生填寫</el-button>
        <el-button class="aside-button" @click="CheckStudentStatus">查詢學生填寫狀況</el-button>
        <el-button class="aside-button" @click="CheckClassStatus">查詢班級填寫狀況</el-button>
      </el-menu>
    </el-aside>
</template>
  
<script lang="ts">
  export default {
    name: 'AsideMenu',
    methods: {
      handleSelect(selectedKey) {
        // 處理選擇事件
      },
      visit_form_s() {
        router.push('/EditRentalSurveyForm_S');
      },
      CheckStudentStatus() {
        router.push('/CheckStudentStatus');
      },
      CheckClassStatus() {
        router.push('/CheckClassStatus');
      }
    }
  }
</script>
