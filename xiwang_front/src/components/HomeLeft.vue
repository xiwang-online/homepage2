<template>
    <div class="home_logo"><img class="logo" src="../assets/logo.png" alt="logo"></div>
    <div class="card home_yiyan">
        <div class="qian yinhao">“</div>
        <div class="hou yinhao">”</div>
        <div class="word" v-if="data.yiyanid == 0">HOPE的个人主页</div>
        <div v-else-if="data.yiyanid == 1"><img class="code" src="../assets/qqcode.png"></div>
        <div v-else-if="data.yiyanid == 2"><img class="code" src="../assets/weixincode.png"></div>
        <div class="word" v-else-if="data.yiyanid == 3">xxxxx@qq.com</div>
        <div class="word" v-else-if="data.yiyanid == 4">github.com/xxxxx</div>
        <div v-else-if="data.yiyanid == 5">
            <div class="yiyan">{{data.yiyan}}</div>
            <div class="yiyanpro">{{data.yiyanpro}}</div>
        </div>




    </div>
    <div :class="data.qqClass" @mouseenter="onEnter" @mouseleave="onLeave">
        <img class="qq" src="../assets/QQ.png" alt="qq" @mouseenter="qqEnter(1)" @mouseleave="qqLeave">
        <img class="qq wechat" src="../assets/weixin.png" alt="wechat" @mouseenter="qqEnter(2)" @mouseleave="qqLeave">
        <img class="qq mail" src="../assets/youxiang.png" alt="mail" @mouseenter="qqEnter(3)" @mouseleave="qqLeave">
        <img class="qq github" src="../assets/github-fill.png" alt="github" @mouseenter="qqEnter(4)"
            @mouseleave="qqLeave" @click="entergit">

    </div>


</template>

<script>
import { reactive, computed, watchEffect, onMounted } from 'vue'
import axios from 'axios'
export default {
    //组件名
    name: 'HomeLeft',


    setup() {
        let data = reactive({
            qqClass: "home_qq",
            yiyanid: 0,
            yiyan: "吾日三省吾身，github有没有提交新的代码？个人主页有没有写新文章？有没有学到新的东西？",
            yiyanpro: ""

        })


        onMounted(() => {
            if (localStorage.getItem('key') === 'value') {
                data.yiyanid = 5
            } else {
                data.yiyanid = 0
            }


            axios.post("api/excerpt/", {
                "action": "list_excerpt",
            })
                .then(function (value) {
                    const a = Math.random() * value.data.retlist.length;
                    data.yiyan = value.data.retlist[Math.floor(a)]["content"];
                    data.yiyanpro = "--" + value.data.retlist[Math.floor(a)]["provenance"];
                })
                .catch(function (reason) {
                    console.log(reason)
                })

        })


        //鼠标进入显示背景
        function onEnter() {
            data.qqClass = "home_qq card"

        }
        //鼠标离开隐藏背景
        function onLeave() {
            data.qqClass = "home_qq"
        }

        function qqEnter(id) {
            data.yiyanid = id
        }

        function qqLeave() {
            if (localStorage.getItem('key') === '') {
                data.yiyanid = 5
            } else {
                data.yiyanid = 0

            }

        }

        function entergit() {
            window.open("https://github.com/xxxxx")

        }



        //数据和函数都要返回
        return {
            data,
            onEnter,
            onLeave,
            qqEnter,
            qqLeave,
            entergit

        }
    },




}
</script>

<style scoped>
@font-face {
    font-family: 'Highlander';
    src: url(../font/Highlander-3.woff2);
    font-weight: 100;
}


.home_logo {
    width: 460px;
    height: 120px;
    margin-top: 60px;
    margin-bottom: 10px;
    margin-right: 40px;
    margin-left: 40px;
    font-size: 55px;
    font-family: Highlander;
    vertical-align: top;
    text-align: center;
}

.home_yiyan {
    width: 460px;
    height: 200px;
    margin-bottom: 5px;
    margin-right: 40px;
    margin-left: 40px;
    position: relative;
}

.home_qq {
    width: 460px;
    height: 55px;
    margin-top: 10px;
    margin-bottom: 0px;
    margin-right: 40px;
    margin-left: 40px;

}

.logo {
    width: 120px;
    margin-right: 10px;

}

.yinhao {
    font-size: 90px;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif
}

.qian {
    position: absolute;
    top: -10px;
    left: 10px;
}

.hou {
    position: absolute;
    bottom: -40px;
    right: 10px;

}

.word {
    padding: 70px 0;
    text-align: center;
    font-size: 36px;
    font-family: FZYaoti;
}

.yiyan {
    padding: 35px 35px;
    text-align: left;
    font-size: 24px;
    font-family: FZYaoti;
}

.yiyan::before {
    content: "\00a0\00a0\00a0\00a0";

}


.yiyanpro {
    position: absolute;
    bottom: 20px;
    right: 50px;
    font-size: 18px;
}

.qq {
    width: 40px;
    margin-right: 15px;
    margin-top: 8px;
    margin-left: 10px;
}



.code {
    width: 180px;
    margin-left: 140px;
    margin-top: 10px;


}


@media (max-width: 1224px) {
    .home_logo {
        width: 80vw;
        height: auto;
        font-size: 14vw;
        margin: 10vw 10vw 3vw 10vw;
        vertical-align: top;
    }

    .logo {
        display: none;

    }

    .home_yiyan {
        width: 80vw;
        height: 30vw;
        margin: 0 10vw;
        position: relative;
    }





    .yinhao {
        font-size: 12vw;
        font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif
    }

    .qian {
        position: absolute;
        top: -1vw;
        left: 3px;
    }

    .hou {
        position: absolute;
        bottom: -6vw;
        right: 2vw;

    }

    .word {
        padding: 10vw 0;
        text-align: center;
        font-size: 8vw;
        font-family: FZYaoti;
    }

    .yiyan {
        padding: 6vw 6vw;
        text-align: left;
        font-size: 4vw;
        font-family: FZYaoti;
    }


    .yiyanpro {
        position: absolute;
        bottom: 2vw;
        right: 7vw;
        font-size: 2.5vw;
    }





    .home_qq {
        width: 80vw;
        height: 15vw;
        margin: 2vw 10vw;
        display: flex;
        justify-content: center;
        align-items: center;


    }

    .qq {
        width: 10vw;
        margin: 0 4vw;

    }



    .code {
        width: 25vw;
        margin-left: 27.5vw;
        margin-top: 10px;


    }

}
</style>