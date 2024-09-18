<template>
    <div class="index">
        <!--鼠标悬停在时间上则显示日期，vue没有悬停事件，用鼠标进入事件和鼠标离开事件代替，也可以用纯css实现-->
        <div class="time" @mouseenter="onEnterTd" @mouseleave="onLeaveTd">{{ data.time.hours }}:{{ data.time.minutes }}
        </div>
        <div class="date" :style="{ visibility: data.dateVis }">{{ data.time.month }}月{{ data.time.date }}日 {{
            data.time.week
        }}
        </div>
        <div class="wether" @mouseenter="onEnterWe" @mouseleave="onLeaveWe">
            <i :class="data.wether.icon"></i>
            <p class="temp">{{ data.wether.temp }}℃</p>
            <div class="wetherDetil" :style="{ visibility: data.wetherVis }">
                <div>{{ data.wether.text }}, {{ data.wether.windDir }}</div>
                <div>体感温度: {{ data.wether.feelsLike }}℃</div>
                <div>相对湿度: {{ data.wether.humidity }}%</div>
                <div>降水量: {{ data.wether.precip }}毫米</div>
                <div>大气压强: {{ data.wether.pressure }}百帕</div>
                <div>能见度: {{ data.wether.vis }}公里</div>
                <div>云量: {{ data.wether.cloud }}%</div>
            </div>
        </div>

        <div class="enter" @click="enterHome">
            <img class="enterImg" src="../assets/enter.svg">
        </div>

        <div class="backchange" @click="backchange">
            <img class="backchangeImg" src="../assets/backchange.svg">
        </div>



        <video v-if="$store.state.background == 1" class="bgvideo" src="../assets/background/1.mp4" poster="../assets/background/1.png" autoplay loop muted playsinline></video>
        <video v-else-if="$store.state.background == 2" class="bgvideo" src="../assets/background/2.mp4"  poster="../assets/background/2.png" autoplay loop muted playsinline></video>
        <video v-else-if="$store.state.background == 3" class="bgvideo" src="../assets/background/3.mp4" poster="../assets/background/3.png" autoplay loop muted playsinline></video>
        <video v-else-if="$store.state.background == 4" class="bgvideo" src="../assets/background/4.mp4" poster="../assets/background/4.png" autoplay loop muted playsinline></video>
        
        <div v-else-if="$store.state.background == 6" class="piao"><img v-for="f in 200" src="../assets/flower1.png" class="snow"></div>
        <!--
        如果封面和首页壁纸相同，那此处就不用再添加壁纸
        <img v-else class="backimg" src="./assets/background/1.JPG">
        -->

        <a href="https://beian.miit.gov.cn/" target="_blank">苏ICP备2021046654号-1</a>

    </div>
</template>

<script>
import { onMounted, reactive } from 'vue'
import { useRouter } from "vue-router";
import axios from 'axios'          //引入axios
import { useStore } from 'vuex'


export default {
    name: 'Spring',

    setup() {
        const router = useRouter()
        const store = useStore()
        let data = reactive({
            time: {
                year: "",
                month: "",
                date: "",
                hours: "",
                minutes: "",
                seconds: "",
                week: "",
            },
            dateVis: "hidden",
            wetherVis: "hidden",
            wether: {
                icon: "",  //图标
                temp: "",  //温度
                feelsLike: "",  //体感温度
                text: "",   //天气情况
                windDir: "",    //风向
                humidity: "",  //相对湿度
                precip: "", //降水量
                pressure: "", //大气压强
                vis: "",     //能见度
                cloud: "",    //云量

            }

        })

        //鼠标进入显示日期
        function onEnterTd() {
            data.dateVis = "visible"

        }
        //鼠标离开隐藏日期
        function onLeaveTd() {
            data.dateVis = "hidden"
        }

        //鼠标进入显示天气
        function onEnterWe() {
            data.wetherVis = "visible"

        }
        //鼠标离开隐藏天气
        function onLeaveWe() {
            data.wetherVis = "hidden"
        }
        function enterHome() {
            router.push('/home')

        }

        function backchange() {
            var backGround = store.state.background
            if (backGround < 6) {
                backGround++
            } else {
                backGround = 1
            }

            window.localStorage.setItem('background', backGround)
            store.commit('bg', backGround)

        }



        onMounted(() => {
            //获取时间
            setInterval(getTime, 500);
            function getTime() {
                var dateObj = new Date();
                var year = dateObj.getFullYear(); //年
                var month = dateObj.getMonth() + 1; //月  (注意：月份+1)
                var date = dateObj.getDate(); //日
                var day = dateObj.getDay();
                var weeks = [
                    "星期日",
                    "星期一",
                    "星期二",
                    "星期三",
                    "星期四",
                    "星期五",
                    "星期六",
                ];
                var week = weeks[day]; //根据day值，获取星期数组中的星期数。
                var hours = dateObj.getHours(); //小时
                var minutes = dateObj.getMinutes(); //分钟
                var seconds = dateObj.getSeconds(); //秒
                if (month < 10) {
                    month = "0" + month;
                }
                if (date < 10) {
                    date = "0" + date;
                }
                if (hours < 10) {
                    hours = "0" + hours;
                }
                if (minutes < 10) {
                    minutes = "0" + minutes;
                }
                if (seconds < 10) {
                    seconds = "0" + seconds;
                }
                data.time.year = year;
                data.time.month = month;
                data.time.date = date;
                data.time.hours = hours;
                data.time.minutes = minutes;
                data.time.seconds = seconds;
                data.time.week = week;
            }


            //外部天气api:https://id.qweather.com/#/homepage

            axios.get('https://devapi.qweather.com/v7/weather/now', {          //前缀在main.js中设置
                params: {
                    key: "",
                    location: ""
                }
            }).then(res => {
                //console.log(res.data.now.icon);
                data.wether.icon = "qi-" + res.data.now.icon
                data.wether.temp = res.data.now.temp
                data.wether.feelsLike = res.data.now.feelsLike
                data.wether.text = res.data.now.text
                data.wether.windDir = res.data.now.windDir
                data.wether.humidity = res.data.now.humidity
                data.wether.precip = res.data.now.precip
                data.wether.pressure = res.data.now.pressure
                data.wether.vis = res.data.now.vis
                data.wether.cloud = res.data.now.cloud
            }, err => {
                console.log(err);
            })
        })





        return {
            data,
            onEnterTd,
            onLeaveTd,
            onEnterWe,
            onLeaveWe,
            enterHome,
            backchange
        }

    }


}
</script>
<style src="../css/flutter.css"  scoped></style>
<style scoped>
/*时间位置*/
.time {
    position: absolute;
    left: 50px;
    bottom: 50px;
    font-size: 120px;
    color: #fff;
    font-family: 'Bodoni MT';
    z-index: 99;
    /*font-weight: bold;
    text-shadow: 3px 3px 15px gray; /*文字阴影*/
}

