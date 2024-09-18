<template>
  <div class="index">
    <div class="header">个人项目</div>
    <div class="page">
      <div class="block" v-for="item in data.notes">
        <img class="img" :src="item.content.img">
        <a class="down" :href="item.content.link" target="_blank">
          <div class="titletime">
            <div class="title">{{ item.content.name }}</div>
            <div class="time">{{ item.content.time }}</div>
          </div>
          <p class="detail">{{ item.content.detail }}</p>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import { reactive, computed, watchEffect, onMounted } from 'vue'
import axios from 'axios'          //引入axios
export default {
  //组件名
  name: 'Projectpage',


  setup() {
    let data = reactive({
      notes: [],
    })



    //生命周期函数，
    //onMounted：在初始化页面完成后执行
    onMounted(() => {
      axios.post('api/notes/', {          //前缀在main.js中设置
        "action": 'list_notes',
        "waste": 2,
      }).then(function (value) {
        data.notes = value.data.retlist.reverse();
        data.notes.forEach(function deal(item) {
          item.content = eval('(' + item.content + ')');
        })
        //console.log(data.notes);
      })
        .catch(function (reason) {
          console.log(reason)
        })
    })


    //数据和函数都要返回
    return {
      data,
    }
  }


}
</script>

<style scoped>
.index{
  flex-direction:column;
}

.header{
  width: 80%;
  font-family: MiSans;
  font-size: 32px;
  font-weight: 800;
  margin-top: 66px;
}


.page {
  width: 80%;
  min-height: 70vh;
  margin: 40px 0 80px 0;
  display: grid;
  /*网格布局*/
  grid-template-columns: repeat(auto-fill, 320px);
  grid-gap: 40px;
  justify-content: center;
  font-family: MiSans;

}

.block {
  display: flex;
  width: 320px;
  height: 276px;
  flex-direction: column;
  background-color: white;
  border-radius: 5px;
  box-shadow: 4px 4px 5px rgb(0, 0, 0, 0.2);
  overflow: hidden;

  padding-bottom: 12px;

}

.down {
  font-size: 0.875rem;
  cursor: pointer;

}

.titletime {
  width: 288px;
  height: 20px;
  padding: 16px 20px 0px 12px;
  display: flex;
  justify-content: space-between;
  font-weight: 400;


}

.time {
  vertical-align: bottom;
  font-size: 1rem;
}

.title {
  font-size: 1.2rem;
}

.detail {
  width: 296px;
  height: 38px;
  padding: 10px 12px 0px 12px;
  /*超出两行变省略号*/
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;

}

.img {
  width: 100%;
  height: 192px;


}
</style>
