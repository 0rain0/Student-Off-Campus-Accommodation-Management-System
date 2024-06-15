<script setup>
import router from "../router/index.js";
import axios from 'axios';
const visit_form_s = () => {
    router.push('/EditRentalSurveyForm_S');
};
const visit_form_t = () => {
    router.push('/EditRentalSurveyForm_T');
    const response = axios.get('http://127.0.0.1:5000/show_stu');
    return response;
};
</script>
<template>
    <div id="common-layout">
        <el-container>
            <el-header id="header" style="display: flex;">
                <el-page-header @click="router.push('/menu');">
                    <!-- <template #breadcrumb>
                        <el-breadcrumb separator="/">
                            <el-breadcrumb-item :to="{ path: './menu' }">
                                Menu
                            </el-breadcrumb-item>
                            <el-breadcrumb-item>系統管理</el-breadcrumb-item>
                        </el-breadcrumb>
                    </template> -->
                    <template #content>
                        <span class="text-large font-600 mr-3" style="color: white;"> 學生訪視 </span>
                    </template>
                </el-page-header>
            </el-header>
            <el-container>
                <el-aside id="aside" width="200px"> </el-aside>
                <el-main id="main">
                   <el-button size="large" round @click="visit_form_s">學生編輯</el-button>
                   <el-button size="large" round @click="visit_form_t">教師編輯</el-button>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<style>
#common-layout .el-container {
    height: 100vh;
    width: 100%;
}

#header {
    background-color: #409eff;
    color: #fff;
    line-height: 60px;
    --el-header-padding: 15px 20px;
}

#aside {
    background-color: #c3e1ff;
    color: #333;
    line-height: 200px;
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
</style>
