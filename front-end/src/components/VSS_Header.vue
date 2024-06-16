<script setup lang="ts">
import router from "../router/index.js";
import axios from 'axios'
</script>
<template>
    <el-header id="header" style="display: flex;">
        <el-page-header @click="router.push('/menu');">
            <template #content>
                <span class="text-large font-600 mr-3" style="color: white;"> 學生訪視 </span>
            </template>
        </el-page-header>
    </el-header>
</template>