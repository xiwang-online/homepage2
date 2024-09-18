<template>
    <div class="common-layout">
        <el-container class="container">
            <el-aside class="aside">
                <div class="title" @click="bs">
                    后台
                </div>
                <el-divider />
                <el-menu active-text-color="#ffffff" background-color="#151628" class="el-menu-vertical-demo"
                    text-color="#a5a5a5">
                    <el-menu-item index="1" @click="webmark">
                        <span>网址集</span>
                    </el-menu-item>
                    <el-menu-item index="2" @click="book">
                        <span>书单</span>
                    </el-menu-item>
                    <el-menu-item index="3" @click="todo">
                        <span>日程</span>
                    </el-menu-item>
                    <el-menu-item index="4" @click="note">
                        <span>记事本</span>
                    </el-menu-item>
                    <el-menu-item index="5" @click="excerpt">
                        <span>摘录</span>
                    </el-menu-item>
                    <el-menu-item index="6" @click="timer">
                        <span>计时器</span>
                    </el-menu-item>
                </el-menu>

            </el-aside>
            <el-main class="main">
                <RouterView></RouterView>
            </el-main>
        </el-container>
    </div>
</template>
  
<script>
import { reactive, computed, watchEffect, onMounted } from 'vue'
import axios from 'axios'          //引入axios
import router from '../router'
export default {
    //组件名
    name: 'BackPage1',
    setup() {
        let data = reactive({

        })


        function webmark() {
            router.replace('/backstage/webmark')

        }

        function book() {
            router.replace('/backstage/book')

        }

        function todo() {
            router.replace('/backstage/todo')

        }

        function note() {
            router.replace('/backstage/note')

        }

        function excerpt() {
            router.replace('/backstage/excerpt')

        }

        function timer() {
            router.replace('/backstage/timer')

        }
        function bs() {
            router.replace('/backstage/')

        }



        //生命周期函数，
        //onMounted：在初始化页面完成后执行
        onMounted(() => {

        })


        //数据和函数都要返回
        return {
            data,
            webmark,
            book,
            todo,
            note,
            excerpt,
            timer,
            bs
        }
    },



}
</script>
<style scoped>
.common-layout {
    width: 100%;
    height: 100vh;
}

.container {
    width: 100%;
    height: 100%;
}

.aside {
    background-color: #151628;
    width: 200px;
}

.main {
    background-color: #151628;
    padding: 0;
}

.title {
    font-size: 34px;
    color: white;
    margin: 20px 20px;
    font-weight: 900;
}


span {
    font-size: 24px;
}

.el-menu-vertical-demo{
    height: 70%;
}


@media (max-width: 1224px) {
.aside{
    display: none;
    width: 0px;
}




}

</style>
  