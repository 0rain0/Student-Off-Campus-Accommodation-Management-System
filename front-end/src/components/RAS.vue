<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import router from '../router';
import axios from 'axios'
import { Promotion, Plus } from '@element-plus/icons-vue';

let AD_data = ref([]); // Initialize as an empty array
let AD_size = ref(0);
let post_data = ref([]);
let post_size = ref(0);
const rateValue = ref([0, 0, 0, 0]);
const review_content = ref(['', '', '', '']);
const comment_content = ref(['', '', '', '']);

onMounted(() => {
    axios.post('http://127.0.0.1:5000/api/getUserType', { userID: localStorage.getItem('userID') })
        .then(res => {
            console.log("Response data:", res.data)
            if (res.data.status === 'success') {
                if (res.data.data === 1) {
                    document.querySelector('.verify').hidden = false;
                } else {
                    document.querySelector('.verify').hidden = true;
                }
            } else {
                alert('取得使用者類型失敗');
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
            alert('取得使用者類型出現錯誤');
        });
});

let paginatedData = computed(() => {
    if (!AD_data.value || AD_data.value.length === 0) {
        return [];
    }
    const start = (currentPage1.value - 1) * pageSize1.value;
    const end = start + pageSize1.value;
    for (let AD of AD_data.value.slice(start, end)) {
        AD.reviews = [];
        axios.post('http://127.0.0.1:5000/api/ad/get-ad-review', { ADID: AD.ADID })
            .then(res => {
                console.log("Response data:", res.data)
                if (res.data.status === 'success') {
                    AD.reviews = res.data.data;
                } else {
                    alert('取得租屋廣告評論資料失敗');
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
                alert('取得租屋廣告評論資料出現錯誤');
            });

    }
    return AD_data.value.slice(start, end);
});

let paginatedData2 = computed(() => {
    if (!post_data.value || post_data.value.length === 0) {
        return [];
    }
    const start = (currentPage2.value - 1) * pageSize2.value;
    const end = start + pageSize2.value;
    for (let post of post_data.value.slice(start, end)) {
        post.comment = [];
        axios.post('http://127.0.0.1:5000/api/ad/get-post-comment', { PID: post.PID })
            .then(res => {
                console.log("Response data:", res.data)
                if (res.data.status === 'success') {
                    post.comment = res.data.data;
                } else {
                    alert('取得貼文評論資料失敗');
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
                alert('取得貼文評論資料出現錯誤');
            });
    }
    return post_data.value.slice(start, end);
});

let paginatedData3 = computed(() => {
    if (!AD_data.value || AD_data.value.length === 0) {
        return [];
    }
    const start = (currentPage3.value - 1) * pageSize3.value;
    const end = start + pageSize3.value;
    return AD_data.value.slice(start, end);
});


const handleSelect = (index) => {
    if (index === '1') {
        axios.get('http://127.0.0.1:5000/api/ad/get-all-approved')
            .then(res => {
                console.log("Response data:", res.data)
                if (res.data.status === 'success') {
                    AD_data.value = res.data.data;
                    AD_size.value = res.data.data.length;
                } else {
                    alert('取得租屋廣告資料失敗');
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
                alert('取得租屋廣告資料出現錯誤');
            });
        document.querySelector('.ad').hidden = false;
        document.querySelector('.message_board').hidden = true;
        document.querySelector('.ad-verify').hidden = true;
    } else if (index === '2') {
        axios.get('http://127.0.0.1:5000/api/ad/get-post')
            .then(res => {
                console.log("Response data:", res.data)
                if (res.data.status === 'success') {
                    post_data.value = res.data.data;
                    post_size.value = res.data.data.length;
                } else {
                    alert('取得貼文資料失敗');
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
                alert('取得貼文資料出現錯誤');
            });
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

const sentReview = (ADID, content, rate) => {
    let review_form = { ADID: ADID, content: content, rate: rate, userID: localStorage.getItem('userID') };
    axios.post('http://127.0.0.1:5000/api/ad/sent-ad-review', review_form)
        .then(res => {
            console.log("Response data:", res.data)
            if (res.data.status === 'success') {
                alert('評論成功');
                handleSelect('1');
                rateValue.value = [0, 0, 0, 0];
                review_content.value = ['', '', '', ''];
            } else {
                alert('評論失敗');
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
            alert('評論出現錯誤');
        });
}

const sentComment = (PID, content) => {
    let comment_form = { PID: PID, content: content, ID: localStorage.getItem('userID') };
    axios.post('http://127.0.0.1:5000/api/ad/sent-comment', comment_form)
        .then(res => {
            console.log("Response data:", res.data)
            if (res.data.status === 'success') {
                alert('留言成功');
                handleSelect('2');
                comment_content.value = ['', '', '', ''];
            } else {
                alert('留言失敗');
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
            alert('留言出現錯誤');
        });
}

let currentPage1 = ref(1);
let pageSize1 = ref(4);

let currentPage2 = ref(1);
let pageSize2 = ref(4);

let currentPage3 = ref(1);
let pageSize3 = ref(4);
let small = ref(false);
let disabled = ref(false);
let background = ref(false);

let ad_subtitle = { "HouseAge": "屋齡", "HouseType": "房屋類型", "RoomType": "房間類型", "Address": "房屋地址", "RentLimit": "限租條件", "Price": "租金", "ContactName": "聯絡人", "ContactTel": "連絡電話", "AD_Des": "詳細資訊" };

const handleSizeChange1 = (val) => {
    pageSize1.value = val;
};

const handleCurrentChange1 = (val) => {
    currentPage1.value = val;
};

const handleSizeChange3 = (val) => {
    pageSize3.value = val;
};

const handleCurrentChange3 = (val) => {
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
                <el-button type="info" bg text @click="router.push('/login')" style="margin-left: auto;">登出</el-button>
            </el-header>
            <el-container>
                <el-aside id="aside" width="200px">
                    <el-menu default-active="1" class="el-menu-vertical-demo" @select="handleSelect">
                        <el-menu-item index="1">租屋廣告</el-menu-item>
                        <el-menu-item index="2">留言板</el-menu-item>
                        <div class="verify">
                            <el-menu-item index="3">租屋廣告審核</el-menu-item>
                        </div>
                    </el-menu>
                </el-aside>
                <el-main id="main">
                    <div class="ad" hidden>
                        <div class="ad-cards"
                            style="display: flex; flex-direction: row; flex-wrap: wrap; align-items: center;">
                            <div style="display: flex; flex-direction: row; flex-wrap: wrap; ">
                                <el-card v-for="(item, k) in paginatedData" :key="k"
                                    style="max-width: 480px; margin: 10px 10px; width: 18vw;">
                                    <template #header>
                                        <div class="card-header">
                                            <span>{{ item.Name }}</span>
                                        </div>
                                    </template>
                                    <img :src="item.AD_File" style="width: 100%;">
                                    <p v-for="(o, i) in ad_subtitle" :key="i" class="text item">{{ o + ": " + item[i] }}
                                    </p>
                                    <template #footer>
                                        <el-collapse>
                                            <el-collapse-item title="評論" name="1">
                                                <div class="review-block">
                                                    <el-card v-for="(review, j) in item.reviews" :key="j"
                                                        style="margin: 10px 10px;">
                                                        <p>{{ review.ID }}</p>
                                                        <p>{{ review.Content }}</p>
                                                        <el-rate v-model="review.Rate" disabled />
                                                    </el-card>
                                                </div>
                                                <div class="input-group">
                                                    <el-input v-model="review_content[k]" style="max-width: 600px"
                                                        placeholder="評論" class="input-with-icon">
                                                        <template #prepend>
                                                            <el-rate v-model="rateValue[k]" />
                                                        </template>
                                                        <template #append>
                                                            <el-button :icon="Promotion"
                                                                @click="sentReview(item.ADID, review_content[k], rateValue[k])" />
                                                        </template>
                                                    </el-input>
                                                </div>
                                            </el-collapse-item>
                                        </el-collapse>
                                    </template>
                                </el-card>
                            </div>
                            <el-button style="justify-content: center;" :icon="Plus" size="large" circle />
                        </div>

                        <div class="pagination-block">
                            <el-pagination v-model:current-page="currentPage1" v-model:page-size="pageSize1"
                                :small="small" :disabled="disabled" :background="background"
                                layout="prev, pager, next, jumper" :total="AD_size" @size-change="handleSizeChange1"
                                @current-change="handleCurrentChange1" />
                        </div>
                    </div>
                    <div class="message_board" hidden>
                        <div class="message_cards">
                            <div class="ad-cards" style="display: flex; flex-direction: row; flex-wrap: wrap;">
                                <el-card v-for="(item, k) in paginatedData2" :key="k"
                                    style="max-width: 480px; margin: 10px 10px; width: 18vw;">
                                    <template #header>
                                        <div class="card-header">
                                            <span>{{ item.Name }}</span>
                                        </div>
                                    </template>
                                    <img :src="item.Post_File" style="width: 100%;">
                                    <p class="text item">Author: {{ item.ID }}</p>
                                    <p class="text item">{{ item.Content }}</p>
                                    <template #footer>
                                        <el-collapse>
                                            <el-collapse-item title="留言" name="1">
                                                <div class="comment-block">
                                                    <el-card v-for="(comment, j) in item.comment" :key="j"
                                                        style="margin: 10px 10px;">
                                                        <p>{{ comment.ID }}</p>
                                                        <p>{{ comment.Content }}</p>
                                                    </el-card>
                                                </div>
                                                <div>
                                                    <el-input v-model="comment_content[k]" style="max-width: 600px"
                                                        placeholder="留言" class="input-with-icon">
                                                        <template #append>
                                                            <el-button :icon="Promotion"
                                                                @click="sentComment(item.PID, comment_content[k])" />
                                                        </template>
                                                    </el-input>
                                                </div>
                                            </el-collapse-item>
                                        </el-collapse>
                                    </template>
                                </el-card>
                            </div>
                        </div>
                        <div class="pagination-block">
                            <el-pagination v-model:current-page="currentPage2" v-model:page-size="pageSize2"
                                :small="small" :disabled="disabled" :background="background"
                                layout="prev, pager, next, jumper" :total="AD_size" @size-change="handleSizeChange2"
                                @current-change="handleCurrentChange2" />
                        </div>
                    </div>
                    <div class="ad-verify" hidden>
                        <div class="ad-cards" style="display: flex; flex-direction: row; flex-wrap: wrap;">
                            <el-card v-for="(item, k) in paginatedData3" :key="k"
                                style="max-width: 480px; margin: 10px 10px; width: 18vw;">
                                <template #header>
                                    <div class="card-header">
                                        <span>{{ item.Name }}</span>
                                    </div>
                                </template>
                                <img :src="item.AD_File" style="width: 100%;">
                                <p v-for="(o, i) in ad_subtitle" :key="i" class="text item">{{ o + ": " + item[i] }}
                                </p>
                                <template #footer>
                                    <el-button type="success" size="mini"
                                        @click="ad_verify(item.ADID, 'accept')">通過</el-button>
                                    <el-button type="danger" size="mini"
                                        @click="ad_verify(item.ADID, 'reject')">不通過</el-button>
                                </template>
                            </el-card>
                        </div>
                        <div class="pagination-block">
                            <el-pagination v-model:current-page="currentPage3" v-model:page-size="pageSize3"
                                :small="small" :disabled="disabled" :background="background"
                                layout="prev, pager, next, jumper" :total="AD_size" @size-change="handleSizeChange3"
                                @current-change="handleCurrentChange3" />
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

.input-group>.el-input-group {
    display: flex;
    flex-direction: column;
}
</style>
