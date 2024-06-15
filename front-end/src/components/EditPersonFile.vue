<template>
    <div id="common-layout">
        <el-container>
            <el-header id="header">
                <el-page-header @click="router.push('/menu');">
                    <template #content>
                        <span class="text-large font-600 mr-3" style="color: white;"> 修改個人資料 </span>
                    </template>
                </el-page-header>
            </el-header>
            <el-container>
                <el-aside id="aside" width="200px"></el-aside>
                <el-main id="main">
                    <div class="login_page" v-if="!isVerified">
                        <div id="container1">
                            <div class="login">
                                <h3 style="color: #409eff;">身分驗證</h3>
                                <br>
                                <el-form v-model="loginForm" ref="loginFormRef">
                                    <el-form-item label="帳號" required>
                                        <el-input v-model="loginForm.account" placeholder="請輸入帳號"></el-input>
                                    </el-form-item>
                                    <el-form-item label="密碼" required>
                                        <el-input v-model="loginForm.password" placeholder="請輸入密碼" show-password></el-input>
                                    </el-form-item>
                                    <el-form-item>
                                        <el-button type="primary" @click="login" width>驗證</el-button>
                                    </el-form-item>
                                </el-form>
                            </div><!-- login end-->
                        </div><!-- container1 end-->
                    </div><!-- login_page end-->

                    <div class="edit_page" v-else>
                        <h3 style="color: #409eff;">編輯個人資料</h3>
                        <br>
                        <el-form v-model="editForm" ref="editFormRef">
                            <el-form-item label="帳號:">
                                <span class="readonly-text">{{ editForm.account }}</span>
                            </el-form-item>
                            <el-form-item label="權限:">
                                <span class="readonly-text">{{ editForm.permission }}</span>
                            </el-form-item>
                            <el-form-item label="密碼:" required>
                                <el-input v-model="editForm.password" placeholder="請輸入密碼" maxlength="15"></el-input>
                            </el-form-item>
                            <el-form-item label="姓名:" required>
                                <el-input v-model="editForm.name" placeholder="請輸入姓名" maxlength="15"></el-input>
                            </el-form-item>
                            <el-form-item label="電子信箱:" required>
                                <el-input v-model="editForm.email" placeholder="請輸入電子信箱" maxlength="30"></el-input>
                            </el-form-item>
                            <!-- 根据权限显示不同的表单项 -->
                            <!-- 房東 -->
                            <el-form-item v-if="editForm.permission === '房東'">
                                <el-form-item label="電話" required>
                                    <el-input v-model="editForm.Tel" placeholder="請輸入電話" maxlength="15"></el-input>
                                </el-form-item>
                            </el-form-item>

                            <!-- 學生 -->
                            <el-form-item v-if="editForm.permission === '學生'">
                                <el-form-item label="電話" required>
                                    <el-input v-model="editForm.Tel" placeholder="請輸入電話" maxlength="15"></el-input>
                                </el-form-item>
                            </el-form-item>
                            <el-form-item v-if="editForm.permission === '學生'">
                                <el-form-item label="年級" required>
                                    <el-select v-model="editForm.Grade" placeholder="請選擇年級" class="select-class">
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
                            </el-form-item>
                            <el-form-item v-if="editForm.permission === '學生'">
                                <el-form-item label="性別" required>
                                    <el-select v-model="editForm.Gender" placeholder="請選擇性別" class="select-class">
                                        <el-option label="男" value="0"></el-option>
                                        <el-option label="女" value="1"></el-option>
                                        <el-option label="其他" value="2"></el-option>
                                    </el-select>
                                </el-form-item>
                            </el-form-item>
                            <el-form-item v-if="editForm.permission === '學生'">
                                <el-form-item label="家中地址" required>
                                    <el-input v-model="editForm.address" placeholder="請輸入家中地址" maxlength="30"></el-input>
                                </el-form-item>
                            </el-form-item>
                            <el-form-item v-if="editForm.permission === '學生'">
                                <el-form-item label="家中電話" required>
                                    <el-input v-model="editForm.HomeTel" placeholder="請輸入家中電話" maxlength="15"></el-input>
                                </el-form-item>
                            </el-form-item>
                            <el-form-item v-if="editForm.permission === '學生'">
                                <el-form-item label="聯絡人姓名" required>
                                    <el-input v-model="editForm.ContactName" placeholder="請輸入聯絡人姓名" maxlength="15"></el-input>
                                </el-form-item>
                            </el-form-item>
                            <el-form-item v-if="editForm.permission === '學生'">
                                <el-form-item label="聯絡人電話" required>
                                    <el-input v-model="editForm.ConTel" placeholder="請輸入聯絡人電話" maxlength="15"></el-input>
                                </el-form-item>
                            </el-form-item>
                            
                            <!-- 老師 -->
                            <el-form-item v-if="editForm.permission === '老師'">
                                <el-form-item label="電話" required>
                                    <el-input v-model="editForm.Tel" placeholder="請輸入電話" maxlength="15"></el-input>
                                </el-form-item>
                            </el-form-item>
                            <el-form-item v-if="editForm.permission === '老師'">
                                <el-form-item label="職級" required>
                                    <el-select v-model="editForm.Rank" placeholder="請選擇職級" class="select-class">
                                        <el-option label="教授" value="0"></el-option>
                                        <el-option label="副教授" value="1"></el-option>
                                        <el-option label="助理教授" value="2"></el-option>
                                    </el-select>
                                </el-form-item>
                            </el-form-item>
                            <el-form-item v-if="editForm.permission === '老師'">
                                <el-form-item label="辦公室位址" required>
                                    <el-input v-model="editForm.OfficeAddr" placeholder="請輸入辦公室位址" maxlength="30"></el-input>
                                </el-form-item>
                            </el-form-item>
                            <el-form-item v-if="editForm.permission === '老師'">
                                <el-form-item label="辦公室電話" required>
                                    <el-input v-model="editForm.OfficeTel" placeholder="請輸入辦公室電話" maxlength="15"></el-input>
                                </el-form-item>
                            </el-form-item>

                            <el-form-item>
                                <el-button type="primary" @click="saveChanges">保存變更</el-button>
                            </el-form-item>
                        </el-form>
                    </div><!-- edit_page end -->
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import router from '../router'
import axios from 'axios'

