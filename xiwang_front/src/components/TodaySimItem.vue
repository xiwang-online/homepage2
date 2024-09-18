<template>
    <tr>
        <td><input type="checkbox" :checked="data.todo.finish" @click="handleChecked(data.todo.id)" /> </td>
        <td :style="data.styleObj" class="td1">{{ data.todo.content }}</td>
    </tr>

</template>

<script>
import { reactive, computed, watchEffect, onMounted } from 'vue'
export default {
    //组件名
    name: 'TodaySimItem',
    props: ["todo", "checkTodo"],


    setup(props) {
        //context用于接受自定义事件和插槽 
        //数据
        let data = reactive({
            todo : props.todo



        })



        //计算属性
    data.styleObj = computed(() => {     //属性直接追加到data中
      if (data.todo.finish) {
            return { textDecoration: "line-through" };
          } else {
            return { textDecoration: "none" };
          }

    })


        function handleChecked(id) {
            props.checkTodo(id)
        }


        //生命周期函数，
        //onMounted：在初始化页面完成后执行
        onMounted(() => {
            //console.log("mounted")
        })


        //数据和函数都要返回
        return {
            data,
            handleChecked,
        }
    },




}
</script>
<style scoped>
td{
    padding-top: 10px;
}

</style>
