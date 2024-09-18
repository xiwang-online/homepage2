<template>
    <div class="main">
        <el-table :data="data.notes" height="85vh" style="width: 100%">
            <el-table-column type="index" width="50"/>
            <el-table-column prop="id" label="ID" width="50" />
            <el-table-column prop="content" label="内容" width="1000" />
            <el-table-column prop="time" label="创建日期" width="100" />
            <el-table-column prop="waste" label="状态" width="80"/>
            <el-table-column prop="remark" label="备注"/>
            <el-table-column fixed="right" label="Operations" width="120">
                <template #default="scope">
                    <el-button link type="primary" @click="modify(scope.row)">修改</el-button>
                    <el-popconfirm title="确定要删除吗?" @confirm="deletenote(scope.row.id)">
                        <template #reference>
                            <el-button link type="primary">删除</el-button>
                        </template>
                    </el-popconfirm>
                </template>
            </el-table-column>
        </el-table>
        <el-button class="but" type="primary" @click="add">添加</el-button>

        <el-dialog v-model="data.modifydialog" title="修改">
            <span>ID:{{ data.modifydata.id }}</span><br>
            <span>内容:</span>
            <el-input v-model="data.modifydata.content" />
            <span>创建日期:</span>
            <el-input v-model="data.modifydata.time" />
            <span>状态:</span>
            <el-input v-model="data.modifydata.waste" />
            <span>备注:</span>
            <el-input v-model="data.modifydata.remark" />
            <el-button class="but" type="primary" @click="modifysubmit">提交</el-button>
        </el-dialog>


        <el-dialog v-model="data.adddialog" title="添加">
            <span>内容:</span>
            <el-input v-model="data.adddata.content" />
            <span>创建日期:</span>
            <el-input v-model="data.adddata.time" />
            <span>状态:</span>
            <el-input v-model="data.adddata.waste" />
            <span>备注:</span>
            <el-input v-model="data.adddata.remark" />
            <el-button class="but" type="primary" @click="addsubmit">提交</el-button>
        </el-dialog>



    </div>
</template>
  
  <script>
import { reactive, computed, watchEffect, onMounted } from 'vue'
import axios from 'axios'
import router from '../router'
export default {
    //组件名
    name: 'BackWebMark',

    setup() {
        let data = reactive({
            notes: [],
            modifydialog: false,   //修改框是否显示
            modifydata: {},  //要修改的数据
            adddialog: false,
            adddata: {
                content: "",
                time: "",
                waste:1,
                remark: "",

            }

        })
        //生命周期函数，
        //onMounted：在初始化页面完成后执行
        onMounted(() => {
            axios.post("api/notes/", {
                "action": "list_notes",
                "waste":0
            })
                .then(function (value) {
                    //console.log(value);
                    data.notes = value.data.retlist;
                })
                .catch(function (reason) {
                    console.log(reason)
                })
        })


        function deletenote(id) {
            axios.post("api/notes/", {
                "action": "del_notes",
                "id": id,
            }).then(function (response) {
                if (response.data.ret == 0) {
                    data.modifydialog = false
                    data.notes = data.notes.filter((note) => { return note.id != id })   //从数组中去掉被删掉的数据
                } else if (response.data.ret == 302) {
                    alert("未登录");
                    router.push("signin");
                }
            }).catch(function (error) {
                console.log(error);
                alert("未知错误");
            });





        }

        function modify(da) {
            data.modifydata = da
            data.modifydialog = true
        }


        function modifysubmit() {
            axios.post("api/notes/", {
                "action": "modify_notes",
                "id": data.modifydata.id,
                "data": {
                    "content": data.modifydata.content,
                    "time": data.modifydata.time,
                    "waste": data.modifydata.waste,
                    "remark":data.modifydata.remark
                },
            }).then(function (response) {
                if (response.data.ret == 0) {
                    data.modifydialog = false
                } else if (response.data.ret == 302) {
                    alert("未登录");
                    router.push("signin");
                }
            }).catch(function (error) {
                console.log(error);
                alert("未知错误");
            });
        }



        function add() {
            data.adddialog = true
        }

        function addsubmit() {
            axios.post("api/notes/", {
                "action": "add_notes",
                "data": data.adddata
            }).then(function (response) {
                if (response.data.ret == 0) {
                    data.adddialog = false
                    const noteObj = { id: response.data.id, content: data.adddata.content, time: data.adddata.time, waste: data.adddata.waste, reamrk:data.adddata.remark };
                    data.notes.push(noteObj)
                    data.adddata.content = ""
                    data.adddata.time= ""
                    data.adddata.waste=1
                    data.adddata.remark = ""
                } else if (response.data.ret == 302) {
                    alert("未登录");
                    router.push("signin");
                }
            }).catch(function (error) {
                console.log(error);
                alert("未知错误");
            });
        }


        //数据和函数都要返回
        return {
            data,
            deletenote,
            modify,
            modifysubmit,
            add,
            addsubmit

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



.but{
    margin: 20px 5px;

}


span{
    font-size: 20px;
    font-weight: 900;
}
</style>
  