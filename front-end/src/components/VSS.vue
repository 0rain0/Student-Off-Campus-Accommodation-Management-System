<script setup>
import { ref, reactive } from 'vue'
import router from '../router';
const visit_form = () => {
    router.push('/EditRentalSurveyForm');
};

</script>
<template>
    <link rel="stylesheet" href="VSS.css">
    <div id="common-layout">
        <VSS_Header />
        <el-container>
            <el-container>
                <el-aside id="aside" width="200px"> </el-aside>
                <el-main id="main">
                   <el-button size="large" round @click="visit_form">新增/編輯表單</el-button>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>