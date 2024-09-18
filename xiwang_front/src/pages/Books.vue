<template>
  <div class="index">
    <div class="main">
      <p class="word">在读</p>
      <div class="book card">
        <img class="bookimg" :src="data.reading[0].remark">
        <p class="bookname">{{ data.reading[0].bookname }}</p>
        <p class="author">{{ data.reading[0].author }}</p>
      </div>

      <p class="word">要读</p>
      <div class="fu">
        <div class="book card" v-for="book in data.unread" :key="book.id">
          <img class="bookimg" :src="book.remark">
          <p class="bookname">{{ book.bookname }}</p>
          <p class="author">{{ book.author }}</p>
        </div>
      </div>

      <p class="word">已读</p>

      <p class="word1">2024</p>
      <div class="ed2023 fu">
        <div class="book card" v-for="book in data.readed" :key="book.id" @click="detail(book)">
          <img class="bookimg" :src="book.remark">
          <p class="bookname">{{ book.bookname }}</p>
          <p class="author">{{ book.author }}</p>
          <p class="count">字数:{{ book.wordCount }}</p>
          <p class="time">读完日期:{{ book.readdata }}</p>
        </div>
      </div>

      <p class="word1">2023</p>
      <div class="ed2023 fu">
        <div class="book card" v-for="book in data.readed23" :key="book.id" @click="detail(book)">
          <img class="bookimg" :src="book.remark">
          <p class="bookname">{{ book.bookname }}</p>
          <p class="author">{{ book.author }}</p>
          <p class="count">字数:{{ book.wordCount }}</p>
          <p class="time">读完日期:{{ book.readdata }}</p>
        </div>
      </div>

      <p class="word1">2022</p>
      <div class="ed2022 fu">
        <div class="book card" v-for="book in data.readed22" :key="book.id" @click="detail(book)">
          <img class="bookimg" :src="book.remark">
          <p class="bookname">{{ book.bookname }}</p>
          <p class="author">{{ book.author }}</p>
          <p class="count">字数:{{ book.wordCount }}</p>
          <p class="time">读完日期:{{ book.readdata }}</p>
        </div>
      </div>
      <p class="word1">2021</p>
      <div class="ed2021 fu">
        <div class="book card" v-for="book in data.readed21" :key="book.id" @click="detail(book)">
          <img class="bookimg" :src="book.remark">
          <p class="bookname">{{ book.bookname }}</p>
          <p class="author">{{ book.author }}</p>
          <p class="count">字数:{{ book.wordCount }}</p>
          <p class="time">读完日期:{{ book.readdata }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { reactive, computed, watchEffect, onMounted, ref } from 'vue'
import axios from 'axios'          //引入axios
import { ElMessageBox } from 'element-plus'  //引入element-ui的消息框
export default {
  //组件名
  name: 'Books',
  setup() {
    let data = reactive({
      reading: [{ "bookname": "", "author": "" }],
      unread: [],
      readed21: [],
      readed22: [],
      readed23: [],
      readed: []
    })



    //生命周期函数，
    //onMounted：在初始化页面完成后执行
    onMounted(() => {
      axios.post('api/books/', {          //在读
        "action": 'list_book',
        "read": 1,
      }).then(function (value) {
        //console.log(value);
        data.reading = value.data.retlist;
      })
        .catch(function (reason) {
          console.log(reason)
        })


      axios.post('api/books/', {          //未读
        "action": 'list_book',
        "read": 2,
      }).then(function (value) {
        //console.log(value);
        data.unread = value.data.retlist;
      })
        .catch(function (reason) {
          console.log(reason)
        })



      axios.post('api/books/', {          //已读
        "action": 'list_book',
        "read": 3,
      }).then(function (value) {
        //console.log(value);
        data.readed = value.data.retlist;
        //console.log(data.readed)
        data.readed = data.readed.reverse()    //倒序
        data.readed21 = data.readed.splice(-9, 9)
        data.readed22 = data.readed.splice(-28, 28)
        data.readed23 = data.readed.splice(-16, 16)
        //console.log(data.readed.slice(-9))
      })
        .catch(function (reason) {
          console.log(reason)
        })


    })


    function detail(e) {
      //console.log(e.notes.slice(0, 4))
      if (e.notes.slice(0, 4) == "http") {
        window.open(e.notes)
      } else {
        ElMessageBox.alert('抱歉，该书读后感尚未公开。', {
          confirmButtonText: 'OK',
        })
      }


    }


    //数据和函数都要返回
    return {
      data,
      detail
    }
  },



}
</script>
<style scoped>
.main {
  display: flex;
  flex-direction: column;
  width: 68%;
  margin: 12% 0;
}

.word {
  font-size: 28px;
  padding: 10px 20px;
  font-weight: 900;
  margin-top: 50px;
  margin-bottom: 10px;
}

.word1 {
  font-size: 20px;
  padding: 10px 20px;
  font-weight: 600;
  margin: 5px 0;
}

.book {
  margin: 8px 20px;
  width: 130px;
  height: 175px;
  background-color: antiquewhite;
  position: relative;
}

.bookimg {
  position: absolute;
  width: 130px;
  height: 175px;
  z-index: 99;
}

.book:hover .bookimg {
  opacity: 0.2
}

.bookname {
  font-size: 20px;
  text-align: center;
  padding: 40px 10px 10px 10px;

}

.author {
  text-align: center;
}


.count {
  font-size: 12px;
  position: absolute;
  bottom: 30px;
  left: 10px;
}

.time {
  font-size: 12px;
  position: absolute;
  bottom: 10px;
  left: 10px;

}

.fu {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  width: auto;
  margin: 0px 0px;
}


@media (max-width: 1224px) {
  .main {
    display: flex;
    flex-direction: column;
    width: 90%;
    margin: 12% 0;
  }

  .book {
  margin: 8px 18px;
}
}
</style>
