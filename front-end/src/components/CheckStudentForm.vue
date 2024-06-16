<template>
    <div id="common-layout">
        <VSS_Header />
        <el-container>
            <VSS_Aside />
            <el-main id="main">
                <Form_S :student="student" />
                <Form_T :student="student" />
                <div align="center">
                    <input type="reset" value="清除表單" name="reset" class="styled-button">
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <input type="submit" value="提交表單" name="submit" class="styled-button">
                </div>
            </el-main>
        </el-container>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import Form_S from './Form_S.vue'
import Form_T from './Form_T.vue'

const route = useRoute()
const student = ref(null)

const fetchStudent = async (id: string) => {
    try {
        const response = await axios.get(`http://127.0.0.1:5000/VSS/CheckForm_S/${id}`)
        student.value = response.data
    } catch (error) {
        console.error("Error fetching student data:", error)
    }
}

onMounted(() => {
    const id = route.params.id as string
    fetchStudent(id)
})
</script>

<style>
@import "@/assets/VSS.css";
</style>