const FPath = 'http://127.0.0.1:5000/EditLogin'
const loginForm = reactive({
    account: '',
    password: ''
})
const isVerified = ref(false)

const editForm = reactive({
    account: '',
    password: '',
    permission: '',
    name: '',
    Tel: '',
    email: '',
    address: '',
    Grade: '',
    Gender: '',
    HomeTel: '',
    ContactName: '',
    ConTel: '',
    Rank: '',
    OfficeAddr: '',
    OfficeTel: ''
})

const login = async () => {
    try {
        const response = await axios.post(FPath, loginForm)
        if (response.data.status === 'success') {
            ElMessage({
                message: response.data.message,
                type: 'success',
            });
            isVerified.value = true
            editForm.account = response.data.result[0]
            editForm.password = response.data.result[1]
            editForm.name = response.data.result2[1]
            if (response.data.result[2] === 1){
                editForm.email = response.data.result2[2]
                editForm.permission = '管理員'
            }
            else if (response.data.result[2] === 2){
                editForm.Tel = response.data.result2[2]
                editForm.email = response.data.result2[3]
                editForm.permission = '房東'
            }
            else if (response.data.result[2] === 3){
                editForm.Tel = response.data.result2[5]
                editForm.email = response.data.result2[6]
                editForm.address = response.data.result2[7]
                editForm.Grade = response.data.result2[2]
                if (response.data.result2[3] == 0){
                    editForm.Gender = "男"
                }
                else if (response.data.result2[3] == 1){
                    editForm.Gender = "女"
                }
                else{
                    editForm.Gender = "其他"
                }
                editForm.HomeTel = response.data.result2[7]
                editForm.ContactName = response.data.result2[8]
                editForm.ConTel = response.data.result2[9]
                editForm.permission = '學生'
            }
            else if (response.data.result[2] === 4){
                editForm.Tel = response.data.result2[3]
                if (response.data.result2[2] == 0){
                    editForm.Rank = "教授"
                }
                else if (response.data.result2[2] == 1){
                    editForm.Rank = "副教授"
                }
                else{
                    editForm.Rank = "助理教授"
                }
                editForm.email = response.data.result2[4]
                editForm.OfficeAddr = response.data.result2[5]
                editForm.OfficeTel = response.data.result2[6]
                editForm.permission = '老師'
            }
        } else {
            ElMessage({
                message: response.data.message,
                type: 'error',
            });
            console.error('Failed to verify account:', response.data.message);
        }
    } catch (error) {
        console.error('Error edit account:', error);
    }
}

const saveChanges = async () => {
    try {
        const response = await axios.post('http://127.0.0.1:5000/SaveChanges', editForm)
        if (response.data.status === 'success') {
            ElMessage({
                message: '變更已保存',
                type: 'success',
            });
        } else {
            ElMessage({
                message: response.data.message,
                type: 'error',
            });
            console.error('Failed to save changes:', response.data.message);
        }
    } catch (error) {
        console.error('Error saving changes:', error);
    }
}
</script>

<style>
* {
    font-family: 微軟正黑體;
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

.select-class {
    width: 150px;
}

#common-layout .el-container {
    height: 100vh;
    width: 100%;
}

body {
    background-color: white;
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
    margin: 0 auto;
    padding: 10px;
    width: 300px;
    height: 350px;
    background-color: white;
    border-radius: 5px;
    border-top: 10px solid #409eff;
    box-shadow: 0 0px 70px rgba(0, 0, 0, 0.1);
}

.login {
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

.readonly-text {
    width: 100%;
}
</style>