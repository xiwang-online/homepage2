<template>
  <tr>
    <td><input type="checkbox" :checked="data.todo.finish" @click="handleChecked(data.todo.id)" /></td>
    <td :style="data.styleObj" class="td1" :title="data.todo.remark">{{ data.todo.content }}</td>
    <td><img src="../assets/delete.png" class="tdimage1" @click.left="handleDelete(data.todo.id)"></td>
    <td><img src="../assets/remark.png" class="tdimage1" @click.left="handleremark(data.todo.id)"></td>

  </tr>

</template>

<script>
import { reactive, computed, watchEffect, onMounted } from 'vue'
export default {
  //组件名
  name: 'TodayItem',
  props: ["todo", "checkTodo", "deleteTodo", "remarkTodo"],


  setup(props) {
    //context用于接受自定义事件和插槽 
    //数据
    let data = reactive({
      todo: props.todo



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


    function handleDelete(id) {
      if (confirm("确定要删除吗？")) {
        props.deleteTodo(id)
      }
    }
    function handleremark(id) {
      props.remarkTodo(id)
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
      handleDelete,
      handleremark
    }
  },




}
</script>
<style scoped>
td {
  padding-top: 12px;

}




tr:hover .tdimage1 {
  display: block;
}

.td1 {
  width: 250px;
  font-size: 18px;
}

.tdimage1 {
  width: 20px;
  height: 20px;
  display: none;
}


@media (max-width: 1224px) {
  td {
    padding-top: 10px;

  }


  tr:hover .tdimage1 {
    display: block;
  }

  .td1 {
    width: 70vw;
    font-size: 3vw;
  }

  .tdimage1 {
    width: 5vw;
    height: 5vw;
    display: block;
    margin-left: 4vw;
  }
}
</style>
