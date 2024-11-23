import { createRouter, createWebHistory } from 'vue-router'
// import MapView from '@/views/MapView.vue'
import HomeView from '@/views/HomeView.vue'
// import PortfolioView from '@/views/PortfolioView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LoginView from '@/views/LoginView.vue'
import PortfolioMain from '@/views/PortfolioMain.vue'
import QuestionPage from '@/components/pages/questions/QuestionPage.vue'
import PortResults from '@/components/pages/questions/PortResults.vue'
import MapView from '@/views/MapView.vue'
import Recommend from '@/views/Recommend.vue'
// import SaveRecommendView from '@/views/SaveRecommendView.vue'
// import PortfolioListView from '@/views/PortfolioListView.vue'
// import CurrencyExchangeView from '@/views/미리작업/CurrencyExchangeView.vue'
// import MyPageView from '@/views/MyPageView.vue'
// import ProductDetailView from '@/views/ProductDetailView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/AboutView.vue'),
    // },
    {
      path:'/map',
      name:'map',
      component: MapView,
    },
    // {
    //   path:'/portfolio',
    //   name:'portfolio',
    //   component: PortfolioView,
    // },
    // {
    //   path: '/portfolio/:id',
    //   name: 'portlist',
    //   component: PortfolioListView
    // },
    // {
    //   path: '/currency_exchange',
    //   name: 'currencyExchange',
    //   component: CurrencyExchangeView
    // },
    {
			path: '/signup',
			name: 'SignUpView',
			component: SignUpView
		},
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/portfolio_main/',
      name: 'portfolio_main',
      component: PortfolioMain
    },
    { 
      path: '/question/:id', 
      name: 'QuestionPage', 
      component: QuestionPage, 
      props: true 
    },
    { 
      path: '/results', 
      name: 'Results', 
      component: PortResults 
    },
    {
      path: '/recommend',
      name: 'Recommend',
      component: Recommend

    }
    // {
    //   path: '/saveRecommend',
    //   name: 'saveRecommend',
    //   component: SaveRecommendView
    // },
    // {
    //   path: '/mypage/:id',
    //   name: 'mypage',
    //   component: MyPageView
    // },
    // {
    //   path: '/productDetail/:id',
    //   name: 'productDetail',
    //   component: ProductDetailView,
    //   props: true, // params를 props로 전달
    // },

  ],
})

export default router
