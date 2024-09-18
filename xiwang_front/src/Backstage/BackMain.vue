<template>
    <div class="main">
        <div class="mainDiv">
            <div class="middle">

                <!--移动端菜单-->
                <div class="mobileM">
                    <div>菜单</div>
                    <div class="menu">
                        <span @click="webmark">网址 </span>
                    
                        <span @click="book">书单 </span>
             
                        <span @click="todo">日程 </span>
        
                        <span @click="note">记事 </span>
       
                        <span @click="excerpt">摘录 </span>


</div>

                </div>
                

                <div class="stations">
                    <div>子站后台</div>
                    <div class="buts">
                        <a href="" target="_blank">
                            <div class="but"><img src="../assets/backstage/note.svg">
                                <p>Trilium</p>
                            </div>
                        </a>
                        <a href="" target="_blank">
                            <div class="but"><img src="../assets/backstage/umamin.svg">
                                <p>Umamin</p>
                            </div>
                        </a>
                    </div>
                </div>
                <div class="stations">
                    <div>后台记事本</div><img class="editbut" width="30" src="../assets/bianji.svg" @click="editChange">
                    <div class="noteItem">
                        <div class="show" v-html="data.noteHtml" v-if="!(data.editShow)"></div>
                        <textarea class="edit" v-if="data.editShow" @blur="editChange"
                            v-model="data.note"></textarea>

                    </div>

                </div>
            </div>
            <div class="right">
                <div class="calM">
                    <Calendar :select="select"></Calendar>
                </div>
                <div class="day">
                    <div class="todayTop">{{ data.day }}</div>
                    <todayList :year="data.time1.year" :month="data.time1.month" :day="data.time1.date" />

                </div>

            </div>
        </div>




    </div>
</template>
  
<script>
import { reactive, computed, watchEffect, onMounted, onBeforeMount } from 'vue'
import axios from 'axios'          //引入axios
import { marked } from 'marked';
import { useRouter } from "vue-router";
import Calendar from '../components/Calendar.vue'  //引入组件
import todayList from '../components/todayList.vue'
import router from '../router'
export default {
    //组件名
    name: 'BackMain',
    components: {
        Calendar, todayList    //注册组件
    },

    setup() {
        const router = useRouter()
        let data = reactive({
            time: {
                year: "2022",
                month: "1",
                date: "1",

            },
            time1: {              //日历选中哪天则为那天，默认值为明天
                year: "2022",
                month: "1",
                date: "1",

            },
            editShow: false,
            note: "",
            noteHtml: "",

        })

        //计算属性
        data.day = computed(() => {     //属性直接追加到data中
            if ((data.time.year == data.time1.year) && (data.time.month == data.time1.month) && (data.time.date == data.time1.date + 1)) {
                return "Yesterday"
            } else if ((data.time.year == data.time1.year) && (data.time.month == data.time1.month) && (data.time.date == data.time1.date - 1)) {
                return "Tomorrow"
            } else if ((data.time.year == data.time1.year) && (data.time.month == data.time1.month) && (data.time.date == data.time1.date)) {
                return "Today"
            } else {
                return data.time1.year + "年" + data.time1.month + "月" + data.time1.date + "日"
            }

        })


        watchEffect(() => {
            data.noteHtml = marked(data.note)

        })

        onBeforeMount(() => {     //先获取时间，然后再将时间传给子组件
            var dateObj = new Date();
            var year = dateObj.getFullYear(); //年
            var month = dateObj.getMonth() + 1; //月  (注意：月份+1)
            var date = dateObj.getDate(); //日
            data.time.year = year;
            data.time.month = month;
            data.time.date = date;
            data.time1.year = year;
            data.time1.month = month;
            data.time1.date = date;
        })



        onMounted(() => {
            axios.post('api/notes/', {          //前缀在main.js中设置
                "action": 'list_notes',
                "waste": 99,
            }).then(function (value) {
                data.note = value.data.retlist[0].content;
            })
                .catch(function (reason) {
                    console.log(reason)
                })

        })

        function select(year, month, date) {    //接收日历组件传过来的日期
            data.time1.year = year;
            data.time1.month = month;
            data.time1.date = date;

        }

        function editChange() {
            data.editShow = !data.editShow;
            if (data.editShow == false) {    //当edit由true转为false时，上传content
                modifyNote()
            }
        }

        function modifyNote() {
            axios.post("api/notes/", {
                "action": "modify_notes",
                "id": 2,
                "data": {
                    "content": data.note,
                }
            })
                .then(function (response) {
                    if (response.data.ret == 0) {
                        
                    } else if (response.data.ret == 302) {
                        alert("未登录")
                        router.push("signin");
                    }
                })
                .catch(function (error) {
                    console.log(error);
                });
        }


        function webmark() {
            router.push('/backstage/webmark')

        }

        function book() {
            router.push('/backstage/book')

        }

        function todo() {
            router.push('/backstage/todo')

        }

        function note() {
            router.push('/backstage/note')

        }

        function excerpt() {
            router.push('/backstage/excerpt')

        }



        //数据和函数都要返回
        return {
            data,
            select,
            editChange,
            webmark,
            book,
            todo,
            note,
            excerpt,
            timer,

        }
    },




}
</script>
<style scoped>
.main {
    width: 100%;
    height: 100%;
    font-size: 48px;
}


