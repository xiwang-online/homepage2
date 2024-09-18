import { createStore } from 'vuex'

export default createStore({
    state: {       // 准备state——用于存储数据
        count:100,
        background:1,
    },

    actions: {   // 准备actions——用于响应组件中的动作
    },


    mutations: {    // 准备mutations——用于操作数据（state）
        bg(state,num){
            state.background=num
        }
    },

})
