<script setup>
import { ref, reactive } from 'vue'
import router from '../router'
import axios from 'axios'
import Cookies from 'js-cookie'

const FPath = 'http://127.0.0.1:5000/login'
const loginForm = reactive({
    username: '',
    password: ''
})

const login = () => {
    axios.post(FPath, loginForm)
        .then(res => {
            console.log("Response data:", res.data)
            if (res.data.login.startsWith('success')) {
                alert(`歡迎${res.data.usertype === '1' ? '管理員' : '登入'}`)
                Cookies.set('UserType', res.data.usertype)
                Cookies.set('username', loginForm.username)
                localStorage.setItem('userID', loginForm.username)
                router.push('/menu')
            } else {
                alert('登入失敗')
            }
        })
        .catch(error => {
            if (error.response) {
                // 伺服器返回了狀態碼，狀態碼不是 2xx
                console.error("Error response data:", error.response.data)
                console.error("Error response status:", error.response.status)
                console.error("Error response headers:", error.response.headers)
            } else if (error.request) {
                // 請求已發出，但沒有收到回應
                console.error("Error request data:", error.request)
            } else {
                // 在設置請求時發生了錯誤
                console.error("Error message:", error.message)
            }
            console.error("Error config:", error.config)
            alert('登入出現錯誤')
        })
}

const logout = () => {
    Cookies.remove('UserType')
    Cookies.remove('username')
    alert('已登出')
    router.push('/login')
}
</script>

<template>
    <div class="system_name">
        <h2>高雄大學學生校外住宿管理系統</h2>
        <h2>SOCAMS</h2>
    </div>

    <div class="login_page">
        <div id="container1">
            <div class="login">
                <h3 style="color: #409eff;">登入 Login</h3>
                <br>
                <el-form v-model="loginForm" ref="loginFormRef">
                    <el-form-item label="帳號" required>
                        <el-input v-model="loginForm.username" placeholder="請輸入帳號"></el-input>
                    </el-form-item>
                    <el-form-item label="密碼" required>
                        <el-input v-model="loginForm.password" placeholder="請輸入密碼" show-password></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="login" width>登入</el-button>
                    </el-form-item>
                </el-form>

                <el-button text type="primary" @click="router.push('/register')">房東註冊</el-button>
            </div><!-- login end-->
        </div><!-- container1 end-->
    </div><!-- login_page end-->
</template>

<style>
* {
    font-family: 微軟正黑體;
}

body {
    background-color: white;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
}

#username,
#password,
#fullname,
#comfirm_password,
#username2,
#password2 {
    width: 200px;
    height: 20px;
    margin: 10px;
    color: #409eff;
}

h5 {
    margin: 20px;
    color: #a3a2a3;
}

h5:hover {
    color: black;
}

#container1 {
    margin: 50px;
    padding: 10px;
    width: 350px;
    height: 350px;
    background-color: white;
    border-radius: 5px;
    border-top: 10px solid #409eff;
    box-shadow: 0 0px 70px rgba(0, 0, 0, 0.1);

    /*定位對齊*/
    position: relative;
    margin: auto;
    top: 100px;
    text-align:center;  
    justify-content: center;
}

.system_name {
    /*定位對齊*/
    position: relative;
    margin: auto;
    top: 100px;
    text-align: center;
}

input {
    padding: 5px;
    border: none;
    border: solid 1px #ccc;
    border-radius: 5px;
}

.el-form-item__content {
    justify-content: center;
}
</style>
