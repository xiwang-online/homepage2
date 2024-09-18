<template>
    <div class="todayList">
        <table>
            <todayItem v-for="todo in data.todos" :key="todo.id" :todo="todo" :checkTodo="checkTodo"
                :deleteTodo="deleteTodo" :remarkTodo="remarkTodo" />
        </table>
        <input type="text" @keyup.enter="add" v-model="data.remark" />
    </div>
</template>

<script>
import { reactive, computed, watchEffect, onMounted } from 'vue'
import axios from 'axios'          //引入axios
import todayItem from './todayItem.vue'
import { useRouter } from "vue-router";
export default {
    //组件名
    name: 'TodayList',
    components: { todayItem },
    props: ["year", "month", "day"],


    setup(props) {     //接收到的参数需要传入setup才能在setup中使用
        //context用于接受自定义事件和插槽 
        const router = useRouter()
        //数据
        let data = reactive({
            todos: [],
            time: props.year + '.' + props.month + '.' + props.day,
            remark: ""


        })

        onMounted(() => {
            axios.post("api/schedule/", {
                "action": "list_schedule",
                "time": data.time,
            }).then(function (value) {
                //console.log(data.time)
                //console.log(value)
                data.todos = value.data.retlist;
            })
                .catch(function (reason) {
                    console.log(reason)
                })


        })

        //勾选
        function checkTodo(id) {
            data.todos.forEach((todo) => {
                if (todo.id === id) {
                    todo.finish = !todo.finish
                    axios.post("api/schedule/", {
                        "action": "check_schedule",
                        "data": {
                            "id": id,
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
            })
        }

        watchEffect(() => {

            data.time = props.year + '.' + props.month + '.' + props.day,  //监视日期的变化从而实时传给time

                axios.post("api/schedule/", {
                    "action": "list_schedule",
                    "time": data.time,
                })
                    .then(function (value) {
                        //console.log(data.time)
                        //console.log(value)
                        data.todos = value.data.retlist;
                    })
                    .catch(function (reason) {
                        console.log(reason)
                    })


        })

        //添加
        function add(e) {
            axios.post("api/schedule/", {
                "action": "add_schedule",
                "data": {
                    "time": data.time,
                    "content": e.target.value,
                }
            })
                .then(function (response) {
                    if (response.data.ret == 0) {
                        const todoObj = { id: response.data.id, finish: false, content: e.target.value }
                        data.todos.push(todoObj)
                        data.remark = ""
                        //console.log(response.data.id)
                    } else if (response.data.ret == 302) {
                        alert("未登录")
                        router.push("signin");
                    }
                })
                .catch(function (error) {
                    console.log(error);
                });
        }

        //删除
        function deleteTodo(id) {
            axios.post("api/schedule/", {
                "action": "del_schedule",
                "data": {
                    "id": id,
                }
            }).then(function (response) {
                if (response.data.ret == 0) {
                    //console.log(response.data.ret)
                    data.todos = data.todos.filter((todo) => { return todo.id != id })
                } else if (response.data.ret == 302) {
                    alert("未登录")
                    router.push("signin");
                }
            })
                .catch(function (error) {
                    console.log(error);
                });

        }
        //评论
        function remarkTodo(id) {
            axios.post("api/schedule/", {
                "action": "modify_schedule",
                "id": id,
                newdata: {
                    remark: data.remark
                }
            })
                .then(function (response) {
                    if (response.data.ret == 0) {
                        //console.log(response.data.ret)
                        data.remark = ""
                    } else if (response.data.ret == 302) {
                        alert("未登录")
                        router.push("signin");
                    }
                })
                .catch(function (error) {
                    console.log(error);
                });
        }





        //数据和函数都要返回
        return {
            data,
            checkTodo,
            add,
            deleteTodo,
            remarkTodo


        }



    },
};


</script>
<style scoped>
.todayList {
    height: 400px;
    width: 260px;
    margin: 0px 25px 20px 25px;
    position: relative;
    font-family: MiSans;

}

input {
    width: 265px;
    height: 30px;
    border: none;
    border-bottom: 2px solid black;
    background-color: inherit;
    position: absolute;
    bottom: 0px;
}


@media (max-width: 1224px) {
    .todayList {
        height: auto;
        width: 70vw;
        margin: 0px 0 20px 5vw;
        position: relative;
        font-family: MiSans;

    }

    input {
        width: 70vw;
        height: 30px;
        border: none;
        border-bottom: 2px solid black;
        background-color: inherit;
        position: static;
        bottom: 0px;
        margin-top: 20px;
    }
}
</style>