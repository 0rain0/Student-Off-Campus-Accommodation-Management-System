import { createRouter, createWebHistory } from "vue-router";  //导入路由
const routes = [
    {
        path:'/', // 要路由到的url路径
        name:'home',
        component:()=>import('../components/HelloWorld.vue'), //导入路由页面的路径
    },
    {
        path:'/login', // 要路由到的url路径
        name:'login',
        component:()=>import('../components/login.vue'), //导入路由页面的路径
    }
];

const router = createRouter({    // 定义一个路由器
    history:createWebHistory(),
    routes
});

export default router;