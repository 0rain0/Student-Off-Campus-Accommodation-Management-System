<script setup lang="ts">
import router from "../router/index.js";
import axios from 'axios'
import {ref, onMounted} from 'vue'
import Cookies from 'js-cookie'
const userType = ref(null)
const userNames = ref(null)
onMounted(() => {
  userType.value = Cookies.get('UserType')
  userNames.value = Cookies.get('username')
})

</script>
<template>
    <el-aside id="aside" width="200px">
      <el-menu default-active="1" class="el-menu-vertical-demo">

          <el-menu-item index="1" v-if="userType === '4'" @click="visit_form_s">學生填寫</el-menu-item>
          <el-menu-item index="2" v-if="userType === '1'|| userType === '3'"@click="CheckStudentStatus">查詢學生填寫狀況</el-menu-item>

          <el-menu-item index="3" v-if="userType === '1'"  @click="CheckClassStatus">查詢班級填寫狀況</el-menu-item>
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
<style>
@import "@/assets/VSS.css";
</style>