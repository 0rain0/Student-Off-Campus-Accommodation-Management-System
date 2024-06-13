<template>
    <div class="register-page">
      <div class="system_name">
        <h2>高雄大學學生校外住宿管理系統</h2>
        <h2>SOCAMS</h2>
      </div>
  
      <div id="container">
        <div class="register">
          <h3 style="color: #409eff;">房東註冊</h3>
          <br>
          <el-form :model="registerForm" ref="registerFormRef" label-width="100px">
            <el-form-item label="帳號" required>
              <el-input v-model="registerForm.account" placeholder="請輸入帳號"></el-input>
            </el-form-item>
            <el-form-item label="姓名" required>
              <el-input v-model="registerForm.name" placeholder="請輸入姓名"></el-input>
            </el-form-item>
            <el-form-item label="電子郵件" required>
              <el-input v-model="registerForm.email" placeholder="請輸入電子郵件"></el-input>
            </el-form-item>
            <el-form-item label="電話" required>
              <el-input v-model="registerForm.tel" placeholder="請輸入電話"></el-input>
            </el-form-item>
            <el-form-item label="密碼" required>
              <el-input type="password" v-model="registerForm.password" placeholder="請輸入密碼"></el-input>
            </el-form-item>
            <el-form-item label="確認密碼" required>
              <el-input type="password" v-model="registerForm.confirmPassword" placeholder="請再次輸入密碼"></el-input>
            </el-form-item>
            <div class="button-container">
              <el-button type="primary" @click="register">註冊</el-button>
              <el-button text type="primary" @click="goToLogin">返回登入</el-button>
            </div>
          </el-form>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { reactive } from 'vue'
  import { useRouter } from 'vue-router'
  import axios from 'axios'
  
  const router = useRouter()
  const FPath = 'http://127.0.0.1:5000/register'
  
  const registerForm = reactive({
    account: '',
    name: '',
    email: '',
    tel: '',
    password: '',
    confirmPassword: ''
  })
  
  const register = () => {
    if (registerForm.password !== registerForm.confirmPassword) {
      alert('密碼和確認密碼不一致')
      return
    }
  
    axios.post(FPath, registerForm)
      .then(res => {
        console.log('Response data:', res.data)
        if (res.data.register === 'success') {
          alert('註冊成功')
          router.push('/login')
        } else {
          alert('註冊失敗')
        }
      })
      .catch(error => {
        if (error.response) {
          console.error('Error response data:', error.response.data)
          console.error('Error response status:', error.response.status)
          console.error('Error response headers:', error.response.headers)
        } else if (error.request) {
          console.error('Error request data:', error.request)
        } else {
          console.error('Error message:', error.message)
        }
        console.error('Error config:', error.config)
        alert('註冊出現錯誤')
      })
  }
  
  const goToLogin = () => {
    router.push('/login')
  }
  </script>
  
  <style>
  * {
    font-family: 微軟正黑體;
  }
  
  body {
    background-color: white;
  }
  
  #container {
    margin: 50px;
    padding: 10px;
    width: 350px;
    background-color: white;
    border-radius: 5px;
    border-top: 10px solid #409eff;
    box-shadow: 0 0px 70px rgba(0, 0, 0, 0.1);
    text-align: center;
    justify-content: center;
    position: relative;
    margin: auto;
    top: 100px;
  }
  
  .system_name {
    position: relative;
    margin: auto;
    top: 100px;
    text-align: center;
  }

.button-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}

.button-container .el-button {
  margin-bottom: 10px;
}
  </style>
  