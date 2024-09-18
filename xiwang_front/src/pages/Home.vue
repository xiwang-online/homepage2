<template>
    <div class="index">
        <div class="home_left">
            <HomeLeft></HomeLeft>
        </div>
        <div class="home_right">
            <HomeRight></HomeRight>
        </div>
    </div>
</template>

<script>
import HomeRight from '../components/HomeRight.vue'
import HomeLeft from '../components/HomeLeft.vue'
export default {
    //组件名
    name: 'Home',
    components: { HomeRight, HomeLeft },

    setup() {

        return {

        }

    }


}
</script>


<style scoped>
.home_left {
    display: flex;
    flex-direction: column;
    /*垂直排列*/
    flex: 0 1 620px
}



.home_right {
    display: flex;
    flex-direction: column;

    /*垂直排列*/
}

@media (max-width: 1224px) {

    .home_left {
        display: flex;
        flex-direction: column;
        /*垂直排列*/
        flex: 0 0 0vw
    }



    .home_right {

        display: flex;
        flex-direction: column;
        /*垂直排列*/
    }


}
</style>

