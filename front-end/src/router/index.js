import { pa } from "element-plus/es/locale/index.mjs";
import { createRouter, createWebHistory } from "vue-router";  //导入路由
/*
GolbalRouter
SAS
VSS
RAS
*/ 
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
        component: () => import('../components/menu.vue')
    },
    // SAS
    {
        path: '/SAS',
        name: 'SAS',
        component: () => import('../components/SAS.vue')
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
    {        path: '/EditPersonFile',
        name: 'EditPersonFile',
        component: () => import('../components/EditPersonFile.vue')
    },
    {
        path:'/AccountManage', // 要路由到的url路径
        name:'AccountManage',
        component:()=>import('../components/AccountManage.vue'), //导入路由页面的路径
    },
    {
        path:'/NewAccount', // 要路由到的url路径
        name:'NewAccount',
        component:()=>import('../components/NewAccount.vue'), //导入路由页面的路径
    },
    {
        path:'//AddLargeAccount', // 要路由到的url路径
        name:'AddLargeAccount',
        component:()=>import('../components/AddLargeAccount.vue'), //导入路由页面的路径
    },
    {
        path:'/ClassManage', // 要路由到的url路径
        name:'ClassManage',
        component:()=>import('../components/ClassManage.vue'), //导入路由页面的路径
    },
    {
        path:'/AddNewClass', // 要路由到的url路径
        name:'AddNewClass',
        component:()=>import('../components/AddNewClass.vue'), //导入路由页面的路径
    },
    {
        path:'/EditClass', // 要路由到的url路径
        name:'EditClass',
        component:()=>import('../components/EditClass.vue'), //导入路由页面的路径
    },
    //VSS 
    {
        path: '/VSS',
        name: 'VSS',
        component: () => import('../components/VSS.vue')
    },
    {//????????不知幹麼的????
        path: '/back_vss',
        name: 'back_vss',
        component: () => import('../components/VSS.vue')
    },
    {
        path: '/EditRentalSurveyForm_S',
        name: 'EditRentalSurveyForm_S',
        component: () => import('../components/EditRentalSurveyForm_S.vue')
    },
    {
        path: '/EditRentalSurveyForm_T',
        name: 'EditRentalSurveyForm_T',
        component: () => import('../components/EditRentalSurveyForm_T.vue')
    },
    {
        path: '/Successform',
        name: 'Successform',
        component: () => import('../components/Successform.vue')
    },
    {
        path: '/CheckStudentStatus/:id?',
        name: 'CheckStudentStatus',
        props: true,
        component: () => import('../components/CheckStudentStatus.vue')
    },
    {
        path: '/CheckClassStatus',
        name: 'CheckClassStatus',
        component: () => import('../components/CheckClassStatus.vue')
    },
    {
        path: '/CheckStudentForm/:id',
        name: 'CheckStudentForm',
        props: true,
        component: () => import('../components/CheckStudentForm.vue')
    },
    {
        path: '/QueryStudentForm/:id',
        name: 'QueryStudentForm',
        props: true,
        component: () => import('../components/QueryStudentForm.vue')
    },
    //RAS
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