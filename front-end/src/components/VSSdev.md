# 開發VSS前端注意事項

## 新網頁模板
```vue
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
```
<VSS_Header />是Header模組
<VSS_Aside />是側欄模組