<template>
  <div class="index">
    <div class="cal">
      <div class="card calendar">
        <div class="calM">
          <Calendar :select="select"></Calendar>
        </div>
      </div>
    </div>
    <div class="day">
      <div class="card today">
        <div class="todayTop">Today</div>
        <todayList :year="data.time.year" :month="data.time.month" :day="data.time.date" />

      </div>
      <div class="card nextday">
        <div class="todayTop">{{ data.day }}</div>
        <todayList :year="data.time1.year" :month="data.time1.month" :day="data.time1.date" />

      </div>
    </div>
  </div>

</template>

<script>
import { reactive, computed, watchEffect, onMounted, onBeforeMount } from 'vue'
import Calendar from '../components/Calendar.vue'  //引入组件
import todayList from '../components/todayList.vue'
export default {
  //组件名
  name: 'TodayPage',
  components: {
    Calendar, todayList    //注册组件
  },

  setup() {
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

    onBeforeMount(() => {     //先获取时间，然后再将时间传给子组件

      //获取时间

      var dateObj = new Date();
      var year = dateObj.getFullYear(); //年
      var month = dateObj.getMonth() + 1; //月  (注意：月份+1)
      var date = dateObj.getDate(); //日
      data.time.year = year;
      data.time.month = month;
      data.time.date = date;
      data.time1.year = year;
      data.time1.month = month;
      data.time1.date = date + 1;


    })

    function select(year, month, date) {    //接收日历组件传过来的日期
      data.time1.year = year;
      data.time1.month = month;
      data.time1.date = date;
      //console.log(date)

    }


    return {
      data,
      select,

    }

  }


}
</script>
<style scoped>
.cal {

  flex: 0 1 620px
}

.calendar {
  width: 460px;
  height: 460px;
  margin-left: 40px;
  margin-right: 40px;
}

.calM {
  padding-top: 50px;
  padding-left: 40px;
}

.day {
  display: flex;

}

.today {
  width: 310px;
  height: 460px;
  margin-right: 24px;
}

.nextday {
  width: 310px;
  height: 460px;
  margin-right: 40px;

}

.todayTop {
  font-size: 28px;
  font-family: MiSans;
  margin-left: 15px;
  font-weight: 900;

}



@media (max-width: 1224px) {
  .cal {
    flex: 0 0 0
  }

  .calendar {
    width: 80vw;
    height: 80vw;
    margin: 10vw;
  }

  .calM {
    padding: 0;
  }

  .day {
    display: flex;
    flex-wrap:wrap;
    justify-content:center;


  }

  .today {
    width: 80vw;
    height: auto;
    margin-right: 0px;
    margin-bottom: 20px;
  }

  .nextday {
    width: 80vw;
    height: auto;
    margin-right: 0px;

  }

  .todayTop {
    font-size: 8vw;
    font-family: MiSans;
    margin-left: 5vw;
    margin-top: 10px;
    font-weight: 900;

  }

}
</style>