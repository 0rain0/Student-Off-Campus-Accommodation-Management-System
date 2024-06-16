<template>
    <div id="common-layout">
        <el-container>
            <el-header id="header">
                <el-page-header @click="router.push('/menu');">
                    <template #content>
                        <span class="text-large font-600 mr-3" style="color: white;"> 系統管理 </span>
                    </template>
                </el-page-header>
            </el-header>
            <el-container>
                <el-aside id="aside" width="200px">
                    <el-button class="aside-button" @click="manageAccounts">帳號管理</el-button>
                    <el-button class="aside-button" @click="manageClasses">班級管理</el-button>
                </el-aside>
                <el-main id="main">
                    
                    <div style="text-align: center;">
                        <el-button type="primary" @click="addLargeNumberOfAccounts">新增大量帳號</el-button>
                        <h1 style="color: black;">新增帳號</h1>
                    </div>
                    
                    <!-- 表单开始 -->
                <el-form label-width="100px">
                    <el-form-item label="帳號">
                        <el-input v-model="newAccount.account" placeholder="請輸入帳號"></el-input>
                    </el-form-item>
                    <el-form-item label="密碼">
                        <el-input v-model="newAccount.password" placeholder="請輸入密碼"></el-input>
                    </el-form-item>
                    <el-form-item label="權限">
                        <el-select v-model="newAccount.permission" placeholder="請選擇權限">
                            <el-option label="管理員" value="管理員"></el-option>
                            <el-option label="房東" value="房東"></el-option>
                            <el-option label="學生" value="學生"></el-option>
                            <el-option label="老師" value="老師"></el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item v-if="newAccount.permission !== '管理員'">
                        <el-form-item label="電話">
                            <el-input v-model="newAccount.phone" placeholder="請輸入電話"></el-input>
                        </el-form-item>
                    </el-form-item>
                    <!-- 根据权限显示不同的表单项 -->
                    <el-form-item v-if="newAccount.permission === '學生'">
                        <el-form-item label="老師ID">
                            <el-input v-model="newAccount.Teacher" placeholder="請輸入老師ID"></el-input>
                        </el-form-item>
                        <el-form-item label="班級ID">
                            <el-input v-model="newAccount.Class" placeholder="請輸入班級ID"></el-input>
                        </el-form-item>
                    </el-form-item>
                    <el-form-item label="姓名">
                        <el-input v-model="newAccount.name" placeholder="請輸入姓名"></el-input>
                    </el-form-item>
                    <el-form-item label="電子信箱">
                        <el-input v-model="newAccount.email" placeholder="請輸入電子信箱"></el-input>
                    </el-form-item>
                    
                    <el-form-item>
                        <el-button type="primary" @click="submitForm">確認新增</el-button>
                    </el-form-item>
                </el-form>
                <!-- 表单结束 -->
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<script lang="ts">
import { ref } from 'vue'
import router from '../router'
import axios from 'axios'

interface Account {
    account: string
    password: string
    permission: string
    name: string
    phone: string
    email: string

    Teacher: string
    Class: string
}

export default {
    setup() {
        const newAccount = ref<Account>({
            account: '',
            password: '',
            permission: '',
            name: '',
            phone: '',
            email: '',
            Teacher: '',
            Class: ''
        })

        const addLargeNumberOfAccounts = () => {
            console.log('Add large number of account clicked')
            router.push('/AddLargeAccount')
        }

        const manageAccounts = () => {
            console.log('Manage accounts clicked')
            router.push('/AccountManage')
        }

        const manageClasses = () => {
            console.log('Manage classes clicked')
            router.push('/ClassManage')
        }

        const submitForm = async () => {
            // 向服务器提交新帐号的信息
            try {
                const response = await axios.post('http://127.0.0.1:5000/api/accounts/new', newAccount.value)
                if (response.data.status === 'success') {
                    ElMessage({
                        message: response.data.message,
                        type: 'success',
                    });
                    resetForm()
                } else {
                    ElMessage({
                        message: response.data.message,
                        type: 'error',
                    });
                    console.error('Failed to new account:', response.data.message);
                }
            } catch (error) {
                console.error('Error creating account:', error)
            }
        }

        const resetForm = () => {
            // 重置表单数据
            newAccount.value = {
                account: '',
                password: '',
                permission: '',
                name: '',
                phone: '',
                email: '',
                Teacher: '',
                Class: ''
            }
        }

        return {
            newAccount,
            addLargeNumberOfAccounts,
            manageAccounts,
            manageClasses,
            submitForm
        }
    }
}
</script>

<style scoped>
#common-layout .el-container {
    height: 100vh;
    width: 100%;
}

#header {
    background-color: #409eff;
    color: #fff;
    line-height: 60px;
    display: flex;
    align-items: center;
    padding: 0 20px;
}

#aside {
    background-color: #c3e1ff;
    color: #333;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
}

.aside-button {
    width: 100%;
    margin-bottom: 10px;
    box-sizing: border-box;
    text-align: center;
}

.el-page-header__breadcrumb {
    margin-bottom: 0px;
}

.el-icon {
    padding-top: 0px;
}

body {
    margin: 0;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
}

.pagination {
    margin-top: 20px;
}
</style>
