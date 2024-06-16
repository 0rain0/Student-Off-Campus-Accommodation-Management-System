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
          <el-menu default-active="2" class="el-menu-vertical-demo" @select="handleSelect">
            <el-menu-item index="1">帳號管理</el-menu-item>
            <el-menu-item index="2">班級管理</el-menu-item>
          </el-menu>
        </el-aside>
        <el-main id="main">
          <el-button type="primary" @click="addClass">新增班級</el-button>

          <el-table :data="filterTableData" style="width: 100%">
            <el-table-column label="Department" prop="department" />
            <el-table-column label="Grade" prop="grade" />
            <el-table-column label="Class" prop="class" />
            <el-table-column label="Number" prop="number" />
            <el-table-column label="Teacher" prop="teacher" />
            <el-table-column align="right">
              <template #header>
                <el-input v-model="search" size="small" placeholder="Type to search" />
              </template>
              <template #default="scope">
                <el-button size="small" @click="handleEdit(scope.$index, scope.row)">
                  Edit
                </el-button>
                <el-button size="small" type="danger" @click="handleDelete(scope.$index, scope.row)">
                  Delete
                </el-button>
              </template>
            </el-table-column>
          </el-table>
          <div class="pagination">
            <el-pagination background layout="prev, pager, next" :total="total" :current-page.sync="currentPage"
              :page-size="pageSize" @current-change="handlePageChange" />
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>




<script lang="ts" setup>
import { ref, computed, onMounted } from 'vue'
import router from '../router'
import axios from 'axios'

interface Class {
  date: string
  name: string
  department: string
  grade: string
  class: string
  number: number
  teacher: string
}

const search = ref('')
const tableData = ref<Class[]>([])
const total = ref(0)
const currentPage = ref(1)
const pageSize = ref(10)

const FPath = 'http://127.0.0.1:5000/ClassManage'

const fetchClassData = async (page = 1) => {
  const response = await axios.get(`http://127.0.0.1:5000/api/classes?page=${page}`)
  if (response.data.status === 'success') {
    tableData.value = response.data.data
    total.value = response.data.total
  } else {
    console.error('Failed to fetch class data:', response.data.message)
  }
}

const filterTableData = computed(() =>
  tableData.value.filter(
    (data) =>
      !search.value ||
      data.department.toLowerCase().includes(search.value.toLowerCase()) ||
      data.teacher.toLowerCase().includes(search.value.toLowerCase())
  )
)

const handleEdit = (index: number, row: Class) => {
  console.log('Edit:', index, row)
  router.push({
    path: '/EditClass',
    query: {
      index: index.toString(),
      department: row.department,
      grade: row.grade,
      class: row.class,
      number: row.number.toString(),
      teacher: row.teacher
    }
  })
}

const handleDelete = async (index: number, row: Class) => {
  console.log(index, row)
  try {
    const response = await axios.post(`http://127.0.0.1:5000/api/classes/delete`, { ...row, _method: 'DELETE' });
    if (response.data.status === 'success') {
      fetchClassData(currentPage.value);
    } else {
      console.error('Failed to delete class:', response.data.message);
    }
  } catch (error) {
    console.error('Error deleting class:', error);
  }
}

const goBack = () => {
  router.push('/menu')
}

const manageAccounts = () => {
  console.log('Manage accounts clicked')
  router.push('/AccountManage')
}

const manageClasses = () => {
  console.log('Manage classes clicked')
  router.push('/ClassManage')
}

const addClass = () => {
  console.log('Add class clicked')
  router.push({
    path: '/AddNewClass',
  })
}

const handlePageChange = (page: number) => {
  fetchClassData(page)
}

onMounted(() => {
  fetchClassData()
})

const handleSelect = (index: string) => {
  if (index === '1') {
    manageAccounts()
  } else if (index === '2') {
    manageClasses()
  }
}
</script>





<style >
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
  /* align-items: center;
    padding: 20px; */
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