<template>
    <link rel="stylesheet" href="VSS.css">
    <div id="common-layout">
        <VSS_Header />
        <el-container>
            <el-container>
                <VSS_Aside />
                <el-main id="main">
                    
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>
<script setup lang="ts">
import router from "../router/index.js";
import axios from 'axios'
</script>