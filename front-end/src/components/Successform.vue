<script setup>
import router from "../router/index.js";
const back_vss = () => {
    router.push('/VSS');
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
                  <div id='success'>
                    <h1>成功填寫表單!</h1>
                    <br>
                    <el-button size="large" round @click="back_vss">回到主選單</el-button>
                  </div>
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
    background-color: white;
    color: black;
}

h1{
  font-size: 30px;
}

#success{
  text-align: center;
  padding-top: 300px;
}
</style>
