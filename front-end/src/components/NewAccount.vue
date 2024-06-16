<template>
    <div id="common-layout">
        <el-container>
            <el-header id="header">
                <el-page-header @click="manageAccounts">
                    <template #content>
                        <span class="text-large font-600 mr-3" style="color: white;"> 系統管理 </span>
                    </template>
                </el-page-header>
            </el-header>
            <el-container>
                <el-aside id="aside" width="200px">
                    <el-menu default-active="1" class="el-menu-vertical-demo" @select="handleSelect">
                        <el-menu-item index="1">帳號管理</el-menu-item>
                        <el-menu-item index="2">班級管理</el-menu-item>
                    </el-menu>
                </el-aside>
                <el-main id="main">

                    <div style="text-align: center;">
                        <el-button type="primary" @click="addLargeNumberOfAccounts">新增大量帳號</el-button>
                        <h1 style="color: black;">新增帳號</h1>
                    </div>

                    <!-- 表单开始 -->
                    <el-form label-width="100px">
                        <el-form-item label="帳號">
                            <el-input v-model="newAccount.account" placeholder="請輸入帳號" maxlength="15"></el-input>
                        </el-form-item>
                        <el-form-item label="密碼">
                            <el-input v-model="newAccount.password" placeholder="請輸入密碼" maxlength="15"></el-input>
                        </el-form-item>
                        <el-form-item label="姓名">
                            <el-input v-model="newAccount.name" placeholder="請輸入姓名" maxlength="15"></el-input>
                        </el-form-item>
                        <el-form-item label="電子信箱">
                            <el-input v-model="newAccount.email" placeholder="請輸入電子信箱" maxlength="30"></el-input>
                        </el-form-item>

                        <el-form-item label="權限">
                            <el-select v-model="newAccount.permission" placeholder="請選擇權限">
                                <el-option label="管理員" value="管理員"></el-option>
                                <el-option label="房東" value="房東"></el-option>
                                <el-option label="學生" value="學生"></el-option>
                                <el-option label="老師" value="老師"></el-option>
                            </el-select>
                        </el-form-item>

                        <!-- 根据权限显示不同的表单项 -->
                        <!-- 房東 -->
                        <el-form-item v-if="newAccount.permission === '房東'">
                            <el-form-item label="電話">
                                <el-input v-model="newAccount.phone" placeholder="請輸入電話" maxlength="15"></el-input>
                            </el-form-item>
                        </el-form-item>

                        <!-- 學生 -->
                        <el-form-item v-if="newAccount.permission === '學生'">
                            <el-form-item label="電話">
                                <el-input v-model="newAccount.phone" placeholder="請輸入電話" maxlength="15"></el-input>
                            </el-form-item>
                            <el-form-item label="年級">
                                <el-select v-model="newAccount.Grade" placeholder="請選擇年級" class="select-class">
                                    <el-option label="1" value="1"></el-option>
                                    <el-option label="2" value="2"></el-option>
                                    <el-option label="3" value="3"></el-option>
                                    <el-option label="4" value="4"></el-option>
                                    <el-option label="5" value="5"></el-option>
                                    <el-option label="6" value="6"></el-option>
                                    <el-option label="7" value="7"></el-option>
                                    <el-option label="8" value="8"></el-option>
                                    <el-option label="9" value="9"></el-option>
                                </el-select>
                            </el-form-item>
                            <el-form-item label="性別">
                                <el-select v-model="newAccount.Gender" placeholder="請選擇性別" class="select-class">
                                    <el-option label="男" value="0"></el-option>
                                    <el-option label="女" value="1"></el-option>
                                    <el-option label="其他" value="2"></el-option>
                                </el-select>
                            </el-form-item>
                        </el-form-item>
                        <el-form-item v-if="newAccount.permission === '學生'">
                            <el-form-item label="家中地址">
                                <el-input v-model="newAccount.Address" placeholder="請輸入家中地址" maxlength="30"></el-input>
                            </el-form-item>
                            <el-form-item label="家中電話">
                                <el-input v-model="newAccount.HomeTel" placeholder="請輸入家中電話" maxlength="15"></el-input>
                            </el-form-item>
                            <el-form-item label="聯絡人姓名">
                                <el-input v-model="newAccount.ContactName" placeholder="請輸入聯絡人姓名"
                                    maxlength="15"></el-input>
                            </el-form-item>
                            <el-form-item label="聯絡人電話">
                                <el-input v-model="newAccount.ConTel" placeholder="請輸入聯絡人電話" maxlength="15"></el-input>
                            </el-form-item>
                        </el-form-item>

                        <!-- 老師 -->
                        <el-form-item v-if="newAccount.permission === '老師'">
                            <el-form-item label="電話">
                                <el-input v-model="newAccount.phone" placeholder="請輸入電話" maxlength="15"></el-input>
                            </el-form-item>
                            <el-form-item label="職級">
                                <el-select v-model="newAccount.Rank" placeholder="請選擇職級" class="select-class">
                                    <el-option label="教授" value="0"></el-option>
                                    <el-option label="副教授" value="1"></el-option>
                                    <el-option label="助理教授" value="2"></el-option>
                                </el-select>
                            </el-form-item>
                            <el-form-item label="辦公室位址">
                                <el-input v-model="newAccount.OfficeAddr" placeholder="請輸入辦公室位址"
                                    maxlength="30"></el-input>
                            </el-form-item>
                            <el-form-item label="辦公室電話">
                                <el-input v-model="newAccount.OfficeTel" placeholder="請輸入辦公室電話"
                                    maxlength="15"></el-input>
                            </el-form-item>
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
    // 通用資料
    account: string
    password: string
    permission: string
    name: string
    phone: string
    email: string

    // 學生
    Grade: string
    Gender: string
    Address: string
    HomeTel: string
    ContactName: string
    ConTel: string

    // 老師
    Rank: string
    OfficeAddr: string
    OfficeTel: string
}

export default {
    setup() {
        const newAccount = ref<Account>({
            // 通用資料
            account: '',
            password: '',
            permission: '',
            name: '',
            phone: '',
            email: '',

            // 學生
            Grade: '',
            Gender: '',
            Class: '',
            Address: '',
            HomeTel: '',
            ContactName: '',
            ConTel: '',

            // 老師
            Rank: '',
            OfficeAddr: '',
            OfficeTel: ''
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
                    resetForm();
                    manageAccounts();
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
                // 通用資料
                account: '',
                password: '',
                permission: '',
                name: '',
                phone: '',
                email: '',

                // 學生
                Grade: '',
                Gender: '',
                Class: '',
                Address: '',
                HomeTel: '',
                ContactName: '',
                ConTel: '',

                // 老師
                Rank: '',
                OfficeAddr: '',
                OfficeTel: ''
            }
        }
        const handleSelect = (index: string) => {
            if (index === '1') {
                manageAccounts()
            } else if (index === '2') {
                manageClasses()
            }
        }
        return {
            handleSelect,
            newAccount,
            addLargeNumberOfAccounts,
            manageAccounts,
            manageClasses,
            submitForm
        }
    }

}



</script>

<style>
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

.select-class {
    width: 150px;
}
</style>