.mainDiv {
    display: flex;
    justify-content: flex-end;
    height: 100%;

}

.middle {
    width: calc(100% - 420px);
    height: 100%;
    margin-right: 20px;
    background-color: #24263b;
    display: flex;
    flex-direction: column;
    align-items: center;
    overflow: scroll;
    overflow-y: auto;
    overflow-x: hidden
}

.right {
    width: 400px;
    height: 100%;
    overflow: scroll;
    overflow-y: auto;
    overflow-x: hidden;
}

.calM {
    width: 380px;
    margin: 0px 0px;
    padding: 10px;
    background-color: rgb(248, 244, 237, 0.2);
    box-shadow: 4px 4px 5px rgb(0, 0, 0, 0.2);
    border-radius: 5px;
    color: white;
}

.day {
    background-color: rgb(248, 244, 237, 0.2);
    box-shadow: 4px 4px 5px rgb(0, 0, 0, 0.2);
    border-radius: 5px;
    color: white;
    width: 380px;
    height: auto;
    padding: 10px;
    font-size: 18px;
    margin-top: 10px;
}

.todayTop {
    font-size: 28px;
    font-family: MiSans;
    margin-left: 15px;
    font-weight: 900;

}




.stations {
    margin-left: 30px;
    margin-top: 25px;
    width: calc(100% - 30px);
    color: white;
    position: relative;
}

.buts {
    display: flex;
    flex-wrap:wrap
}

.but {
    background-color: rgb(248, 244, 237, 0.2);
    box-shadow: 4px 4px 5px rgb(0, 0, 0, 0.2);
    border-radius: 5px;
    font-family: MiSans;
    margin: 20px 20px 0 20px;
    text-align: center;
    color: white;
    font-size: 16px;

}

.but:hover {
    background-color: rgb(248, 244, 237, 0.1);

}

.but img {
    width: 50px;
    margin: 20px 26px 5px 26px;
}

.but p {
    padding-bottom: 5px;
}


.show {
    margin: 10px 0px;
    padding: 10px;
    height: 500px;
    width: calc(95% - 20px);
    font-size: 20px;
    overflow-y: scroll;
    overflow-y: auto;
    overflow-x: hidden;
    background-color: rgb(248, 244, 237, 0.2);
    box-shadow: 4px 4px 5px rgb(0, 0, 0, 0.2);
    border-radius: 5px;
}




.edit {
    border: 0;
    outline: none;
    font-family: MiSans;
    margin: 10px 0px;
    padding: 10px;
    height: 500px;
    width: calc(95% - 20px);
    font-size: 20px;
    background-color: rgb(248, 244, 237, 0.8);
    box-shadow: 4px 4px 5px rgb(0, 0, 0, 0.4);
    border-radius: 5px;
}


.editbut{
    position: absolute;
    right: 6%;
    top:73px
}

.mobileM{
    display: none;
}




@media (max-width: 1224px) {
.right{
    display: none;
}

.middle{
    width: 100%;
}

.mobileM{
    display:block;
    color: white;
    width: calc(100% - 60px);
    margin-left: 30px;
    margin-right: 30px;
    margin-top: 25px;
    
}

.mobileM span{
    margin: 10px;
    font-size: 28px;
    cursor: pointer;
}

.menu{
    display: flex;
    flex-wrap:wrap
}


}

</style>
  