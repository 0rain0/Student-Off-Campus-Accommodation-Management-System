<script setup>
import { ref, reactive, onMounted } from 'vue'
import router from '../router'
import Cookies from 'js-cookie'
import { Tools, Comment, List, Edit, User } from '@element-plus/icons-vue'

const userType = ref(null)

onMounted(() => {
  userType.value = Cookies.get('UserType')
})

const toSAS = () => {
  router.push('/ClassManage')
}

const toVSS = () => {
  router.push('/vss')
}

const toEditPersonFile = () => {
    router.push('/EditPersonFile')
}

const toRAS = () => {
  router.push('/ras')
}

const logout = () => {
  Cookies.remove('UserType')
  Cookies.remove('username')
  alert('已登出')
  router.push('/login')
}
</script>

<template>
  <div id="menu">
    <div id="menu-button-1" class="menu-button" v-if="userType === '1'">
      <el-button id="sas-button" type="info" @click="toSAS" text>
        <el-icon :size="50"><Tools /></el-icon>
        <span>系統管理</span>
      </el-button>
    </div>
    <div id="menu-button-2" class="menu-button" v-if="userType === '1' || userType === '3' || userType === '4'">
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
    <div id="menu-button-3" class="menu-button">
        <el-button id="ad-button" type="info" @click="toEditPersonFile" text>
            <el-icon :size="50"><Edit /></el-icon>
            <span>修改個人資料</span>
        </el-button>
    </div>
        <div id="menu-button-4" class="menu-button">
          <el-button id="log-out" type="info" @click="logout" text>
            <el-icon :size="50"><User /></el-icon>
            <span>登出</span>
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

#sas-button>span, #student-button>span, #ad-button>span, #log-out>span {
  flex-direction: column;
}

#sas-button>span>span, #student-button>span>span, #ad-button>span>span, #log-out>span>span {
  padding-top: 5px;
  color: black;
}

#sas-button, #student-button, #ad-button, #log-out {
  padding-top: 25px;
  padding-bottom: 50px;
  flex-direction: column;
}

#sas-button .el-icon, #student-button .el-icon, #ad-button .el-icon, #log-out .el-icon {
  padding-top: 20px;
}
</style>
