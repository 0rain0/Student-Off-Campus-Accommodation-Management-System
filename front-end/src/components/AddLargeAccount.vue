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
                    <div style="margin-bottom: 20px;">
                        <h3>檔案格式需求範例：</h3>
                        <p>帳號, 密碼, 權限, 姓名, 電話, 電子郵件,( 老師ID, 班級ID)</p>
                        <h1>管理員電話欄位為空，學生多兩個欄位(老師ID、班級ID)</h1>
                        <p>示例：</p>
                        <p>admin, password, 管理員, 管理員, , admin@example.com</p>
                        <p>landlord, password, 房東, 房東, 987654321, landlord@example.com</p>
                        <p>student, password, 學生, 學生, 123123123, student@example.com, teacher, class</p>
                        <p>teacher, password,老 師, 老師, 456456456, teacher@example.com</p>
                    </div>
                    <div style="text-align: center;">
                        <el-button type="primary">
                            <span>選擇檔案</span>
                            <input type="file" accept=".csv,.txt" id="fileInput" class="file-input" @change="handleFileUpload">
                        </el-button>
                        <el-button type="primary" @click="uploadFile">上傳檔案</el-button>
                        <h1 style="color: black;">文件內容預覽</h1>
                        <pre>{{ fileContent }}</pre> <!-- Display file content -->
                    </div>
                    
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import router from '../router'
import axios from 'axios'

const fileContent = ref<string | null>(null)
const fileInput = ref<HTMLInputElement | null>(null)

const handleFileUpload = (event: Event) => {
    const input = event.target as HTMLInputElement
    if (input.files && input.files.length > 0) {
        const file = input.files[0]
        const reader = new FileReader()
        reader.onload = () => {
            fileContent.value = reader.result as string
        }
        reader.readAsText(file)
    }
}

const resetFileInput = () => {
    if (fileInput.value) {
        fileInput.value.value = ''
    }
}

const uploadFile = async () => {
    if (!fileContent.value) {
        alert('請選擇一個文件')
        return
    }

    try {
        const response = await axios.post('http://127.0.0.1:5000/api/accounts/bulk_add', { fileContent: fileContent.value })
        if (response.data.status === 'success') {
            ElMessage({
                message: response.data.message,
                type: 'success',
            });
        } else {
            ElMessage({
                message: response.data.message,
                type: 'error',
            });
            console.error('Failed to add new account:', response.data.message);
        }
    } catch (error) {
        console.error('Error uploading file:', error)
        alert('文件上傳失敗')
    } finally{
        fileContent.value = null
    }
}

const manageAccounts = () => {
    router.push('/AccountManage')
}

const manageClasses = () => {
    router.push('/ClassManage')
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

.file-input {
    opacity: 0;
    position: relative;
    width: 100%;
    height: 100%;
    cursor: pointer;
}
</style>