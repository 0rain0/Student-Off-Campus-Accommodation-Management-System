<template>
    <div id="common-layout">
        <VSS_Header />
    </div>
    <div>
      <el-container>
          <VSS_Aside />
          <el-main id="main">
              <Form_S ref="formS" :student="student" />   
              <div align="center">
                  <input type="reset" value="清除表單" name="reset" class="styled-button">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  <input type="button" @click="submitFormS" value="提交表單" name="submit" class="styled-button">
              </div>       
          </el-main>
        </el-container>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, onMounted } from 'vue'
  import { useRoute } from 'vue-router'
  import axios from 'axios'
  import Form_S from './Form_S.vue'
  
  const route = useRoute()
  const student = ref({})
  
  const formS = ref(null)
  
  const fetchStudent = async (id) => {
      try {
          const response = await axios.get(`http://127.0.0.1:5000/VSS/CheckForm_S/${id}`)
          student.value = response.data
      } catch (error) {
          console.error("Error fetching student data:", error)
      }
  }
  
  const submitFormS = () => {
      if (formS.value) {
          formS.value.handleSubmit()
      }
  }
  
  onMounted(() => {
      const id = route.params.id
      fetchStudent(id)
  })
  </script>
  
  <style>
  @import "@/assets/VSS.css";
  </style>
  
