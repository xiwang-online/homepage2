<template>
    <div class="index">
        <div class="note">
            <NoteItem v-for="note in data.notes" :key="note.id" :note="note"></NoteItem>
            <div class="add card"><img src="../assets/jia.svg" @click="addNote"></div>
        </div>
    </div>

</template>




<!--写的有问题，要将note改成组件来显示-->
<!--没有获得焦点时显示html格式，获得焦点时显示markdown格式
@blur 是当元素失去焦点时所触发的事件

@focus是元素获取焦点时所触发的事件-->




<script>
import { reactive, computed, watchEffect, onMounted } from 'vue'
import axios from 'axios'          //引入axios
import NoteItem from '../components/NoteItem.vue'
export default {
    //组件名
    name: 'Notes',
    components: { NoteItem },
    setup() {
        let data = reactive({
            notes: [],
            time: ""

        })

        //生命周期函数，
        //onMounted：在初始化页面完成后执行
        onMounted(() => {
            var dateObj = new Date();
            var year = dateObj.getFullYear(); //年
            var month = dateObj.getMonth() + 1; //月  (注意：月份+1)
            var date = dateObj.getDate(); //日
            data.time = year + "." + month + "." + date



            axios.post('api/notes/', {          //前缀在main.js中设置
                "action": 'list_notes',
                "waste": 1,
            }).then(function (value) {
                //console.log(value);
                data.notes = value.data.retlist;
            })
                .catch(function (reason) {
                    console.log(reason)
                })

        })


        function addNote() {
            axios.post("api/notes/", {
                "action": "add_notes",
                "data": {
                    "content": "",
                    "time": data.time,
                    "waste": 1,
                    "remark": ""
                }
            }).then(function (response) {
                if (response.data.ret == 0) {
                    const noteObj = { id: response.data.id, content: "", time: data.time, waste: 1, remark: "" }
                    data.notes.push(noteObj)
                    //console.log(response.data.id)
                } else if (response.data.ret == 302) {
                    alert("未登录")
                    router.push("signin");
                }
            })
                .catch(function (error) {
                    //console.log(error);
                });

        }


        //数据和函数都要返回
        return {
            data,
            addNote,


        }
    },



}
</script>
<style scoped>
.note {
    display: flex;
    /*水平垂直居中*/
    align-items: center;
    justify-content: flex-start;
    width: 75%;
    height: 75%;
    flex-wrap: wrap;


}

.add {
    margin: 0px 20px 30px 20px;
    padding: 20px 30px;
    height: 350px;
    width: 350px;
    display: flex;
    /*水平垂直居中*/
    align-items: center;
    justify-content: center;

}

.add img {
    width: 100px;
}

.add img:hover {
    width: 120px;
}



@media (max-width: 1224px) {
    .note {
        display: flex;
        /*水平垂直居中*/
        align-items: center;
        justify-content: flex-start;
        width: 100vw;
        height: auto;
        flex-wrap: wrap;
        margin-top: 20vw;


    }

    .add {
        margin: 0px 10vw 30px 10vw;
        padding: 5vw 5vw;
        height: 80vw;
        width: 70vw;
        display: flex;
        /*水平垂直居中*/
        align-items: center;
        justify-content: center;

    }

    .add img {
        width: 100px;
    }

    .add img:hover {
        width: 120px;
    }


}
</style>
