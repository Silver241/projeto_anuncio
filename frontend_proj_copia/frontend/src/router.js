import {createRouter, createWebHistory} from 'vue-router'
import Home from '@/views/home.vue'
import SignUp from './views/sign_up.vue'
import Login from './views/login.vue'
import ChoiceAd from './views/choice_ad.vue'
import loged_user from './views/loged_user.vue'


const routes =[
    {
        path: '/',
        name: 'home',
        component: Home
    },
    {
        path: '/sign_up',
        name: 'sign_up',
        component: SignUp
    },
    {
        path: '/login',
        name: 'login',
        component: Login
    },
    {
        path: '/choice_ad',
        name: 'choice_ad',
        component: ChoiceAd
    },
    {
        path: '/loged_user',
        name: 'loged_user',
        component: loged_user
    }
]

const router =createRouter(
    {
        history: createWebHistory(),
        routes
    }
)

export default router;