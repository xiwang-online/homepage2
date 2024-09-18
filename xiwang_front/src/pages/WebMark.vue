<template>
    <div class="index">
        <div class="main" v-if="data.show == false">
            <div class="searchbar card">
                <input class="input" type="text" placeholder="搜索" autocomplete="off" v-model="data.chooseCon"
                    @keyup.enter="search">
                <div class="searchimg">
                    <img @click="choosebar" class="img" src="../assets/bing.svg" v-if="data.searchChoose == 0">
                    <img @click="choosebar" class="img" src="../assets/baidu.svg" v-if="data.searchChoose == 1">
                    <img @click="choosebar" class="img" src="../assets/guge.svg" v-if="data.searchChoose == 2">
                    <img @click="choosebar" class="img" src="../assets/csdn.svg" v-if="data.searchChoose == 3">
                    <div v-if="data.chooseShow == true" class="choose card">
                        <div class="chooseOpt" @click="chooseOne"><img class="img" src="../assets/bing.svg">必应</div>
                        <div class="chooseOpt" @click="chooseTwo"><img class="img" src="../assets/baidu.svg">百度</div>
                        <div class="chooseOpt" @click="chooseThree"><img class="img" src="../assets/guge.svg">谷歌</div>
                        <div class="chooseOpt" @click="chooseFour"><img class="img" src="../assets/csdn.svg">CSDN</div>
                    </div>
                </div>
                <div class="searchbtn" @click="search">
                    <img class="but" src="../assets/sousuo.svg">
                </div>
            </div>


            <div class="web">
                <a href="https://bilibili.com" target="_blank">
                    <div class="card webcard">

                        <img class="webimg" src="../assets/bilibili.svg">
                        <p>Bilibili</p>

                    </div>
                </a>
                <a href="https://github.com" target="_blank">
                    <div class="card webcard">
                        <img class="webimg" src="../assets/github.svg">
                        <p>Github</p>
                    </div>
                </a>
                <a href="https://www.deepl.com/zh/translator" target="_blank">
                    <div class="card webcard">
                        <img class="webimg" src="../assets/deepl.svg">
                        <p>DeepL翻译</p>
                    </div>
                </a>
                <a href="https://mail.qq.com/" target="_blank">
                    <div class="card webcard">
                        <img class="webimg" src="../assets/youxiang.svg">
                        <p>QQ邮箱</p>
                    </div>
                </a>
                <a href="https://www.zhihu.com/" target="_blank">
                    <div class="card webcard">
                        <img class="webimg" src="../assets/zhihu.svg">
                        <p>知乎</p>
                    </div>
                </a>
                <a href="https://666bfg.com/" target="_blank">
                    <div class="card webcard">
                        <img class="webimg" src="../assets/emi.svg">
                        <p>避风港</p>
                    </div>
                </a>
                <a href="https://weread.qq.com/" target="_blank">
                    <div class="card webcard">
                        <img class="webimg" src="../assets/dushu.svg">
                        <p>微信读书</p>
                    </div>
                </a>
                <a href="https://yiyan.baidu.com/" target="_blank">
                    <div class="card webcard">
                        <img class="webimg" src="../assets/wxyy.svg">
                        <p>文心一言</p>
                    </div>
                </a>
                <a href="https://www.notion.so" target="_blank">
                    <div class="card webcard">
                        <img class="webimg" src="../assets/Notion.svg">
                        <p>Notion</p>
                    </div>
                </a>
                <a href="https://www.v2ex.com/" target="_blank">
                    <div class="card webcard">
                        <img class="webimg" src="../assets/v2ex.svg">
                        <p>V2EX</p>
                    </div>
                </a>

            </div>

            <div class="more" @click="change">
                更多...
            </div>
        </div>
        <div class="main" v-if="data.show == true">
            <div class="webmark card">
                <div class="webmarkin">
                    <p class="webmarkp" v-for="web in data.webs" :key="web.id">
                        <a :href="web.weburl" target="_blank">{{ web.webname }}</a>
                    </p>
                </div>
            </div>

            <div class="more" @click="change">
                返回...
            </div>
        </div>
    </div>

