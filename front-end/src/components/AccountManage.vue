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
                        <el-button type="primary" @click="addAccount">新增帳號</el-button>
                        <h1 style="color: black;">帳號管理</h1>
                    </div>
                    <el-table :data="filterTableData" style="width: 100%">
                        <el-table-column label="帳號" prop="account" />
                        <el-table-column label="密碼">
                            <template #default="scope">
                                <el-input v-if="scope.row.isEditing" v-model="scope.row.password" />
                                <span v-else>{{ scope.row.password }}</span>
                            </template>
                        </el-table-column>
                        <el-table-column label="權限" prop="permission" />
                        <el-table-column label="姓名">
                            <template #default="scope">
                                <el-input v-if="scope.row.isEditing" v-model="scope.row.name" />
                                <span v-else>{{ scope.row.name }}</span>
                            </template>
                        </el-table-column>
                        <el-table-column label="電話">
                            <template #default="scope">
                                <el-input v-if="scope.row.isEditing" v-model="scope.row.phone" />
                                <span v-else>{{ scope.row.phone }}</span>
                            </template>
                        </el-table-column>
                        <el-table-column label="電子信箱">
                            <template #default="scope">
                                <el-input v-if="scope.row.isEditing" v-model="scope.row.email" />
                                <span v-else>{{ scope.row.email }}</span>
                            </template>
                        </el-table-column>
                        <el-table-column align="right">
                            <template #header>
                                <el-input v-model="search" size="small" placeholder="Type to search" />
                            </template>
                            <template #default="scope">
                                <el-button size="small" v-if="scope.row.isEditing" @click="saveEdit(scope.row)">
                                    確認編輯
                                </el-button>
                                <el-button size="small" v-else @click="enableEdit(scope.row)">
                                    修改
                                </el-button>
                                <el-button size="small" type="danger" @click="confirmDelete(scope.$index, scope.row)">
                                    刪除
                                </el-button>
                            </template>
                        </el-table-column>
                    </el-table>
                    <div class="pagination">
                        <el-pagination background layout="prev, pager, next" :total="total"
                            :current-page.sync="currentPage" :page-size="pageSize" @current-change="handlePageChange" />
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

interface Account {
    account: string
    password: string
    permission: string
    name: string
    phone: string
    email: string
}

const search = ref('')
const tableData = ref<Account[]>([])
const total = ref(0)
const currentPage = ref(1)
const pageSize = ref(10)

const FPath = 'http://127.0.0.1:5000/AccountManage'

const fetchAccountData = async (page = 1) => {
    const response = await axios.get(`http://127.0.0.1:5000/api/accounts?page=${page}`)
    if (response.data.status === 'success') {
        tableData.value = response.data.data
        total.value = response.data.total
    } else {
        console.error('Failed to fetch account data:', response.data.message)
    }
}

const filterTableData = computed(() =>
    tableData.value.filter(
        (data) =>
            !search.value ||
            data.account.toLowerCase().includes(search.value.toLowerCase()) ||
            data.password.toLowerCase().includes(search.value.toLowerCase()) ||
            data.permission.toLowerCase().includes(search.value.toLowerCase()) ||
            data.name.toLowerCase().includes(search.value.toLowerCase()) ||
            data.phone.toLowerCase().includes(search.value.toLowerCase()) ||
            data.email.toLowerCase().includes(search.value.toLowerCase())
    )
)

const saveEdit = async (row: Account) => {
    console.log('Save:', row)
    try {
        const response = await axios.post(`http://127.0.0.1:5000/api/account/update`, { ...row, _method: 'UPDATE' })
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
            console.error('Failed to update account:', response.data.message);
        }
        row.isEditing = false
        fetchAccountData(currentPage.value);
    } catch (error) {
        console.error('Error updating account:', error);
    }
}

const enableEdit = (row: Account) => {
    row.isEditing = true
}

const confirmDelete = (index: number, row: Account) => {
    ElMessageBox.confirm(
        '是否刪除此帳號?',
        '提示',
        {
            confirmButtonText: '確認刪除',
            cancelButtonText: '取消',
            type: 'warning',
        }
    ).then(() => {
        handleDelete(index, row)
    }).catch(() => {
        console.log('取消刪除');
    })
}

const handleDelete = async (index: number, row: Account) => {
    console.log(index, row)
    try {
        const response = await axios.post(`http://127.0.0.1:5000/api/account/delete`, { ...row, _method: 'DELETE' });
        if (response.data.status === 'success') {
            ElMessage({
                message: '刪除成功',
                type: 'success',
            });
            fetchAccountData(currentPage.value);
        } else {
            ElMessage({
                message: response.data.message,
                type: 'error',
            });
            console.error('Failed to delete account:', response.data.message);
        }
    } catch (error) {
        console.error('Error deleting account:', error);
    }
}

const manageAccounts = () => {
    console.log('Manage accounts clicked')
    router.push('/AccountManage')
}

const manageClasses = () => {
    console.log('Manage classes clicked')
    router.push('/ClassManage')
}

const addAccount = () => {
    console.log('Add account clicked')
    router.push('/NewAccount')
}

const handlePageChange = (page: number) => {
    fetchAccountData(page)
}

onMounted(() => {
    fetchAccountData()
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
