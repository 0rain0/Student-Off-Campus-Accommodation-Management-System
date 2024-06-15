<script setup lang="ts">
import { ref, reactive } from 'vue'
import router from '../router'

// 原來在第一個 <script setup> 中的函數
const visit_form = () => {
    router.push('/EditRentalSurveyForm');
};

// 原來在第二個 <script setup> 中的函數
const CheckStudentStatus = () => {
    console.log('Jump CheckStudentStatus');
    router.push('/CheckStudentStatus');
};
const CheckClassStatus = () => {
    console.log('Jump CheckClassStatus');
    router.push('/CheckClassStatus');
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
                <el-aside id="aside" width="200px">
                <!-- 側邊 -->
                    <el-menu default-active="1" class="el-menu-vertical-demo" @select="handleSelect">
                        <el-button class="aside-button" @click="visit_form">新增/編輯表單</el-button>
                        <el-button class="aside-button" @click="CheckStudentStatus" >查詢學生填寫狀況</el-button>
                        <el-button class="aside-button" @click="CheckClassStatus">查詢班級填寫狀況</el-button>
                    </el-menu>
                </el-aside>
                <el-main id="main">
                   
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
    display: flex;
    align-items: center;
    padding: 0 20px;
}

#aside {
    background-color: #c3e1ff;
    color: #333;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
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