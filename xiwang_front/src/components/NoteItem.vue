<template>
    <div class="noteItem">
        <div class="tools">
            <img width="30" src="../assets/bianji.svg" @click="editChange">
            <img width="30" src="../assets/shanchu.svg" @click="deleteNote">
        </div>
        <div class="show card" v-html="data.noteHtml.content" v-if="!(data.editShow)"></div>
        <textarea class="edit" v-if="data.editShow" @blur="editChange" v-model="data.note.content"></textarea>

    </div>

</template>

<script>
import { reactive, computed, watchEffect, onMounted } from 'vue'
import { marked } from 'marked';
import axios from 'axios'          //引入axios
import { useRouter } from "vue-router";
export default {
    //组件名
    name: 'NoteItem',
    props: ["note"],


    setup(props) {
        //context用于接受自定义事件和插槽 
        const router = useRouter()
        //数据
        let data = reactive({
            note: props.note,
            noteHtml: [],
            editShow: false

        })



        watchEffect(() => {
            //js的拷贝数据都是浅拷贝（引用），需要通过如下方式深拷贝数据
            data.noteHtml = JSON.parse(JSON.stringify(data.note));
            data.noteHtml.content = marked(data.noteHtml.content)

        })



        function editChange() {
            data.editShow = !data.editShow;
            if (data.editShow == false) {    //当edit由true转为false时，上传content
                modifyNote()
            }
        }



        function deleteNote() {    //将note放入垃圾桶，即将waste改为2
            axios.post("api/notes/", {
                "action": "modify_notes",
                "id": data.note.id,
                "data": {
                    "waste": 2,
                }
            }).then(function (response) {
                if (response.data.ret == 0) {
                    //console.log(response.data.ret)
                    location.reload()
                } else if (response.data.ret == 302) {
                    alert("未登录")
                    router.push("signin");
                }
            })
                .catch(function (error) {
                    console.log(error);
                });

        }

        function modifyNote() {
            axios.post("api/notes/", {
                "action": "modify_notes",
                "id": data.note.id,
                "data": {
                    "content": data.note.content,
                }
            })
                .then(function (response) {
                    if (response.data.ret == 0) {
                        //console.log(response.data.ret)
                    } else if (response.data.ret == 302) {
                        alert("未登录")
                        router.push("signin");
                    }
                })
                .catch(function (error) {
                    console.log(error);
                });
        }



        //生命周期函数，
        //onMounted：在初始化页面完成后执行
        onMounted(() => {
            console.log("mounted")
        })


        //数据和函数都要返回
        return {
            data,
            editChange,
            deleteNote,
        }
    },




}
</script>
<style scoped>
.tools {
    background-color: #9ec862;
    width: 410px;
    margin: 0px 20px;
    display: flex;
    justify-content:flex-end

}

.show {
    margin: 0px 20px 30px 20px;
    padding: 20px 30px;
    height: 350px;
    width: 350px;
    font-size: 20px;
    overflow-y: scroll;
    overflow-y: auto;
    overflow-x: hidden
}




.edit {
    border: 0;
    outline: none;
    font-family: MiSans;
    margin: 0px 20px 30px 20px;
    padding: 20px 30px;
    height: 350px;
    width: 350px;
    font-size: 20px;
    background-color: rgb(248, 244, 237, 0.8);
    box-shadow: 4px 4px 5px rgb(0, 0, 0, 0.4);
    border-radius: 5px;
}

@media (max-width: 1224px) {
    .tools {
    background-color: #9ec862;
    width: 80vw;
    margin: 0px 10vw;
    display: flex;
    justify-content:flex-end

}

.show {
    margin: 0px 10vw 30px 10vw;
    padding: 5vw 5vw;
    height: 80vw;
    width: 70vw;
    font-size: 16px;
    overflow-y: scroll;
    overflow-y: auto;
    overflow-x: hidden
}




.edit {
    border: 0;
    outline: none;
    font-family: MiSans;
    margin: 0px 10vw 30px 10vw;
    padding: 5vw 5vw;
    height: 80vw;
    width: 70vw;
    font-size: 16px;
    background-color: rgb(248, 244, 237, 0.8);
    box-shadow: 4px 4px 5px rgb(0, 0, 0, 0.4);
    border-radius: 5px;
}
}

</style>
