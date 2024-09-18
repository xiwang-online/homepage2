<template>
  <div class="today" @click="enterToday">日程</div>
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
  name: 'TodaySim',
  components: { TodaySimItem },


  setup() {     //接收到的参数需要传入setup才能在setup中使用
    //context用于接受自定义事件和插槽 
    const router = useRouter()
    //数据
    let data = reactive({
      todos: [],
      time: ''


    })





    //生命周期函数，
    //onMounted：在初始化页面完成后执行
    onMounted(() => {
      var time1 = new Date();
      var year1 = time1.getFullYear();
      var month1 = time1.getMonth() + 1;
      var data1 = time1.getDate();
      data.time = year1 + '.' + month1 + '.' + data1
      axios.post("api/schedule/", {
        "action": "list_schedule",
        "time": data.time,
      })
        .then(function (value) {
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


    function enterToday() {
      router.push('/today')

    }



    //数据和函数都要返回
    return {
      data,
      checkTodo,
      enterToday
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
  overflow-x: hidden
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
