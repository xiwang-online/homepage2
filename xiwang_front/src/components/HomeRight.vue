<template>
    <div class="home_right_top">
        <div class="card home_time" @mouseenter="onEnter" @mouseleave="onLeave">
            <div class="year" v-if="data.showdata == 0">{{ data.time.year }}年{{ data.time.month }}月{{ data.time.date }}日
                {{ data.time.week }}
            </div>
            <div class="year" v-if="data.showdata == 1">本站已跌跌撞撞运行：
            </div>
            <div class="hour" v-if="data.showdata == 0">{{ data.time.hours }}:{{ data.time.minutes }}:{{ data.time.seconds
            }}</div>
            <div class="hourold" v-if="data.showdata == 1">{{ data.timeold }}</div>
            <div class="wether">苏州 {{ data.wether.text }} {{ data.wether.temp }}℃ {{ data.wether.windDir }}</div>
        </div>
        <div class="card home_today">
            <TodaySim v-if="data.todayshow == 1"></TodaySim>
            <TodaySimNo v-if="data.todayshow == 0"></TodaySimNo>
        </div>
    </div>
    <div class="home_right_center"></div>
    <div class="home_right_buttom">
        <div class="home_right_buttom_top">
            <div class="card home_link" @click="notion">
                <img class="link" src="../assets/biji.svg" alt="note">
                <p>文档笔记</p>
            </div>

            <div class="card home_link" @click="webmark">
                <img class="link" src="../assets/wangzhi.svg" alt="web">
                <p>网址集</p>
            </div>

            <div class="card home_link" @click="books">
                <img class="link" src="../assets/shudan.svg" alt="book">
                <p>书单</p>
            </div>

        </div>
        <div class="home_right_buttom_buttom">

            <div class="card home_link" @click="pro">
                <img class="link" src="../assets/yunpan.svg" alt="cloud">
                <p>个人项目</p>
            </div>


            <div class="card home_link" @click="notes">
                <img class="link" src="../assets/jishi.svg" alt="notebook">
                <p>博客</p>
            </div>
            <!--
            <div class="card home_link" @click="notes">
                <img class="link" src="../assets/jishi.svg" alt="notebook">
                <p>记事本</p>
            </div>
            -->
            <div class="card home_link" @click="backstage">
                <img class="link" src="../assets/houtai.svg" alt="back">
                <p>后台</p>
            </div>
        </div>
    </div>
</template>

<script>
import { reactive, computed, watchEffect, onMounted } from 'vue'
import axios from 'axios'          //引入axios
import TodaySim from './TodaySim.vue'
import TodaySimNo from './TodaySimNo.vue'
import { useRouter } from "vue-router";
export default {
    //组件名
    name: 'HomeRight',

    components: { TodaySim, TodaySimNo },


    setup() {
        const router = useRouter()
        let data = reactive({
            showdata: 0,
            timeold: "",
            todayshow: 0,  //登录后才显示日程
            time: {
                year: "",
                month: "",
                date: "",
                hours: "",
                minutes: "",
                seconds: "",
                week: "",
            },
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

        onMounted(() => {
            //是否登录
            if (localStorage.getItem('key') === 'value') {
                data.todayshow = 1
            } else {
                data.todayshow = 0
            }




            //获取时间
            setInterval(getTime, 250);
            function getTime() {
                var dateObj = new Date();   //当前时间
                var grt = new Date("");//建站时间
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



                //计算运行时间
                var days = (dateObj - grt) / 1000 / 60 / 60 / 24;
                var dnum = Math.floor(days);   //天
                var hours = (dateObj - grt) / 1000 / 60 / 60 - (24 * dnum);
                var hnum = Math.floor(hours);   //时
                if (String(hnum).length == 1) {
                    hnum = "0" + hnum;
                }
                var minutes = (dateObj - grt) / 1000 / 60 - (24 * 60 * dnum) - (60 * hnum);
                var mnum = Math.floor(minutes);  //分
                if (String(mnum).length == 1) {
                    mnum = "0" + mnum;
                }
                var seconds = (dateObj - grt) / 1000 - (24 * 60 * 60 * dnum) - (60 * 60 * hnum) - (60 * mnum);
                var snum = Math.round(seconds);    //秒
                if (String(snum).length == 1) {
                    snum = "0" + snum;
                }

                data.timeold = dnum + "天" + hnum + "时" + mnum + "分" + snum + "秒"

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




        function webmark() {
            router.push('/web')
        }

        function notes() {
            //router.push('/notes')
            window.open("")//在新窗口打开
            //window.location.href="";//当前窗口打开
        }
        function books() {
            router.push('/books')
        }
        function backstage() {
            router.push('/backstage')
        }

        function notion() {
            window.open("")
            //window.location.href="";
        }
        function pro() {
            router.push('/pro')
        }

        function login() {
            router.push('/signin')

        }



        function onEnter() {
            data.showdata = 1

        }

        function onLeave() {
            data.showdata = 0

        }



        //数据和函数都要返回
        return {
            data,
            webmark,
            notes,
            books,
            backstage,
            notion,
            pro,
            onEnter,
            onLeave,
            login


        }
    },




}
</script>

<style scoped>
@font-face {
    font-family: 'UnidreamLED';
    src: url(../font/UnidreamLED.ttf);
    font-weight: 100;
}



.home_right_top {
    display: flex;
}


.home_time {
    width: 310px;
    height: 190px;
    margin-right: 24px;
}


.home_today {
    width: 310px;
    height: 190px;
    margin-right: 40px;

    
}


.home_right_center {
    height: 50px;
}

.home_right_buttom {
    display: flex;
    flex-direction: column;
    /*垂直排列*/

}

.home_right_buttom_top {
    display: flex;
}

.home_right_buttom_buttom {
    display: flex;
    margin-top: 35px;
}


.home_link {
    width: 200px;
    height: 95px;
    margin-right: 22px;
    text-align: center;
    font-size: 20px;
    font-family: MiSans;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
}

.home_link:hover {
    font-size: 22px;
}

.year {
    text-align: center;
    font-size: 20px;
    font-family: MiSans;
    margin-top: 20px;
}

.hour {
    text-align: center;
    font-size: 60px;
    font-family: UnidreamLED;
    margin-top: 10px;
}


.hourold {
    text-align: center;
    font-size: 30px;
    margin: 25px 0;
}

.wether {
    text-align: center;
    font-size: 20px;
    font-family: MiSans;
    margin-top: 10px;
}

.link {
    width: 35px;
    margin-right: 5px;
}






@media (max-width: 1224px) {

    .home_right_top {
        display: flex;
    }


    .home_time {
        display: none;
    }


    .home_today {
        width: 80vw;
        height: auto;
        margin: 0vw 10vw;
    }

    .home_right_center {
        display: none;
    }

    .home_right_buttom {
        display: flex;
        flex-direction: column;
        margin-top: 20px;
        /*垂直排列*/

    }

    .home_right_buttom_top {
        display: flex;
        flex-direction: column;
        /*垂直排列*/
        align-items: center
    }

    .home_right_buttom_buttom {
        display: flex;
        flex-direction: column;
        /*垂直排列*/
        align-items: center;
        margin-top: 0;
        margin-bottom: 20vw;
    }


    .home_link {
        width: 80vw;
        height: 95px;
        margin: 15px 10vw;
        text-align: center;
        font-size: 20px;
        font-family: MiSans;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
    }

    .home_link:hover {
        font-size: 22px;
    }



    .link {
        width: 35px;
        margin-right: 5px;
    }
}
</style>
