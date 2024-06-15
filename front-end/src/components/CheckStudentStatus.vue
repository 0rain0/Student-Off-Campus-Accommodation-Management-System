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
                <!-- 側邊 -->
                    <el-menu default-active="1" class="el-menu-vertical-demo" @select="handleSelect">
                        <el-button class="aside-button" @click="visit_form_s">學生填寫</el-button>
                        <el-button class="aside-button" @click="visit_form_t">教師填寫</el-button>
                        <el-button class="aside-button" @click="CheckStudentStatus" >查詢學生填寫狀況</el-button>
                        <el-button class="aside-button" @click="CheckClassStatus">查詢班級填寫狀況</el-button>
                    </el-menu>
            </el-aside>
            <el-main>
                <el-row :gutter="20" class="mb-3">
                    <el-col :span="8">
                        <el-input v-model="searchSID" placeholder="輸入學號"></el-input>
                    </el-col>
                    <el-col :span="8">
                        <el-input v-model="searchName" placeholder="輸入姓名"></el-input>
                    </el-col>
                    <el-col :span="8">
                        <el-button type="primary" @click="handleSearch">搜尋</el-button>
                        <el-button @click="handleReset">重置</el-button>
                    </el-col>
                </el-row>
                <el-table :data="students" style="width: 100%">
                    <el-table-column prop="SID" label="學號" width="150" />
                    <el-table-column prop="Name" label="姓名" width="100" />
                    <el-table-column prop="Phone" label="電話" width="150" />
                    <el-table-column prop="Email" label="電子信箱" width="250" />
                    <el-table-column prop="Status" label="狀態" width="150">
                        <template #default="scope">
                            <el-tag :type="scope.row.Status === '已填寫' ? 'success' : 'danger'">
                                {{ scope.row.Status }}
                            </el-tag>
                        </template>
                    </el-table-column>
                    <el-table-column label="操作" width="100">
                        <template #default="scope">
                            <el-button 
                                @click="handleFill(scope.$index, scope.row)" 
                                type="primary" 
                                size="small"
                                :disabled="scope.row.Status !== '已填寫'"
                            >
                                查看
                            </el-button>
                        </template>
                    </el-table-column>
                </el-table>
                <el-pagination
                    layout="prev, pager, next"
                    :total="total"
                    @current-change="handlePageChange">
                </el-pagination>
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

const visit_form_s = () => {
    router.push('/EditRentalSurveyForm_S');
};

const visit_form_t = () => {
    router.push('/EditRentalSurveyForm_T');
};


onMounted(() => {
    fetchStudents()
})
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