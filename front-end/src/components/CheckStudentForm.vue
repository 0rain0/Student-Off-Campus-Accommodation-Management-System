<template>
    <div id="common-layout">
      <VSS_Header />
      <el-container>
        <VSS_Aside />
        <el-main id="main">
              <Form_S />
              <Form_T />
              <div align="center">
                <input type="reset" value="清除表單" name="reset" class="styled-button">
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <input type="submit" value="提交表單" name="submit" class="styled-button">
            </div>
        </el-main>
      </el-container>
    </div>
  </template>
  
  <script setup lang="ts">
import router from "../router/index.js";
import axios from 'axios'
</script>
  
  <style>
  @import "@/assets/VSS.css";
  </style>
  