<template>
    <div id="common-layout">
      <el-header id="header" style="display: flex;">
        <el-page-header @click="router.push('/menu');">
          <template #content>
            <span class="text-large font-600 mr-3" style="color: white;">
              學生訪視
            </span>
          </template>
        </el-page-header>
      </el-header>
      <el-main>
        <el-table :data="students" style="width: 100%">
          <el-table-column prop="id" label="學號" width="150" />
          <el-table-column prop="account" label="帳號" width="150" />
          <el-table-column prop="password" label="密碼" width="100" />
          <el-table-column prop="name" label="姓名" width="100" />
          <el-table-column prop="phone" label="電話" width="150" />
          <el-table-column prop="email" label="電子信箱" width="250" />
          <el-table-column prop="status" label="學生填寫狀態" width="150">
            <template slot-scope="scope">
              <el-tag :type="scope.row.status === '已填寫' ? 'success' : 'info'">
                {{ scope.row.status }}
              </el-tag>
            </template>
          </el-table-column>
          <el-table-column label="操作" width="100">
            <template slot-scope="scope">
              <el-button @click="handleFill(scope.$index, scope.row)"
                         type="primary"
                         size="small">
                填寫
              </el-button>
            </template>
          </el-table-column>
        </el-table>
        <el-pagination
          layout="prev, pager, next"
          :total="total"
          @current-change="handlePageChange">
        </el-pagination>
      </el-main>
    </div>
  </template>
  <script setup lang="ts">
    import { ref, onMounted } from 'vue';
    import { useRouter } from 'vue-router';
    import { getStudents } from '../api';
  </script>
  
  <style scoped>
  .text-large {
    font-size: 20px;
  }
  .font-600 {
    font-weight: 600;
  }
  .mr-3 {
    margin-right: 1rem;
  }
  </style>
  