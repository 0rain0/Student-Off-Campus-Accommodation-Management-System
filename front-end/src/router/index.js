import { pa } from "element-plus/es/locale/index.mjs";
import { createRouter, createWebHistory } from "vue-router";  //导入路由
const routes = [
    {
        path:'/', // 要路由到的url路径
        name:'home',
        component:()=>import('../components/login.vue'), //导入路由页面的路径
    },
    {
        path:'/register', // 要路由到的url路径
        name:'Landlord_register',
        component:()=>import('../components/Landlord_register.vue'), //导入路由页面的路径
    },
    {
        path:'/login', // 要路由到的url路径
        name:'Login',
        component:()=>import('../components/login.vue'), //导入路由页面的路径
    },
    {
        path:'/menu', // 要路由到的url路径
        name:'menu',
        component:()=>import('../components/menu.vue'), //导入路由页面的路径
    },
    {
        path:'/ClassManage', // 要路由到的url路径
        name:'ClassManage',
        component:()=>import('../components/ClassManage.vue'), //导入路由页面的路径
    },
    {
        path:'/EditClass', // 要路由到的url路径
        name:'EditClass',
        component:()=>import('../components/EditClass.vue'), //导入路由页面的路径
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
        path: '/back_vss',
        name: 'back_vss',
        component: () => import('../components/VSS.vue')
    },
    {
        path: '/RAS',
        name: 'RAS',
        component: () => import('../components/RAS.vue')
    },
    {
        path: '/EditRentalSurveyForm',
        name: 'EditRentalSurveyForm',
        component: () => import('../components/EditRentalSurveyForm.vue')
    }
    ,
    {
        path: '/Successform',
        name: 'Successform',
        component: () => import('../components/Successform.vue')
        path:'/AddNewClass', // 要路由到的url路径
        name:'AddNewClass',
        component:()=>import('../components/AddNewClass.vue'), //导入路由页面的路径
    }
];

const router = createRouter({    // 定义一个路由器
    history:createWebHistory(),
    routes
});

export default router;