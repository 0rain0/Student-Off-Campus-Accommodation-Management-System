<template>
    <div id="common-layout">
        <VSS_Header />
        <el-container>
            <VSS_Aside />
            <el-main id="main">
                <Form_S :student="student" />
                <Form_T ref="formTComponent" :student="student" />
                <div align="center">
                    <input type="reset" value="清除表單" name="reset" class="styled-button">
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <input type="submit" value="提交表單" name="submit" class="styled-button" @click="submitForm">
                </div>
            </el-main>
        </el-container>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import Form_S from './Form_S.vue'
import Form_T from './Form_T.vue'

const route = useRoute()
const student = ref({})
const formTComponent = ref(null)

const fetchStudent = async (id) => {
    try {
        const response = await axios.get(`http://127.0.0.1:5000/VSS/CheckForm_S/${id}`)
        console.log('Fetched student data:', response.data)

        const dataArray = response.data.form
        student.value = {
            VFID: dataArray[0],
            SID: dataArray[1],
            DG: dataArray[2],
            S_Name: dataArray[3],
            S_Tel: dataArray[4],
            T_Name: dataArray[5],
            State: dataArray[6],
            V_Time: dataArray[7],
            L_Name: dataArray[8],
            L_Tel: dataArray[9],
            R_Addr: dataArray[10],
            RentType: dataArray[11],
            RoomType: dataArray[12],
            Price: dataArray[13],
            RoommateN: dataArray[14],
            RoommateP: dataArray[15],
            RA: dataArray[16],
            Deposit: dataArray[17],
            Recommend: dataArray[18],
            SA_01: dataArray[19],
            SA_02: dataArray[20],
            SA_03: dataArray[21],
            SA_04: dataArray[22],
            SA_05: dataArray[23],
            SA_06: dataArray[24],
            SA_07: dataArray[25],
            SA_08: dataArray[26],
            SA_09: dataArray[27],
            SA_10: dataArray[28],
            SA_11: dataArray[29],
            SA_12: dataArray[30],
            SA_13: dataArray[31],
            EN_01: dataArray[32],
            EN_02: dataArray[33],
            EN_03: dataArray[34],
            EN_04: dataArray[35],
            VI_01: dataArray[36],
            VI_02: dataArray[37],
            Result: dataArray[38],
            DI_01: dataArray[39],
            DI_02: dataArray[40],
            DI_03: dataArray[41],
            DI_04: dataArray[42],
            DI_05: dataArray[43],
            EN_03_Des: dataArray[44],
            EN_04_Des: dataArray[45],
            VI_01_Des: dataArray[46],
            RE_Des: dataArray[47],
            RE_Memo: dataArray[48],
            DI_05_Des: dataArray[49]
        }
        console.log('Converted student data:', student.value)
    } catch (error) {
        console.error("Error fetching student data:", error)
    }
}
const submitFormS = () => {
    if (formS.value && formS.value.handleSubmit) {
        formS.value.handleSubmit()
    }
}
onMounted(() => {
    const id = route.params.id
    fetchStudent(id)
})

watch(student, (newVal) => {
    console.log('Student data passed to Form_S and Form_T:', newVal)
})
</script>

<style>
@import "@/assets/VSS.css";
</style>