</template>

<script>
import { reactive, computed, watchEffect, onMounted } from 'vue'
import axios from 'axios'          //引入axios
export default {
    //组件名
    name: 'WebMark',
    setup() {
        let data = reactive({
            show: false,
            webs: [],
            search: ["baidu", "guge", "csdn"],
            searchChoose: 0,
            chooseShow: false,
            chooseCon: ""


        })



        //生命周期函数，
        //onMounted：在初始化页面完成后执行
        onMounted(() => {
            axios.post("api/web/", {
                "action": "list_web",
            })
                .then(function (value) {
                    data.webs = value.data.retlist;
                })
                .catch(function (reason) {
                    console.log(reason)
                })

        })

        function change() {
            data.show = !data.show
        }

        function choosebar() {
            data.chooseShow = !data.chooseShow
        }
        function chooseOne() {
            data.chooseShow = !data.chooseShow
            data.searchChoose = 0
        }
        function chooseTwo() {
            data.chooseShow = !data.chooseShow
            data.searchChoose = 1
        }
        function chooseThree() {
            data.chooseShow = !data.chooseShow
            data.searchChoose = 2
        }
        function chooseFour() {
            data.chooseShow = !data.chooseShow
            data.searchChoose = 3
        }

        function search() {

            if (data.searchChoose == 0) {
                window.open("https://cn.bing.com/search?q=" + data.chooseCon)
            } else if (data.searchChoose == 1) {
                window.open("https://www.baidu.com/s?wd=" + data.chooseCon)

            } else if (data.searchChoose == 2) {
                window.open("https://www.google.com/search?q=" + data.chooseCon)

            }else {
                window.open("https://so.csdn.net/so/search?q=" + data.chooseCon)

            }

        }



        //数据和函数都要返回
        return {
            data,
            change,
            choosebar,
            chooseOne,
            chooseTwo,
            chooseThree,
            chooseFour,
            search
        }
    },



}
</script>


<style scoped>
.main {
    display: flex;
    /*水平垂直居中*/
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 100%;
    flex-direction: column;
}

.searchbar {
    position: relative;
    background-color: whitesmoke;
    height: 43px;
    width: 600px;
    border-radius: 30px;
    margin: 50px 0;

}

.input {
    position: absolute;
    outline: 0;
    border: none;
    width: 500px;
    height: 100%;
    padding: 0 50px;
    color: inherit;
    background-color: transparent;
    font-size: 14px;
    text-align: center;

}

.searchimg {
    position: absolute;
    top: 7px;
    left: 8px;
}

.choose {
    position: absolute;
    top: 40px;
    width: 120px;
    height: 160px;
    background-color: whitesmoke;
    cursor: pointer;


}

.chooseOpt {
    margin-top: 5px;
    padding: 4px 0px 4px 10px;
    font-size: 18px;
}

.chooseOpt:hover {
    background-color: darkgray;
}

.searchbtn {
    position: absolute;
    left: 565px;
    top: 8px;
    cursor: pointer;
}

img {
    width: 25px;
    margin-right: 10px;
}

.web {
    display: flex;
    width: 800px;
    flex-wrap: wrap;
    justify-content: center
}

.webcard {
    width: 90px;
    height: 90px;
    margin: 15px 30px;
    display: flex;
    /*水平垂直居中*/
    align-items: center;
    justify-content: center;
    flex-direction: column;
    font-size: 14px;
    cursor: pointer;
    color: black;
    font-family: MiSans;
}


.webimg {
    width: 30px;
    margin-bottom: 10px;
    margin-right: 0;
}

.webimg:hover {
    width: 35px;
}

.more {
    margin: 30px 0;
    width: 740px;
    height: 30px;
    color: darkgrey;
    text-align: center;
    font-size: 20px;
    cursor: pointer;
}

.more:hover {
    background-color: rgb(248, 244, 237, 0.5);
    box-shadow: 4px 4px 5px rgb(0, 0, 0, 0.2);
    border-radius: 5px;
    color: black;

}

