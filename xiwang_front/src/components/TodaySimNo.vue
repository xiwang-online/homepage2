<template>
  <div class="today">日程</div>
  <div class="table">
    <table>
      <TodaySimItem v-for="todo in data.todos" :key="todo.id" :todo="todo" :checkTodo="checkTodo" />
    </table>
  </div>
</template>

<script>
import { reactive, computed, watchEffect, onMounted } from 'vue'
import axios from 'axios'          //引入axios
import TodaySimItem from './TodaySimItem.vue'
import { useRouter } from "vue-router";
export default {
  //组件名
  name: 'TodaySimNo',
  components: { TodaySimItem },


  setup() {     //接收到的参数需要传入setup才能在setup中使用
    //context用于接受自定义事件和插槽 
    const router = useRouter()
    //数据
    let data = reactive({
      todos: [{ id: 1045, scheduledata: '2023.11.14', content: '是谁好奇心这么大', finish: true, remark: null },
      { id: 1046, scheduledata: '2023.11.14', content: '不要再看了', finish: true, remark: null },
      { id: 1047, scheduledata: '2023.11.14', content: '没登陆看到的都是假数据', finish: false, remark: null },
      { id: 1048, scheduledata: '2023.11.14', content: '真的没什么好看的啦', finish: false, remark: null },
      { id: 1049, scheduledata: '2023.11.14', content: '我也是服了你了', finish: false, remark: null }
    ],


    })





    //生命周期函数，
    //onMounted：在初始化页面完成后执行
    onMounted(() => {

    })


    //数据和函数都要返回
    return {
      data,
    }
  },




}
</script>
<style scoped>
.today {
  font-size: 28px;
  font-family: MiSans;
  margin-left: 15px;
  font-weight: 900;
  cursor: pointer;
  /*光标为一只手*/
}

table {
  margin-left: 30px;
  font-size: 22px;
  font-family: MiSans;

}

.table {
  height: 150px;
  overflow: scroll;
  overflow-y: auto;
  overflow-x: hidden;
  filter: blur(4px);
  pointer-events: none;
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
  .today {
    font-size: 28px;
    font-family: MiSans;
    margin-left: 15px;
    font-weight: 900;
    cursor: pointer;
    /*光标为一只手*/

  }

  table {
    margin-left: 30px;
    font-size: 22px;
    font-family: MiSans;

  }

  .table {
    height: auto;
    margin-bottom: 3vw;
    
  }


}
</style>
