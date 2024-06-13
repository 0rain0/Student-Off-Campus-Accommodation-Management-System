<script setup>
import { ref, reactive } from 'vue'
import router from '../router';
import { Tools, Comment, List } from '@element-plus/icons-vue';

const toSAS = () => {
    router.push('/sas');
};

const toVSS = () => {
    router.push('/vss');
};

const toRAS = () => {
    router.push('/ras');
};
</script>

<template>
<div id="menu">
    <div id="menu-button-1" class="menu-button">
        <el-button id="sas-button" type="info" @click="toSAS" text>
            <el-icon :size="50"><Tools /></el-icon>
            <span>系統管理</span>
        </el-button>
    </div>
    <div id="menu-button-2" class="menu-button">
        <el-button id="student-button" type="info" @click="toVSS" text>
            <el-icon :size="50"><List /></el-icon>
            <span>學生訪視</span>
        </el-button>
    </div>
    <div id="menu-button-3" class="menu-button">
        <el-button id="ad-button" type="info" @click="toRAS" text>
            <el-icon :size="50"><Comment /></el-icon>
            <span>租屋廣告/留言板</span>
        </el-button>
    </div>
</div>
</template>

<style>
#menu {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    height: 80vh;
}

.menu-button {
    margin-right: 60px;
    display: flex;
    flex-direction: column;
}

#sas-button>span, #student-button>span, #ad-button>span {
    flex-direction: column;
}

#sas-button>span>span, #student-button>span>span, #ad-button>span>span {
    padding-top: 5px;
    color: black;
}

#sas-button, #student-button, #ad-button {
    padding-top: 25px;
    padding-bottom: 50px;
    flex-direction: column;
}

#sas-button .el-icon, #student-button .el-icon, #ad-button .el-icon {
    padding-top: 20px;
}

</style>
