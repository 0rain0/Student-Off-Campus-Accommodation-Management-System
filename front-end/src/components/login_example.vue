<template>
    <center>
        <el-form v-model="mqttM" ref="mqqtRef" label-width="120px" method="post">
            <el-col :span="8">
                <el-form-item label="username"><el-input v-model="mqttM.username" style="width: 240px" placeholder=""
                        ></el-input></el-form-item>
                <el-form-item label="password"><el-input v-model="mqttM.password" style="width: 240px" placeholder=""
                        ></el-input></el-form-item>
                <el-form-item><el-button type="primary" @click="onSubmit()">提交</el-button></el-form-item>
                <el-form-item label="count"><el-input v-model="status" style="width: 240px" disabled
                        placeholder="" /></el-form-item>

            </el-col>
        </el-form>
    </center>
</template>
<script lang="ts" setup>

import { reactive, ref } from 'vue'
import axios from 'axios'
const FPath = 'http://localhost:5000/login'
const mqttM = reactive({
    username: '',
    password: '',
})
const status = ref('')
const onSubmit = () => {
    axios.post(FPath, mqttM).then(res => {
        console.log(res)
        status.value = res.data.login
    })
}

</script>
