<template>
  <div class="canlendarPanel">
    <div class="canlendar-header">
      <p class="pre">
        <!--
        <span @click="changeDate('preYear')">
          上年
        </span>
        -->
        <span @click="changeDate('preMonth')">
          <img class="change" src="../assets/zuo.svg" alt="left">
        </span>
      </p>
      <p class="currenDate">{{ `${data.year}年${data.month}月` }}</p>
      <p class="next">
        <span @click="changeDate('nextMonth')">
          <img class="change" src="../assets/you.svg" alt="right">
        </span>
        <!--
        <span @click="changeDate('nextYear')">
          下年
        </span>
        -->
      </p>
    </div>
    <div class="canlendar-main">
      <ul class="main-header">
        <li class="week" v-for="(item, index) in data.week">
          {{ item }}
        </li>
      </ul>
      <ul class="main">
        <li v-for="inx in data.weekDay" class="disabled">
          {{ data.preMonthSize - data.weekDay + inx }}
        </li>
        <li v-for="index in data.monthList[data.month - 1]">
          <span :class="{ currentDay: index === data.day }" @click="onSelectDay(index)">
            {{ index }}</span>
        </li>
        <li v-for="index in data.lastWeekDay" class="disabled">{{ index }}</li>
      </ul>
    </div>
  </div>


</template>

<script>
import { reactive, computed, watchEffect, onMounted } from 'vue'
export default {
  //组件名
  name: 'Calendar',
  props: ["select"],   //用于将选中的日期传给父组件

  setup(props) {
    //数据
    let data = reactive({
      year: 0,
      month: 0,
      day: 0,
      week: ['周日', '周一', '周二', '周三', '周四', '周五', '周六'],
      monthList: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
      weekDay: 1,
      lastWeekDay: 1,


    })




    // 上一个月有多少天
    //计算属性
    data.preMonthSize = computed(() => {     //属性直接追加到data中
      return data.month - 1 === 0 ? 31 : data.monthList[data.month - 2]

    })



    //生命周期函数，
    //onMounted：在初始化页面完成后执行
    onMounted(() => {
      getCurrentDate()
      initDate()
    })


    // 获得今天的日期
    function getCurrentDate() {
      const date = new Date()
      data.year = date.getFullYear()
      data.month = date.getMonth() + 1
      data.day = date.getDate()
    }
    // 根据年月日获得为星期几
    function getWeekDay(year, month, day) {
      return new Date(`${year}/${month}/${day}`).getDay()
    }
    function initDate() {
      if (
        (data.year % 4 === 0 && data.year % 100 !== 0) ||
        data.year % 400 === 0
      ) {
        data.monthList[1] = 29
      } else {
        data.monthList[1] = 28
      }
      // 获得指定年月的1号是星期几
      const firstDay = getWeekDay(data.year, data.month, 1)
      // 在1号前面填充多少个上个月的日期
      data.weekDay = firstDay === 7 ? 0 : firstDay
      // 获得最后一天是星期几，往后填充多少个
      const remineDay = getWeekDay(
        data.year,
        data.month,
        data.monthList[data.month - 1]
      )
      data.lastWeekDay = remineDay === 7 ? 6 : 6 - remineDay
    }


    function changeDate(type) {
      switch (type) {
        case 'preYear':
          data.year -= 1
          break
        case 'preMonth':
          // 当前月份为1月， 上一个月分为12月，年份减1
          if (data.month === 1) {
            data.month = 12
            data.year -= 1
          } else {
            data.month -= 1
          }
          break
        case 'nextYear':
          data.year += 1
          break
        case 'nextMonth':
          // 当前月份为12月， 下个月分为1月，年份加1
          if (data.month === 12) {
            data.month = 1
            data.year += 1
          } else {
            data.month += 1
          }
          break
        default:
          break
      }
      initDate()
    }

    function onSelectDay(day) {
      //console.log(data.year + "年" + data.month + "月" + day)
      props.select(data.year, data.month, day)

    }


    //数据和函数都要返回
    return {
      data,
      changeDate,
      onSelectDay
    }
  },




}
</script>


<style scoped>
.canlendarPanel {
  height: 360px;
  width: 380px;
  display: flex;
  flex-direction: column;
  /*垂直排列*/
  text-align: center;
  /*文字居中*/
  font-family: MiSans;
}

