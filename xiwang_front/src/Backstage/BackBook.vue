<template>
    <div class="main">
        <el-table :data="data.books" height="85vh" style="width: 100%">
            <el-table-column type="index" width="50"/>
            <el-table-column prop="id" label="ID" width="50" />
            <el-table-column prop="bookname" label="书名" width="220" />
            <el-table-column prop="author" label="作者" width="200" />
            <el-table-column prop="wordCount" label="字数" width="80" />
            <el-table-column prop="readdata" label="读完日期" width="100" />
            <el-table-column prop="read" label="在未已" width="80" />
            <el-table-column prop="notes" label="评论" width="260" :show-overflow-tooltip='true'/>
            <el-table-column prop="remark" label="备注" :show-overflow-tooltip='true' />
            <el-table-column fixed="right" label="Operations" width="120">
                <template #default="scope">
                    <el-button link type="primary" @click="modify(scope.row)">修改</el-button>
                    <el-popconfirm title="确定要删除吗?" @confirm="deletebook(scope.row.id)">
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
            <span>书名:</span>
            <el-input v-model="data.modifydata.bookname" />
            <span>作者:</span>
            <el-input v-model="data.modifydata.author" />
            <span>字数:</span>
            <el-input v-model="data.modifydata.wordCount" />
            <span>日期:</span>
            <el-input v-model="data.modifydata.readdata" />
            <span>在未已:</span>
            <el-input v-model="data.modifydata.read" />
            <span>评论:</span>
            <el-input v-model="data.modifydata.notes" />
            <span>备注:</span>
            <el-input v-model="data.modifydata.remark" />
            <el-button class="but" type="primary" @click="modifysubmit">提交</el-button>
        </el-dialog>


        <el-dialog v-model="data.adddialog" title="添加">
            <span>书名:</span>
            <el-input v-model="data.adddata.bookname" />
            <span>作者:</span>
            <el-input v-model="data.adddata.author" />
            <span>字数:</span>
            <el-input v-model="data.adddata.wordCount" />
            <span>日期:</span>
            <el-input v-model="data.adddata.readdata" />
            <span>在未已:</span>
            <el-input v-model="data.adddata.read" />
            <span>评论:</span>
            <el-input v-model="data.adddata.notes" />
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
    name: 'BackBook',

    setup() {
        let data = reactive({
            books: [],
            modifydialog: false,   //修改框是否显示
            modifydata: {},  //要修改的数据
            adddialog: false,
            adddata: {
                bookname: "",
                author: "",
                wordCount: "",
                readdata: "",
                read: "",
                notes: "",
                remark: "",

            }

        })
        //生命周期函数，
        //onMounted：在初始化页面完成后执行
        onMounted(() => {
            axios.post("api/books/", {
                "action": "list_book",
                "read": 0
            })
                .then(function (value) {
                    data.books = value.data.retlist;
                })
                .catch(function (reason) {
                    console.log(reason)
                })
        })


        function deletebook(id) {
            axios.post("api/books/", {
                "action": "del_book",
                "id": id,
            }).then(function (response) {
                if (response.data.ret == 0) {
                    data.modifydialog = false
                    data.books = data.books.filter((book) => { return book.id != id })   //从数组中去掉被删掉的数据
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
            axios.post("api/books/", {
                "action": "modify_book",
                "id": data.modifydata.id,
                "data": {
                    "bookname": data.modifydata.bookname,
                    "author": data.modifydata.author,
                    "wordcount": data.modifydata.wordCount,
                    "readdata": data.modifydata.readdata,
                    "read": data.modifydata.read,
                    "notes": data.modifydata.notes,
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
            axios.post("api/books/", {
                "action": "add_book",
                "data": data.adddata
            }).then(function (response) {
                if (response.data.ret == 0) {
                    data.adddialog = false
                    const bookObj = {
                        id: response.data.id,
                        bookname: data.adddata.bookname,
                        author: data.adddata.author,
                        wordcount: data.adddata.wordCount,
                        readdata: data.adddata.readdata,
                        read: data.adddata.read,
                        notes: data.adddata.notes,
                        remark: data.adddata.remark,
                    };
                    data.books.push(bookObj)
                    data.adddata.bookname = ""
                    data.adddata.author = ""
                    data.adddata.wordCount = ""
                    data.adddata.readdata = ""
                    data.adddata.read = ""
                    data.adddata.notes = ""
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
            deletebook,
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