<script setup>
import { ref, reactive, computed } from 'vue'
import router from '../router';
import axios from 'axios'

let AD_data = ref([]); // Initialize as an empty array
let AD_size = ref(0);
let paginatedData = computed(() => {
  if (!AD_data.value || AD_data.value.length === 0) {
    return [];
  }
  const start = (currentPage3.value - 1) * pageSize3.value;
  const end = start + pageSize3.value;
  return AD_data.value.slice(start, end);
});

const handleSelect = (index) => {
    if (index === '1') {
        document.querySelector('.ad').hidden = false;
        document.querySelector('.message_board').hidden = true;
        document.querySelector('.ad-verify').hidden = true;
    } else if (index === '2') {
        document.querySelector('.ad').hidden = true;
        document.querySelector('.message_board').hidden = false;
        document.querySelector('.ad-verify').hidden = true;
    } else if (index === '3') {
        axios.get('http://127.0.0.1:5000/api/ad/get_verify')
            .then(res => {
                console.log("Response data:", res.data)
                if (res.data.status === 'success') {
                    AD_data.value = res.data.data;
                    AD_size.value = res.data.data.length;
                } else {
                    alert('取得租屋廣告審核資料失敗');
                }
            })
            .catch(error => {
                if (error.response) {
                    console.error("Error response data:", error.response.data)
                    console.error("Error response status:", error.response.status)
                    console.error("Error response headers:", error.response.headers)
                } else if (error.request) {
                    console.error("Error request data:", error.request)
                } else {
                    console.error("Error message:", error.message)
                }
                console.error("Error config:", error.config)
                alert('取得租屋廣告審核資料出現錯誤');
            });
        document.querySelector('.ad').hidden = true;
        document.querySelector('.message_board').hidden = true;
        document.querySelector('.ad-verify').hidden = false;
    }
}

const ad_verify = (ADID, verify_result) => {
    axios.post('http://127.0.0.1:5000/api/ad/verify', { ADID: ADID, verify_result: verify_result })
        .then(res => {
            console.log("Response data:", res.data)
            if (res.data.status === 'success') {
                alert('審核成功');
                handleSelect('3');
            } else {
                alert('審核失敗');
            }
        })
        .catch(error => {
            if (error.response) {
                console.error("Error response data:", error.response.data)
                console.error("Error response status:", error.response.status)
                console.error("Error response headers:", error.response.headers)
            } else if (error.request) {
                console.error("Error request data:", error.request)
            } else {
                console.error("Error message:", error.message)
            }
            console.error("Error config:", error.config)
            alert('審核出現錯誤');
        });

}

let currentPage3 = ref(1);
let pageSize3 = ref(4); // Set page size to 4
let small = ref(false);
let disabled = ref(false);
let background = ref(false);

let ad_subtitle = {"HouseAge": "屋齡", "HouseType": "房屋類型", "RoomType": "房間類型", "Address": "房屋地址", "RentLimit": "限租條件", "Price": "租金", "ContactName": "聯絡人", "ContactTel": "連絡電話", "AD_Des": "詳細資訊" };

const handleSizeChange = (val) => {
  pageSize3.value = val;
};

const handleCurrentChange = (val) => {
  currentPage3.value = val;
};
</script>

<template>
    <div id="common-layout">
        <el-container>
            <el-header id="header" style="display: flex;">
                <el-page-header @click="router.push('/menu');">
                    <template #content>
                        <span class="text-large font-600 mr-3" style="color: white;"> 租屋廣告/留言板 </span>
                    </template>
                </el-page-header>
            </el-header>
            <el-container>
                <el-aside id="aside" width="200px">
                    <el-menu default-active="1" class="el-menu-vertical-demo" @select="handleSelect">
                        <el-menu-item index="1">租屋廣告</el-menu-item>
                        <el-menu-item index="2">留言板</el-menu-item>
                        <el-menu-item index="3">租屋廣告審核</el-menu-item>
                    </el-menu>
                </el-aside>
                <el-main id="main">
                    <div class="ad" hidden>
                        <div class="ad-cards">
                            <el-card style="max-width: 480px">
                                <template #header>
                                    <div class="card-header">
                                        <span>Card name</span>
                                    </div>
                                </template>
                                <p v-for="o in 4" :key="o" class="text item">{{ ad_subtitle[o] + o }}</p>
                                <template #footer>Footer content</template>
                            </el-card>
                        </div>
                        <!-- <div class="pagination-block">
                            <el-pagination v-model:current-page="currentPage3" v-model:page-size="pageSize3"
                                :small="small" :disabled="disabled" :background="background"
                                layout="prev, pager, next, jumper" :total="AD_size" @size-change="handleSizeChange"
                                @current-change="handleCurrentChange" />
                        </div> -->
                    </div>
                    <div class="message_board" hidden>
                        <p>留言板</p>
                    </div>
                    <div class="ad-verify" hidden>
                        <div class="ad-cards" style="display: flex; flex-direction: row; flex-wrap: wrap;">
                            <el-card v-for="(item, k) in paginatedData" :key="k" style="max-width: 480px; margin: 10px 10px; width: 18vw;">
                                <template #header>
                                    <div class="card-header">
                                        <span>{{ item.Name }}</span>
                                    </div>
                                </template>
                                <img :src="item.AD_File" style="width: 100%;">
                                <p v-for="(o, i) in ad_subtitle" :key="i" class="text item">{{ o + ": " + item[i] }}</p>
                                <template #footer>
                                    <el-button type="success" size="mini" @click="ad_verify(item.ADID, 'accept')">通過</el-button>
                                    <el-button type="danger" size="mini" @click="ad_verify(item.ADID, 'reject')">不通過</el-button>
                                </template>
                            </el-card>
                        </div>
                        <div class="pagination-block">
                            <el-pagination v-model:current-page="currentPage3" v-model:page-size="pageSize3"
                                :small="small" :disabled="disabled" :background="background"
                                layout="prev, pager, next, jumper" :total="AD_size" @size-change="handleSizeChange"
                                @current-change="handleCurrentChange" />
                        </div>
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
}
</style>
