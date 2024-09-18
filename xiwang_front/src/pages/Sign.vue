<template>
    <div class="index">
            <div class="sign1 card">
                <input placeholder="name" type="text" v-model="data.name">
                <input placeholder="password" type="password" v-model="data.password" @keydown.enter="sign">
                <input class="buttom" type="submit" value="登  录" @click="sign">
                <p>本网站为个人使用，不提供注册功能。</p>
            </div>
    </div>

</template>

<script>
import { reactive, computed, watchEffect, onMounted } from 'vue'
import axios from 'axios'          //引入axios
import {useRouter} from "vue-router";
export default {
    //组件名
    name: 'Sign',
    setup() {
        const router=useRouter()
        let data = reactive({
            name: "",
            password: "",
        })



        function sign() {
            const params = new URLSearchParams();
            params.append('name', data.name);
            params.append('password', data.password);
            axios.post("api/signin/", params)
                .then(function (response) {
                    if (response.data.ret == 0) {
                        alert("登录成功")
                        window.localStorage.setItem('key', '')
                        router.back();
                    } else {
                        alert("登录失败")
                    }
                })
                .catch(function (error) {
                    console.log(error);
                });
        }


        //数据和函数都要返回
        return {
            data,
            sign
        }
    },



}
</script>

<style scoped>

.sign1 {
    width: 400px;
    height: 320px;
    font-family: MiSans;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center
}


input {
    outline: 0;
    background: #f2f2f2;
    width: 72%;
    border: 0;
    margin: 0 0 15px;
    padding: 12px;
    box-sizing: border-box;
    font-size: 22px;
}

.buttom {
    font-family: MiSans;
    outline: 0;
    background: #4CAF50;
    width: 72%;
    height: 50px;
    border: 0;
    color: #FFFFFF;
    font-size: 22px;
    cursor: pointer;
    margin-top: 20px;
}

.buttom:hover {
    font-size: 24px;
    background: #43A047;
}

p {
    color: darkgray;
}




@media (max-width: 1224px) {
.index{
    width: 100vw;
    height: 100vh;
}    
.sign1 {
    width: 80vw;
    height: 72vw;
    font-family: MiSans;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center
}


input {
    outline: 0;
    background: #f2f2f2;
    width: 72%;
    border: 0;
    margin: 0 0 15px;
    padding: 12px;
    box-sizing: border-box;
    font-size: 22px;
}

.buttom {
    font-family: MiSans;
    outline: 0;
    background: #4CAF50;
    width: 72%;
    height: 50px;
    border: 0;
    color: #FFFFFF;
    font-size: 22px;
    cursor: pointer;
    margin-top: 20px;
}

.buttom:hover {
    font-size: 24px;
    background: #43A047;
}

p {
    color: darkgray;
}

}

</style>
