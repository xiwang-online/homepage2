<template>
    <div class="main">
        <el-table :data="data.webs"  height="85vh" style="width: 100%">
            <el-table-column type="index" width="50"/>
            <el-table-column prop="id" label="ID" width="50" />
            <el-table-column prop="webname" label="网站名" width="250" />
            <el-table-column prop="weburl" label="链接" width="500" />
            <el-table-column prop="remark" label="备注" />
            <el-table-column fixed="right" label="Operations" width="120">
                <template #default="scope">
                    <el-button link type="primary" @click="modify(scope.row)">修改</el-button>
                    <el-popconfirm title="确定要删除吗?" @confirm="deleteweb(scope.row.id)">
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
            <span>网站名:</span>
            <el-input v-model="data.modifydata.webname" />
            <span>链接:</span>
            <el-input v-model="data.modifydata.weburl" />
            <span>备注:</span>
            <el-input v-model="data.modifydata.remark" />
            <el-button class="but" type="primary" @click="modifysubmit">提交</el-button>
        </el-dialog>


        <el-dialog v-model="data.adddialog" title="添加">
            <span>网站名:</span>
            <el-input v-model="data.adddata.webname" />
            <span>链接:</span>
            <el-input v-model="data.adddata.weburl" />
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
            webs: [],
            modifydialog: false,   //修改框是否显示
            modifydata: {},  //要修改的数据
            adddialog: false,
            adddata: {
                webname: "",
                weburl: "",
                remark: "",

            }

        })
        //生命周期函数，
        //onMounted：在初始化页面完成后执行
        onMounted(() => {
            axios.post("api/web/", {
                "action": "list_web",
            })
                .then(function (value) {
                    data.webs = value.data.retlist;
                })
                .catch(function (reason) {
                    console.log(reason)
                })
        })


        function deleteweb(id) {
            axios.post("api/web/", {
                "action": "del_web",
                "id": id,
            }).then(function (response) {
                if (response.data.ret == 0) {
                    data.modifydialog = false
                    data.webs = data.webs.filter((web) => { return web.id != id })   //从数组中去掉被删掉的数据
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
            axios.post("api/web/", {
                "action": "modify_web",
                "id": data.modifydata.id,
                "newdata": {
                    "webname": data.modifydata.webname,
                    "weburl": data.modifydata.weburl,
                    "remark": data.modifydata.remark,
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
            axios.post("api/web/", {
                "action": "add_web",
                "data": data.adddata
            }).then(function (response) {
                if (response.data.ret == 0) {
                    data.adddialog = false
                    const webObj = { id: response.data.id, webname: data.adddata.webname, weburl: data.adddata.weburl, remark: data.adddata.remark };
                    data.webs.push(webObj)
                    data.adddata.webname = ""
                    data.adddata.weburl = ""
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
            deleteweb,
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
  