<template>
  <div id="common-layout">
    <el-container>
      <el-header id="header">
        <el-page-header @click="goBack">
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
          <!-- Row for the title -->
          <el-row>
            <el-col :span="24">
              <h2 style="text-align: center; margin: 20px 0;"> 修改班級</h2>
            </el-col>
          </el-row>
          <!-- Row for the form and table -->
          <el-row :gutter="20">
            <el-col :span="6" :offset="3" class="form-col" style="margin-top: 30px;">
              <div class="form-section">
                <el-form :model="form">
                  <el-form-item label="系所:" style="margin-bottom: 20px;">
                    <el-input v-model="form.department"></el-input>
                  </el-form-item>
                  <el-form-item label="導師:" style="margin-bottom: 20px;">
                    <el-input v-model="form.teacher"></el-input>
                  </el-form-item>
                  <el-form-item label="班級:" style="margin-bottom: 20px;">
                    <el-input v-model="form.section"></el-input>
                  </el-form-item>
                  <el-form-item label="年級:" style="margin-bottom: 20px;">
                    <el-select v-model="form.grade" placeholder="Select">
                      <el-option label="一年級" value="1"></el-option>
                      <el-option label="二年級" value="2"></el-option>
                      <el-option label="三年級" value="3"></el-option>
                      <el-option label="四年級" value="4"></el-option>
                      <el-option label="五年級" value="5"></el-option>
                    </el-select>
                  </el-form-item>
                </el-form>
                <div style="margin-top: 30px; text-align: center;">
                  <el-button type="primary" @click="submit">完成</el-button>
                  <el-button @click="cancel">取消</el-button>
                </div>
              </div>
            </el-col>
            <el-col :span="3"></el-col>
            <el-col :span="10" class="table-col">
              <el-table :data="filterTableData" style="width: 100%;">
                <el-table-column prop="sid" label="學號" />
                <el-table-column prop="name" label="姓名" />
                <el-table-column label="操作">
                  <template #default="scope">
                    <template v-if="isStudentSelected(scope.row)">
                      <el-button size="small" type="danger" @click="removeClass(scope.row)">取消加入</el-button>
                    </template>
                    <template v-else>
                      <el-button size="small" @click="joinClass(scope.row)">加入班級</el-button>
                    </template>
                  </template>
                </el-table-column>
                <el-table-column align="right">
                  <template #header>
                    <el-input v-model="search" size="small" placeholder="Type to search" />
                  </template>
                </el-table-column>
              </el-table>
              <div class="pagination">
                <el-pagination
                  background
                  layout="prev, pager, next"
                  :total="total"
                  :current-page.sync="currentPage"
                  :page-size="pageSize"
                  @current-change="handlePageChange"
                />
              </div>
            </el-col>
          </el-row>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script lang="ts" setup>
import { ref, computed, onMounted } from 'vue'
import router from '../router'
import axios from 'axios'
import { useRoute } from 'vue-router'

const route = useRoute()

interface Student {
  sid: string
  name: string
}

const search = ref('')
const tableData = ref<Student[]>([])
const selectedStudents = ref<Student[]>([])
const total = ref(0)
const currentPage = ref(1)
const pageSize = ref(10)

const form = ref({
  department: '',
  grade: '',
  section: '',
  teacher: ''
})

onMounted(() => {
  form.value.department = route.query.department as string
  form.value.grade = route.query.grade as string
  form.value.section = route.query.class as string
  form.value.teacher = route.query.teacher as string

  fetchStudentData()
})

const fetchStudentData = async (page = 1) => {
  try {
    const response = await axios.get(`http://127.0.0.1:5000/api/students`, {
      params: {
        department: form.value.department,
        grade: form.value.grade,
        section: form.value.section,
        page: page
      }
    })
    if (response.data.status === 'success') {
      tableData.value = response.data.student_all
      selectedStudents.value = response.data.student_selected
      total.value = response.data.total
    } else {
      console.error('Failed to fetch student data:', response.data.message)
    }
  } catch (error) {
    console.error('Error fetching student data:', error)
  }
}

const filterTableData = computed(() =>
  tableData.value.filter(
    (data) =>
      !search.value ||
      data.sid.toLowerCase().includes(search.value.toLowerCase()) ||
      data.name.toLowerCase().includes(search.value.toLowerCase())
  )
)

const isStudentSelected = (student: Student) => {
  return selectedStudents.value.some(selected => selected.sid === student.sid)
}

const joinClass = (student: Student) => {
  console.log('加入班級:', student)
  selectedStudents.value.push(student)
}

const removeClass = (student: Student) => {
  console.log('取消加入:', student)
  selectedStudents.value = selectedStudents.value.filter(selected => selected.sid !== student.sid)
}

const goBack = () => {
  router.push('/menu')
}

const manageAccounts = () => {
  console.log('Manage accounts clicked')
}

const manageClasses = () => {
  console.log('Manage classes clicked')
}

const submit = () => {
  console.log('Submit clicked')
}

const cancel = () => {
  console.log('Cancel clicked')
}

const handlePageChange = (page: number) => {
  fetchStudentData(page)
}

onMounted(() => {
  fetchStudentData()
})
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

.form-col,
.table-col {
  padding: 20px;
}

.form-section {
  background-color: #f9f9f9;
  border-radius: 8px;
}

.pagination {
  margin-top: 20px;
  text-align: center;
}
</style>
