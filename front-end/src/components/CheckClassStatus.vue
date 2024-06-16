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
                    <el-table :data="ClassStatu" style="width: 100%">
                        <el-table-column prop="Department" label="系所" width="150" />
                        <el-table-column prop="Grade" label="年級" width="100" />
                        <el-table-column prop="Section" label="班級" width="100" />
                        <el-table-column prop="Total" label="人數" width="100" />
                        <el-table-column prop="Status" label="狀態" width="100">
                            <template #default="scope">
                                <el-tag :type="scope.row.Status === '已填寫' ? 'success' : 'danger'">
                                    {{ scope.row.Status }}
                                </el-tag>
                            </template>
                        </el-table-column>     
                    </el-table>               
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>
<script setup lang="ts">
import router from "../router/index.js";
import axios from 'axios'
</script>