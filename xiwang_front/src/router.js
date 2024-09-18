import { createRouter, createWebHashHistory, createWebHistory } from "vue-router"




// 2. 定义路由配置
const routes = [
  {
    path: '/',
    component: () => import('./pages/Spring.vue'),

  },
  {
    path: '/home',
    component: () => import('./pages/Home.vue'),
    children: [

    ]
  },
  {
    path: '/web',
    component: () => import('./pages/WebMark.vue'),
    children: [

    ]
  },
  {
    path: '/notes',
    component: () => import('./pages/Notes.vue'),
    children: [

    ]
  },
  {
    path: '/today',
    component: () => import('./pages/TodayPage.vue'),
    children: [

    ]
  },
  {
    path: '/signin',
    component: () => import('./pages/Sign.vue'),
    children: [

    ]
  },
  {
    path: '/books',
    component: () => import('./pages/Books.vue'),
    children: [

    ]
  },
  {
    path: '/pro',
    component: () => import('./pages/Projectpage.vue'),
    children: [

    ]
  },
  
  {
    path: '/backstage',
    component: () => import('./Backstage/BackPage.vue'),
    beforeEnter(to, from, next) {         //独享路由守卫
      if (localStorage.getItem('key') === '') {
        next()
      } else {
        alert("未登录");
        router.push("signin"); 
      }
    },
    children: [
      {
        path: '',
        component: () => import('./Backstage/BackMain.vue'),
      },
      {
        path: 'webmark',
        component: () => import('./Backstage/BackWebMark.vue'),
      },
      {
        path: 'book',
        component: () => import('./Backstage/BackBook.vue'),
      },
      {
        path: 'todo',
        component: () => import('./Backstage/BackTodo.vue'),
      },
      {
        path: 'note',
        component: () => import('./Backstage/BackNote.vue'),
      },
      {
        path: 'excerpt',
        component: () => import('./Backstage/BackExcerpt.vue'),
      },
    ]
  },




  {
    path: '/TemplateHope2',
    component: () => import('./pages/TemplateHope2.vue'),
    children: [

    ]
  },

];

// 3. 创建路由实例
const router = createRouter({
  // 4. 采用hash 模式
  history: createWebHashHistory(),
  // 采用 history 模式
  // history: createWebHistory(),
  routes, //使用上方定义的路由配置
});

/*
// 路由守卫
router.beforeEach((to, from, next) => {
    const isLogin = localStorage.ele_login ? true : false;
    if (to.path == '/login') {
      next();
    } else {
      // 是否在登录状态下
      isLogin ? next() : next('/login');
    }
  });
*/


export default router
//导出router