.canlendar-header {
  /*日历头*/
  line-height: 35px;
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.pre {
  cursor: pointer;
  /*光标为一只手*/
}

.next {
  cursor: pointer;
  /*光标为一只手*/
}


.currenDate {
  /*日历头日期显示*/
  width: 300px;
  font-size: 24px;
  font-family: PingFangSC-Medium;
}

.canlendar-main {
  /*日历主体*/
  display: flex;
  flex: 1;
  flex-direction: column;

}

.main-header {
  /*主体头*/
  display: flex;
  line-height: 30px;
  margin: 15px 0;
}

.week {
  /*星期显示*/
  font-size: 20px;
  flex: 1;

}



ul.main {
  /*主体日期*/
  display: flex;
  flex: 1;
  flex-wrap: wrap;
  /*容器内项目是否自动换行*/
  align-items: center;
  /*元素在辅轴上如何对齐*/
  padding-bottom: 10px;
  font-size: 20px;
  justify-content: center
}

.main li {
  /**/
  position: relative;
  width: 54px;
  /*数字宽度*/
  line-height: 25px;
  cursor: pointer;
  /*光标为一只手*/
}


.main li:hover {
  font-size: 24px;
}

.main li:active {
  font-size: 18px;
}



.disabled {
  /*非本月样式*/
  color: cadetblue;
  cursor: default;
}

.currentDay:before {
  /*画圈*/
  content: '';
  position: absolute;
  display: inline-block;
  left: 8px;
  top: -5px;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  border: 3px solid #FFE100;
}


.change {
  width: 25px;
  margin-top: 3px;
}

.change:hover {
  width: 25px;
  height: 28px;
  margin-top: 2px;
}


.change:active {
  width: 25px;
  height: 23px;
  margin-top: 5px;
}




@media (max-width: 1224px) {
  .canlendarPanel {
    height: 80vw;
    width: 80vw;
    display: flex;
    flex-direction: column;
    /*垂直排列*/
    text-align: center;
    /*文字居中*/
    font-family: MiSans;
    justify-content: center;
    align-items:center;
  }

  .canlendar-header {
    /*日历头*/
    line-height: 20px;
    display: flex;
    flex-direction: row;
    justify-content: center;
  }

  .pre {
    cursor: pointer;
    /*光标为一只手*/
  }

  .next {
    cursor: pointer;
    /*光标为一只手*/
  }


  .currenDate {
    /*日历头日期显示*/
    width: 55vw;
    font-size: 4vw;
    padding-top: 0vw;
    font-family: PingFangSC-Medium;
  }

  .canlendar-main {
    /*日历主体*/
    display: flex;
    flex: 0;
    flex-direction: column;
    align-items:center;
    width: 80vw;
    
  }

  .main-header {
    /*主体头*/
    display: flex;
    line-height: 4vw;
    margin: 4vw 0 2vw 0;
    width: 70vw;

    
  }

  .week {
    /*星期显示*/
    font-size: 3vw;
    flex: 1;

  }



  ul.main {
    /*主体日期*/
    display: flex;
    flex: 1;
    flex-wrap: wrap;
    /*容器内项目是否自动换行*/
    align-items: center;
    /*元素在辅轴上如何对齐*/
    padding-bottom: 0vw;
    font-size: 4vw;
    justify-content: center;
    width: 70vw;
  }

  .main li {
    /**/
    position: relative;
    width: 10vw;
    /*数字宽度*/
    line-height: 9vw;
    cursor: pointer;
    /*光标为一只手*/
  }


  .main li:hover {
    font-size: 5vw;
  }

  .main li:active {
    font-size: 3vw;
  }



  .disabled {
    /*非本月样式*/
    color: cadetblue;
    cursor: default;
  }

  .currentDay:before {
    /*画圈*/
    content: '';
    position: absolute;
    display: inline-block;
    left: 1.8vw;
    top: 1vw;
    width: 5vw;
    height: 5vw;
    border-radius: 50%;
    border: 3px solid #FFE100;
  }


  .change {
    width: 4vw;
    margin-top: 0vw;
  }

  .change:hover {
    width: 4vw;
    height: auto;
    margin-top: 0px;
  }


  .change:active {
    width: 25px;
    height: 23px;
    margin-top: 5px;
  }


}
</style>
<!--
<style lang="scss" scoped>
.canlendarPanel {
  height: 260px;
  border-bottom: 3px solid var(--background);
  display: flex;
  flex-direction: column;
  .canlendar-header {
    line-height: 30px;
    background: var(--special-bg);
    display: flex;
    flex-direction: row;
    justify-content: center;
    .currenDate {
      margin: 0 20px;
      font-size: 16px;
      font-family: PingFangSC-Medium;
    }
    .icon {
      width: 12px;
      height: 12px;
    }
  }
  .canlendar-main {
    flex: 1;
    display: flex;
    flex-direction: column;
    .main-header {
      display: flex;
      line-height: 30px;
      color: var(--text-color);
      li {
        flex: 1;
      }
    }
    ul.main {
      flex: 1;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      padding-bottom: 10px;
      font-size: 14px;
      li {
        position: relative;
        width: 42px;
        line-height: 25px;
        cursor: pointer;
      }
      .disabled {
        color: var(--text-color);
        cursor: default;
      }
      .currentDay:before {
        content: '';
        position: absolute;
        display: inline-block;
        left: 8px;
        width: 24px;
        height: 24px;
        border-radius: 50%;
        border: 1px solid #FFE100;
      }
    }
  }
}
</style>
-->