<template>
    <div id="common-layout">
        <el-header id="header" style="display: flex;">
            <el-page-header @click="router.push('/menu');">
                <template #content>
                    <span class="text-large font-600 mr-3" style="color: white;">學生訪視</span>
                </template>
            </el-page-header>
        </el-header>
        <el-container>
            <el-aside id="aside" width="200px">
                <el-menu default-active="1" class="el-menu-vertical-demo" @select="handleSelect">
                    <el-menu-item class="aside-button" @click="CheckStudentStatus">查詢學生填寫狀況</el-menu-item>
                    <el-menu-item class="aside-button" @click="CheckClassStatus">查詢班級填寫狀況</el-menu-item>
                </el-menu>
            </el-aside>
            <el-main>
                
                
            </el-main>
        </el-container>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import router from '../router'
import axios from 'axios'

interface Student {
    SID: string
    Name: string
    Phone: string
    Email: string
    Status: string
}

const students = ref<Student[]>([])
const total = ref(0)
const pageSize = 10
const currentPage = ref(1)
const searchSID = ref('')
const searchName = ref('')

const fetchStudents = async (params = {}) => {
    try {
        const response = await axios.get('http://127.0.0.1:5000/VSS/students', {
            params: {
                page: currentPage.value,
                pageSize,
                ...params
            }
        })
        students.value = response.data.students
        total.value = response.data.total
    } catch (error) {
        console.error("Error fetching students:", error)
    }
}

const handlePageChange = (page: number) => {
    currentPage.value = page
    fetchStudents()
}

const handleSearch = () => {
    const params: any = {}
    if (searchSID.value) params.SID = searchSID.value
    if (searchName.value) params.Name = searchName.value
    fetchStudents(params)
}

const handleReset = () => {
    searchSID.value = ''
    searchName.value = ''
    fetchStudents()
}

const handleFill = (index: number, row: Student) => {
    if (row.Status === '已填寫') {
        // 執行查看操作
        console.log(`查看學生 ${row.SID} 的詳細信息`)
    }
}

onMounted(() => {
    fetchStudents()
})
</script>

<style scoped>
.text-large {
    font-size: 20px;
}
.font-600 {
    font-weight: 600;
}
.mr-3 {
    margin-right: 1rem;
}
#common-layout .el-container {
    height: 100vh;
    width: 100%;
}

#header {
    background-color: #409eff;
    color: #fff;
    line-height: 60px;
    --el-header-padding: 15px 20px;
}

#aside {
    background-color: #c3e1ff;
    color: #333;
    line-height: 200px;
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
.mb-3 {
    margin-bottom: 1rem;
}
</style>