/*日期位置 */
.date {
    position: absolute;
    left: 65px;
    bottom: 30px;
    font-size: 32px;
    color: #fff;
    font-family: 'Bodoni MT';
    z-index: 99;

}

/*天气位置 */
.wether {
    position: absolute;
    left: 360px;
    bottom: 70px;
    font-size: 48px;
    color: #fff;
    display: flex;
    font-family: 'Bodoni MT';
    z-index: 99;

}

.bgvideo {
    position: fixed;
    width: 100%;
    height: 100vh;
    object-fit: cover;
}

/*温度位置*/
.temp {
    position: absolute;
    bottom: 0px;
    left: 55px;
}

.wetherDetil {
    position: absolute;
    width: 400px;
    bottom: 65px;
    left: 0px;
    font-size: 18px;

}

.enter {
    background-color: aliceblue;
    opacity: 0.5;
    position: absolute;
    width: 100px;
    height: 45px;
    bottom: 80px;
    left: 0;
    right: 0;
    margin: 0 auto;
    border-radius: 30px;
    z-index: 99;
}

.enter:hover {
    box-shadow: 0 0 10px gray;
    opacity: 0.8;
}

.enterImg {
    width: 35px;
    height: 30px;
    margin-top: 8px;
    margin-left: 28px;
}



.backchange {
    background-color: aliceblue;
    opacity: 0.5;
    position: absolute;
    width: 66px;
    height: 66px;
    bottom: 30px;
    right: 30px;
    border-radius: 50%;
    z-index: 99;
}

.backchange:hover {
    box-shadow: 0 0 10px gray;
    opacity: 0.8;
}

.backchangeImg {
    width: 35px;
    height: 30px;
    margin-top: 18px;
    margin-left: 15px;
}


a {
    position: absolute;
    bottom: 10px;
    color: #666;
    z-index: 9999;
}



@media (max-width: 1224px) {

    /*时间位置*/
    .time {
        display: none;
    }

    /*日期位置 */
    .date {
        display: none;

    }

    /*天气位置 */
    .wether {
        display: none;

    }


    .enter {
        background-color: aliceblue;
        opacity: 0.5;
        position: absolute;
        width: 100px;
        height: 45px;
        bottom: 80px;
        left: 0;
        right: 0;
        margin: 0 auto;
        border-radius: 30px;
        z-index: 99;
    }

    .enter:hover {
        box-shadow: 0 0 10px gray;
        opacity: 0.8;
    }

    .enterImg {
        width: 35px;
        height: 30px;
        margin-top: 8px;
        margin-left: 28px;
    }

    .backchange {
        display: none;
    }

    /*
    .backchange {
        background-color: aliceblue;
        opacity: 0.5;
        position: absolute;
        width: 50px;
        height: 50px;
        bottom: 30px;
        right: 30px;
        border-radius: 50%;
        z-index: 99;
    }

    .backchange:hover {
        box-shadow: 0 0 10px gray;
        opacity: 0.8;
    }

    .backchangeImg {
        width: 30px;
        height: 30px;
        margin-top: 11px;
        margin-left: 10.5px;
    }

*/

}
</style>
