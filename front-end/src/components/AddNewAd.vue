<template>
    <div id="common-layout">
        <el-header id="header" style="display: flex;">
          <el-page-header @click="router.push('/RAS');">
            <template #content>
              <span class="text-large font-600 mr-3" style="color: white;"> 新增廣告 </span>
            </template>
          </el-page-header>
        </el-header>
    </div>
  
    <div>
      <el-container>
        <el-aside id="aside" width="200px"></el-aside>
          <el-main id="main">
            <form action="http://127.0.0.1:5000/receive_ad" method="POST">
                            <table>
                                <tr>
                                    <th colspan="8" class="center"><h1>新增房屋租賃廣告</h1></th>
                                </tr>
                                <tr>
                                    <th>標題：</th>
                                    <td colspan="7"><input type="text" class="underline-input" name="title"></td>
                                </tr>
                                <tr>
                                    <th>屋齡：</th>
                                    <td><input type="text" class="underline-input" name="age"></td>
                                </tr>
                                <tr>
                                    <th>房屋類型：</th>
                                    <td colspan="5">
                                        <div class="radio-group">
                                            <label><input type="radio" name="house_type" value="0"> 透天</label>
                                            <label><input type="radio" name="house_type" value="1"> 公寓</label>
                                            <label><input type="radio" name="house_type" value="2"> 大樓</label>
                                            <label><input type="radio" name="house_type" value="3"> 學舍</label>
                                            <label><input type="radio" name="house_type" value="4"> 其他</label>
                                        </div>
                                    </td>
                                </tr>
                                <tr>
                                    <th>房間類型：</th>
                                    <td colspan="3">
                                        <div class="radio-group">
                                            <label><input type="radio" name="room_type" value="0"> 套房</label>
                                            <label><input type="radio" name="room_type" value="1"> 雅房</label>
                                        </div>
                                    </td>
                                </tr>
                                <tr>
                                    <th>地址：</th>
                                    <td colspan="3"><input type="text" class="underline-input" name="address"></td>
                                </tr>
                                <tr>
                                    <th>限租條件：</th>
                                    <td colspan="7"><input type="text" class="underline-input" name="rental_conditions"></td>
                                </tr>
                                <tr>
                                    <th>租金：</th>
                                    <td><input type="text" class="underline-input" name="rent"></td>
                                </tr>
                                <tr>
                                    <th>聯絡人姓名：</th>
                                    <td><input type="text" class="underline-input" name="contact_name"></td>
                                    <th>聯絡人電話：</th>
                                    <td><input type="text" class="underline-input" name="contact_phone"></td>
                                </tr>
                                <tr>
                                    <th>開始刊登日(YYYY-MM-DD)：</th>
                                    <td><input type="date" class="underline-input" name="start_date"></td>
                                    <th>結束刊登日(YYYY-MM-DD)：</th>
                                    <td><input type="date" class="underline-input" name="end_date"></td>
                                </tr>
                                <tr>
                                    <th>廣告描述</th>
                                    <el-input
                                        v-model="textarea"
                                        style="width: 240px"
                                        :rows="2"
                                        type="textarea"
                                        name="description"
                                    />
                                </tr>
                                <tr>
                                    <th>廣告檔案連結：</th>
                                    <td colspan="7"><input type="text" class="underline-input" name="ad_file_link"></td>
                                </tr>
                            </table>
  
                          <div align="center">
                              <br>
                              <input type="reset" value="清除廣告內容" name="reset" class="styled-button">
                              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                              <input type="submit" value="提交廣告" name="submit" class="styled-button">
                          </div>
            </form>
          </el-main>
        </el-container>
    </div>
  </template>
  
  <script setup>
  
  import router from "../router/index.js";

  import { ref } from 'vue'
  const textarea = ref('')

  document.addEventListener('DOMContentLoaded', (event) => {
    const userID = localStorage.getItem('userID');
    if (userID) {
        document.getElementById('userID').value = userID;
    }
  });

  </script>
  
  <style>
          #common-layout .el-container {
              height: 100%;
              width: 100%;
          }
  
          #header {
              background-color: #409eff;
              color: white;
              line-height: 60px;
              --el-header-padding: 15px 20px;
          }
  
          #aside {
              background-color: #c3e1ff;
              color: #333;
              line-height: 200px;
          }
  
          .el-page-header__breadcrumb {
              margin-bottom: 0px;
          }
  
          .el-icon {
              padding-top: 0px;
          }
  
          body {
              background-color: white;
              margin: 0;
              font-family: 'Avenir', Helvetica, Arial, sans-serif;
          }
  
          table {
              width: 100%;
              border-collapse: collapse;
              margin-bottom: 20px;
              font-size: 20px;
              color: black;
          }
  
          th, td {
              padding: 8px;
              text-align: left;
          }
  
          .line {
              border-top:1.5px solid black;
              border-bottom:1.5px solid black;
          }
  
          .evaluate {
             border-bottom:1.5px dashed black;
          }
  
          .center {
              text-align: center;
          }
  
          .underline-input {
              text-align: center;
              border: none;
              border-bottom: 1px solid black;
              outline: none;
              width: 70%;
              font-size: 20px;
          }
  
          .radio-group {
              justify-content: space-around;
          }
  
          h1 {
              margin-top: 5px;
              margin-bottom: 5px;
          }
  
          .styled-button {
              background-color: white;
              border: 1px solid #c1c1c1;
              color: black;
              text-align: center;
              font-size: 18px;
              border-radius: 50px;
              padding: 7px 25px;
              cursor: pointer;
              transition: background-color 0.3s;
          }
  
          .styled-button:hover {
              color: #409eff;
              background-color: #c3e1ff;
          }
  </style>
  