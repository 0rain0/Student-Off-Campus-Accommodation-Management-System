<style>
@import "@/assets/VSS.css";
</style>
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
                        <el-table-column prop="TeacherName" label="導師名字" width="150" />
                        <el-table-column prop="CompleteRate" label="完成率" width="100" />
                        <el-table-column label="操作" width="100">
                                <el-button>
                                    查看
                                </el-button>
                        </el-table-column>
                    </el-table>               
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';

interface ClassStatue {
    Department: string;
    Grade: string;
    Section: string;
    TeacherName: string;
    CompleteRate: number;
}

const classStatus = ref<ClassStatue[]>([]);

const getClassStatus = async () => {
    try {
        const response = await axios.get('http://localhost:5000/VSS/ClassStatue');
        classStatus.value = response.data.classes;
    } catch (error) {
        console.error("Failed to fetch class status:", error);
    }
}

onMounted(getClassStatus);
</script>
