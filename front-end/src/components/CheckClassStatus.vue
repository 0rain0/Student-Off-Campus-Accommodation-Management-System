<template>
    <div id="common-layout">
        <VSS_Header />
        <el-container>
            <el-container>
                <VSS_Aside />
                <el-main id="main">
                    <el-table :data="classStatus" style="width: 100%">
                        <el-table-column prop="Department" label="系所" width="150" />
                        <el-table-column prop="Grade" label="年級" width="100" />
                        <el-table-column prop="Section" label="班級" width="100" />
                        <el-table-column prop="teacherName" label="導師名字" width="150" />
                        <el-table-column prop="CompleteRate" label="完成率" width="100" />
                        <el-table-column label="操作" width="100">
                            <template #default="scope">
                                <el-button @click="handleFill(scope.row.CID)" type="primary" size="small">
                                    查看
                                </el-button>
                            </template>
                        </el-table-column>
                    </el-table>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import router from '../router';
import axios from 'axios';

interface ClassStatus {
    CID: string;
    Department: string;
    Grade: string;
    Section: string;
    teacherName: string;
    CompleteRate: number;
}

const classStatus = ref<ClassStatus[]>([]);

const getClassStatus = async () => {
    try {
        const response = await axios.get('http://localhost:5000/VSS/ClassStatue');
        classStatus.value = response.data.classes;
    } catch (error) {
        console.error("Failed to fetch class status:", error);
    }
}

const handleFill = (CID: string) => {
    console.log(CID);
    router.push({ name: 'CheckStudentStatus', params: { id: CID } });
}

onMounted(getClassStatus);
</script>
