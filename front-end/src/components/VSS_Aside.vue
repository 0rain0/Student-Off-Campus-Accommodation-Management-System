<script setup lang="ts">
import router from "../router/index.js";
import axios from 'axios'
</script>

<template>
    <link rel="stylesheet" href="./VSS.css">
    <el-aside id="aside" width="200px">
      <!-- 側邊 -->
      <el-menu default-active="1" class="el-menu-vertical-demo">
          <el-menu-item index="1" @click="visit_form_s">學生填寫</el-menu-item>
          <el-menu-item index="2" @click="CheckStudentStatus">查詢學生填寫狀況</el-menu-item>
          <el-menu-item index="3" @click="CheckClassStatus">查詢班級填寫狀況</el-menu-item>
      </el-menu>
    </el-aside>
</template>
  
<script lang="ts">
  export default {
    name: 'AsideMenu',
    methods: {
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