<template>
    <center>
        <div>
            <img src="../assets/NUK_logo.svg" alt="logo" style="width: 200px; height: 200px;">
            <h1>NUK SOCAMS</h1>
            <h1>高雄大學學生校外住宿管理系統</h1>
        </div>
        <div>
            <h1>登入 Login</h1>
            <el-form :model="loginForm" :rules="loginRules" ref="loginForm" label-width="80px" class="demo-ruleForm">
                <el-form-item label="帳號" prop="username">
                    <el-input v-model="loginForm.username" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="密碼" prop="password">
                    <el-input type="password" v-model="loginForm.password" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="login">登入</el-button>
                    <el-button @click="resetForm('loginForm')">重置</el-button>
                </el-form-item>
            </el-form>
    </center>
</template>