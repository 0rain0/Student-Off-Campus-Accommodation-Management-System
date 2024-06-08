import { pa } from "element-plus/es/locale/index.mjs";
import { createRouter, createWebHistory } from "vue-router";  //导入路由
import menu from "../components/menu.vue";

const routes = [
    {
        path:'/', // 要路由到的url路径
        name:'home',
        component:()=>import('../components/login.vue'), //导入路由页面的路径
    },
    {
        path:'/home_example', // 要路由到的url路径
        name:'home_example',
        component:()=>import('../components/HelloWorld_example.vue'), //导入路由页面的路径
    },
    {
        path:'/login_example', // 要路由到的url路径
        name:'login_example',
        component:()=>import('../components/login_example.vue'), //导入路由页面的路径
    },
    {
        path: '/menu',
        name: 'menu',
        component: menu
    },
    {
        path: '/SAS',
        name: 'SAS',
        component: () => import('../components/SAS.vue')
    },
    {
        path: '/VSS',
        name: 'VSS',
        component: () => import('../components/VSS.vue')
    },
    {
        path: '/RAS',
        name: 'RAS',
        component: () => import('../components/RAS.vue')
    }
];

const router = createRouter({    // 定义一个路由器
    history:createWebHistory(),
    routes
});

export default router;