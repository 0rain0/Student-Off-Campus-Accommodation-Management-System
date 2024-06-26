<template>
    <div id="common-layout">
        <VSS_Header />
        <el-container>
            <VSS_Aside />
            <el-main>
                <el-row :gutter="20" class="mb-3" v-if="isUserType('1')">
                    <el-col :span="6">
                        <el-input v-model="searchSID" placeholder="輸入學號"></el-input>
                    </el-col>
                    <el-col :span="6">
                        <el-input v-model="searchName" placeholder="輸入姓名"></el-input>
                    </el-col>
                    <el-col :span="6">
                        <el-input v-model="searchCID" placeholder="輸入班級CID"></el-input>
                    </el-col>
                    <el-col :span="6">
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
                            <el-button v-if="isUserType('4')"
                                @click="handleFill(scope.row.SID)" 
                                type="primary" 
                                size="small"
                                :disabled="scope.row.Status !== '已填寫'"
                            >
                                填寫
                            </el-button>
                            <br v-if="isUserType('4')">
                            <el-button
                                @click="handleQ(scope.row.SID)"
                                type="primary"
                                size="small"
                                :disabled="scope.row.Status !== '已填寫'"
                            >
                                查詢
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
import { ref, onMounted, defineProps } from 'vue'
import router from '../router'
import axios from 'axios'
import Cookies from 'js-cookie'

const userType = ref(null)
const userNames = ref(null)

onMounted(() => {
  userType.value = Cookies.get('UserType')
  userNames.value = Cookies.get('username')
})

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
const searchCID = ref('')

const fetchStudents = async (params = {}) => {
    try {
        let additionalParams = {}
        if (userType.value === '4') {
            const tidResponse = await axios.get('http://127.0.0.1:5000/VSS/TIDtoCID', {
                params: { TID: userNames.value }
            })
            console.log('TID to CID response:', tidResponse.data)
            additionalParams = { CID: tidResponse.data.cid.CID }
        }
        if(userType.value === '1') {
            additionalParams = { CID: searchCID.value }
        }
        console.log('Additional params:', additionalParams)
        
        // 合并 params 和 additionalParams
        const combinedParams = { 
            page: currentPage.value,
            pageSize,
            ...params,
            ...additionalParams 
        }
        console.log('Combined params:', combinedParams)

        const response = await axios.get('http://127.0.0.1:5000/VSS/studentStatue', {
            params: combinedParams
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
    if (searchCID.value) params.CID = searchCID.value
    fetchStudents(params)
}

const handleReset = () => {
    searchSID.value = ''
    searchName.value = ''
    searchCID.value = ''
    fetchStudents()
}

const handleFill = (sid: string) => {
    router.push({ name: 'CheckStudentForm', params: { id: sid } })
}

const props = defineProps({
    id: {
        type: String,
        default: null
    }
})

onMounted(() => {
    if (props.id) {
        searchCID.value = props.id
        handleSearch()
    } else {
        fetchStudents()
    }
})

const handleQ = (sid: string) => {
    router.push({ name: 'QueryStudentForm', params: { id: sid } })
}
onMounted(() => {
    fetchStudents()
})


const isUserType = (type: string) => {
    return userType.value === type
}

</script>

<style>
@import "@/assets/VSS.css";
</style>
