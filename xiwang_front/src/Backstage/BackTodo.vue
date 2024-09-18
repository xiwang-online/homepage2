<template>
    <div class="main">
        <el-calendar v-if="!data1.show">
            <template #dateCell="{ data }">
                <div :class="data.isSelected ? 'is-selected' : ''" class="calendar-day">
                    {{ data.day.split('-').slice(1).join('-') }}
                    <div v-for="todo in data1.todolist" :key="todo.id">
                        <div v-if="datachange(data.day) == todo.scheduledata" :class="todo.finish ? '' : 'is-finish'"
                            :title="todo.remark">
                            <el-tooltip class="box-item" effect="dark" :content="todo.remark" placement="right-start">
                                {{ todo.content }}
                            </el-tooltip>
                        </div>
                    </div>
                </div>
            </template>
        </el-calendar>


        <el-table :data="data1.todolist" height="90vh" style="width: 100%" v-if="data1.show">
            <el-table-column type="index" width="50" />
            <el-table-column prop="id" label="ID" width="50" />
            <el-table-column prop="scheduledata" label="日期" width="120" />
            <el-table-column prop="content" label="内容" width="500" />
            <el-table-column prop="finish" label="是否完成" width="100" />
            <el-table-column prop="remark" label="备注" />
        </el-table>



        <el-switch class="sw" v-model="data1.show" size="large" active-text="表格" inactive-text="日历"
            style="--el-switch-on-color: #1bca65; --el-switch-off-color: #409ffb" />
    </div>
    <!--
        基本显示功能已经完成，此部分不添加增删改功能,
        后面可以进行样式的优化，比如
        悬浮弹窗显示详细信息   √
        未完成显示红色          √
        超出部分做成滚动窗口    √
-->

</template>
  
<script>
import { reactive, computed, watchEffect, onMounted } from 'vue'
import axios from 'axios'
import router from '../router'
export default {
    //组件名
    name: 'BackTodo',

    setup() {
        let data1 = reactive({
            todolist: [],
            show: false



        })
        //生命周期函数，
        //onMounted：在初始化页面完成后执行
        onMounted(() => {
            axios.post("api/schedule/", {
                "action": "list_schedule",
                "time": 0,
            }).then(response => {
                
                data1.todolist = response.data.retlist
            }).catch(function (reason) {
                console.log(reason)
            })

        })


        function datachange(time) {
            var time1 = new Date(time);
            var year1 = time1.getFullYear();
            var month1 = time1.getMonth() + 1;
            var data1 = time1.getDate();
            return year1 + '.' + month1 + '.' + data1

        }

        //数据和函数都要返回
        return {
            data1,
            datachange

        }
    },




}
</script>
<style scoped>
.main {
    width: 100%;
    height: 100%;
    background-color: #24263b;
}

.sw{
    position: absolute;
    bottom: 10px;
    left: 50%;
}



/*最外层透明*/
:deep(.el-table),
:deep(.el-table--expanded-cell) {
    background-color: #24263b !important;
    color: white;
    border: 0;

}

/* 表格内背景颜色 */
:deep(.el-table th),
:deep(.el-table tr),
:deep(.el-table td) {
    background-color: #24263b !important;
    border: 0;
    /*去除表格*/

}

/*去除底边框*/
:deep(.el-table td.el-table__cell) {
    border: 0;
}

:deep(.el-table th.el-table__cell.is-leaf) {
    border: 0;
}

/*去除底部灰条.el-table::before*/
:deep(.el-table::before) {
    display: none;
}


.is-finish {
    color: brown;
}
</style>

<style>
.el-calendar-table .el-calendar-day {
    /*修改日历单元格高度*/
    height: 14vh;
    overflow: scroll;
    overflow-y: auto;
    overflow-x: hidden
}

.is-selected {
    color: #1989fa;
}


.el-calendar {
    --el-calendar-border: 0;
    --el-calendar-header-border-bottom: 0;
    --el-calendar-selected-bg-color: #131323;
    background-color: #24263b !important;
    color: white;
}
</style>
  