.webmark {
    width: 800px;
    height: 600px;
    margin-top: 50px;

}

.webmarkin {
    width: 750px;
    height: 500px;
    margin: 40px 0px 60px 40px;
    overflow: scroll;
    overflow-y: auto;
    overflow-x: hidden;
    font-family: MiSans;
    font-size: 24px;
}

.webmarkp {
    padding: 8px;
}

.webmarkp::before {
    content: "🔗";
    display: inline-block;
    margin-right: 0.3em;
    font-size: 1em;
    vertical-align: middle;
}

a:hover {
    color: #e74c3c;
}


/*滚动条样式*/
::-webkit-scrollbar {
    width: 14px;
    height: 14px;
}

::-webkit-scrollbar-track,
::-webkit-scrollbar-thumb {
    border-radius: 999px;
    border: 5px solid transparent;
}

::-webkit-scrollbar-track {
    box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.2) inset;
}

::-webkit-scrollbar-thumb {
    min-height: 20px;
    background-clip: content-box;
    box-shadow: 0 0 0 5px rgba(0, 0, 0, 0.2) inset;
}

::-webkit-scrollbar-corner {
    background: transparent;
}


@media (max-width: 1224px) {
    .main {
        display: flex;
        /*水平垂直居中*/
        align-items: center;
        justify-content: center;
        width: 100%;
        height: 100%;
        flex-direction: column;
    }

    .searchbar {
        position: relative;
        background-color: whitesmoke;
        height: 43px;
        width: 80vw;
        border-radius: 30px;
        margin: 50px 0 20px 0;

    }

    .input {
        position: absolute;
        outline: 0;
        border: none;
        width: 60vw;
        height: 100%;
        padding: 0 10vw;
        color: inherit;
        background-color: transparent;
        font-size: 14px;
        text-align: center;

    }

    .searchimg {
        position: absolute;
        top: 7px;
        left: 8px;
    }

    .choose {
        position: absolute;
        top: 40px;
        width: 120px;
        height: 120px;
        background-color: whitesmoke;
        cursor: pointer;


    }

    .chooseOpt {
        margin-top: 5px;
        padding: 4px 0px 4px 10px;
        font-size: 18px;
    }

    .chooseOpt:hover {
        background-color: darkgray;
    }

    .searchbtn {
        position: absolute;
        left: 71vw;
        top: 8px;
        cursor: pointer;
    }

    img {
        width: 25px;
        margin-right: 10px;
    }

    .web {
        display: flex;
        width: 100vw;
        flex-wrap: wrap;
        justify-content: center
    }

    .webcard {
        width: 90px;
        height: 90px;
        margin: 12px 15px;
        display: flex;
        /*水平垂直居中*/
        align-items: center;
        justify-content: center;
        flex-direction: column;
        font-size: 14px;
        cursor: pointer;
        color: black;
        font-family: MiSans;
    }


    .webimg {
        width: 30px;
        margin-bottom: 10px;
        margin-right: 0;
    }

    .webimg:hover {
        width: 35px;
    }

    .more {
        margin: 30px 0;
        width: 80vw;
        height: 30px;
        color: darkgrey;
        text-align: center;
        font-size: 20px;
        cursor: pointer;
        
    }

    .more:hover {
        background-color: rgb(248, 244, 237, 0.5);
        box-shadow: 4px 4px 5px rgb(0, 0, 0, 0.2);
        border-radius: 5px;
        color: black;

    }

    .webmark {
        width: 80vw;
        height: auto;
        margin-top: 40px;

    }

    .webmarkin {
        width: 100%;
        height: auto;
        margin: 20px 0px 30px 10px;
        overflow:hidden;
        font-family: MiSans;
        font-size: 20px;
    }

    .webmarkp {
        padding: 5px;
    }

    .webmarkp::before {
        content: "🔗";
        display: inline-block;
        margin-right: 0.2em;
        font-size: 0.8em;
        vertical-align: middle;
    }

    a:hover {
        color: #e74c3c;
    }


}
</style>
