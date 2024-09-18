<template>

  <img v-if="$store.state.background==2" class="backimg" src="./assets/background/2.png">
  <img v-else-if="$store.state.background==3" class="backimg" src="./assets/background/3.png">
  <img v-else-if="$store.state.background==4" class="backimg" src="./assets/background/4.png">
  <img v-else-if="$store.state.background==5" class="backimg" src="./assets/background/5.jpg">

  <img v-else-if="$store.state.background==6" class="backimg" src="./assets/background/spring_background.png">
  <img v-else class="backimg" src="./assets/background/1.png">


  

  <RouterView></RouterView>
</template>

<script>
import { onMounted, reactive } from 'vue'
import { useRouter } from "vue-router";
import { useStore } from 'vuex'
export default {
  name: 'App',

  setup() {
    const router = useRouter()
    const store = useStore()
    let data = reactive({


    })


    onMounted(() => {

      //判断本地是否存有背景编号，有的话放到store中，没有的话设为1
      if (localStorage.getItem('background') != null) {
        store.commit('bg', localStorage.getItem('background'))
      } else {
        window.localStorage.setItem('background', 1)
        store.commit('bg', localStorage.getItem('background'))
      }

    })









    return {
      data,

    }

  }

}
</script>

<style scoped>
.backimg {
  position: fixed;
  width: 100%;
  height: 100vh;
  top: 0;
  object-fit: cover;
  z-index: -1;
}




@media (max-width: 1224px) {}
</style>
