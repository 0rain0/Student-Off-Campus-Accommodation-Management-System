<template>
    <div id="common-layout">
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
                        <span class="text-large
                        font-600 mr-3" style="color: white;"> 學生訪視 </span>
                    </template>
                </el-page-header>
            </el-header>
        </div>
</template>
