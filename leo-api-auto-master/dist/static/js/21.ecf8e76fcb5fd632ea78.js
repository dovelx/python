webpackJsonp([21],{H9Oo:function(e,t,s){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var r=s("woOf"),i=s.n(r),o=s("vMJZ"),a=s("EMlb"),n={name:"UserList",data:function(){return{filters:{email:""},users:[],roles:{admin:"超级管理员",project:"项目管理员",user:"普通用户"},rolesOption:[{name:"admin",description:"超级管理员"},{name:"project",description:"项目管理员"},{name:"user",description:"普通用户"}],projectsOption:[],size:10,skip:0,sortBy:"createAt",order:"descending",pageNum:1,totalNum:0,listLoading:!1,statusChangeLoading:!1,selects:[],editFormVisible:!1,editLoading:!1,editFormRules:{email:[{required:!0,type:"email",trigger:"blur"}],roles:[{required:!0,message:"请选择角色",trigger:"blur"}]},editForm:{email:"",password:"",roleNames:[],userProjects:[]},initPassword:"leo-api-test"}},methods:{queryUsers:function(e){this.listLoading=!0;var t=this;""!==t.filters.email.trim()&&(e.email=t.filters.email.trim()),Object(o.e)(e).then(function(e){var s=e.status,r=e.data;t.listLoading=!1,"ok"===s?(t.totalNum=r.totalNum,t.users=r.rows):t.$message.error({message:r,center:!0})}).catch(function(e){t.$message.error({message:"用户列表获取失败，请稍后刷新重试哦~",center:!0}),t.listLoading=!1})},getUsers:function(){var e={size:this.size,skip:this.skip,sortBy:this.sortBy,order:this.order};this.queryUsers(e)},handleSizeChange:function(e){this.size=e;var t={size:this.size,skip:this.skip,sortBy:this.sortBy,order:this.order};this.queryUsers(t)},handleCurrentChange:function(e){this.skip=(e-1)*this.size;var t={size:this.size,skip:this.skip,sortBy:this.sortBy,order:this.order};this.queryUsers(t)},handleChangeStatus:function(e,t){var s=this;s.statusChangeLoading=!0;var r=!t.active,i={email:t.email,active:r};Object(o.k)(i,{"Content-Type":"application/json"}).then(function(e){var r=e.status,i=e.data;s.statusChangeLoading=!1,"ok"===r?(s.$message({message:i,center:!0,type:"success"}),t.status=!t.status):s.$message.error({message:i,center:!0}),s.getUsers()}).catch(function(){s.$message.error({message:"用户状态更新失败,请稍后重试哦",center:!0}),s.statusChangeLoading=!1,s.getUsers()})},sortChange:function(e){this.sortBy=e.prop,this.order=e.order;var t={size:this.size,skip:this.skip,sortBy:this.sortBy,order:this.order};this.queryUsers(t)},selectsChange:function(e){this.selects=e},reportRowStyle:function(e){var t=e.row;e.rowIndex;return!0!==t.active?"background-color: #DDDDDD":""},ReportTableRow:function(e){e.row,e.rowIndex;return"reportTableRow"},formatRoles:function(e){var t=this;return e.map(function(e){return t.roles[e]}).join(" / ")},handleEdit:function(e,t){this.editFormVisible=!0,console.log(t),this.editForm=i()({},this.editForm,t)},changeUserRoles:function(){var e=this;this.$refs.editForm.validate(function(t){t?e.$confirm("确认提交吗？","提示",{}).then(function(){var t={email:e.editForm.email,roleNames:e.editForm.roleNames};e.editLoading=!0,Object(o.b)(e.editForm.email,t,{}).then(function(t){e.editLoading=!1,"ok"===t.status?e.$message({message:t.data,center:!0}):e.$message.error({message:t.data,center:!0}),e.$refs.editForm.resetFields(),e.editFormVisible=!1,e.getUsers()})}):e.$message.error({message:"表单验证失败",center:!0})})},resetPwd:function(){var e=this;this.$confirm("确认提交吗？","提示",{}).then(function(){var t={email:e.editForm.email,password:e.initPassword};e.editLoading=!0,Object(o.j)(e.editForm.email,t,{}).then(function(t){e.editLoading=!1,"ok"===t.status?e.$message({message:t.data,center:!0}):e.$message.error({message:t.data,center:!0}),e.$refs.editForm.resetFields(),e.editFormVisible=!1,e.getUsers()})})},handleDel:function(e,t){var s=this;this.$confirm("确认删除用户吗？","提示",{}).then(function(){var e=s;e.statusChangeLoading=!0;var r={users:[t.email]};Object(o.d)(r,{"Content-Type":"application/json"}).then(function(t){var s=t.status,r=t.data;e.statusChangeLoading=!1,"ok"===s?e.$message({message:r,center:!0,type:"success"}):e.$message.error({message:r,center:!0}),e.getUsers()}).catch(function(){e.$message.error({message:"删除用户失败,请稍后重试哦",center:!0}),e.statusChangeLoading=!1,e.getUsers()})})},getAllProjects:function(){var e=this;Object(a.c)({},{}).then(function(t){var s=t.status,r=t.data;"ok"===s?e.projectsOption=r.rows:e.$message.error({message:r,center:!0})}).catch(function(t){e.$message.err({message:"项目获取失败，请稍后刷新重试哦~",center:!0})})},changeProjects:function(){var e=this;this.$confirm("确认提交吗？","提示",{}).then(function(){var t={email:e.editForm.email,userProjects:e.editForm.userProjects};e.editLoading=!0,Object(o.c)(e.editForm.email,t,{}).then(function(t){e.editLoading=!1,"ok"===t.status?e.$message({message:t.data,center:!0}):e.$message.error({message:t.data,center:!0}),e.$refs.editForm.resetFields(),e.editFormVisible=!1,e.getUsers()})})}},created:function(){this.getUsers(),this.getAllProjects()}},l={render:function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[r("strong",{staticClass:"title"},[e._v(e._s(e.$route.meta.title))]),e._v(" "),r("el-col",{staticClass:"toolbar",staticStyle:{"padding-bottom":"0px"},attrs:{span:24}},[r("el-form",{attrs:{inline:!0,model:e.filters},nativeOn:{submit:function(e){e.preventDefault()}}},[r("router-link",{staticStyle:{"text-decoration":"none",color:"aliceblue"},attrs:{to:""}},[r("el-button",{staticClass:"return-list",on:{click:function(t){return e.$router.back(-1)}}},[r("i",{staticClass:"el-icon-d-arrow-left",staticStyle:{"margin-right":"5px"}}),e._v("返回\n        ")])],1),e._v(" "),e.$store.getters.roles.includes("admin")?r("el-form-item",{staticStyle:{"margin-left":"35px"}},[r("router-link",{staticStyle:{"text-decoration":"none",color:"aliceblue"},attrs:{to:{name:"Register"}}},[r("el-button",{staticClass:"el-icon-plus",attrs:{type:"primary"}},[e._v("新增用户")])],1)],1):e._e(),e._v(" "),r("div",{staticStyle:{float:"right","margin-right":"95px"}},[r("el-form-item",[r("el-input",{attrs:{placeholder:"邮箱"},nativeOn:{keyup:function(t){return!t.type.indexOf("key")&&e._k(t.keyCode,"enter",13,t.key,"Enter")?null:e.getUsers(t)}},model:{value:e.filters.email,callback:function(t){e.$set(e.filters,"email","string"==typeof t?t.trim():t)},expression:"filters.email"}})],1),e._v(" "),r("el-form-item",[r("el-button",{staticClass:"el-icon-search",attrs:{type:"primary"},on:{click:e.getUsers}},[e._v(" 查询")])],1)],1)],1)],1),e._v(" "),r("el-table",{directives:[{name:"loading",rawName:"v-loading",value:e.listLoading,expression:"listLoading"}],staticStyle:{width:"100%"},attrs:{data:e.users,"row-style":e.reportRowStyle,"row-class-name":e.ReportTableRow,"highlight-current-row":""},on:{"sort-change":e.sortChange,"selection-change":e.selectsChange}},[r("el-table-column",{attrs:{type:"selection","min-width":"5%"}}),e._v(" "),r("el-table-column",{attrs:{prop:"_id",label:"ID","min-width":"20%",sortable:"custom","show-overflow-tooltip":""}}),e._v(" "),r("el-table-column",{attrs:{prop:"email",label:"邮箱","min-width":"20%",sortable:"custom","show-overflow-tooltip":""}}),e._v(" "),r("el-table-column",{attrs:{prop:"roleNames",label:"角色","min-width":"50%","show-overflow-tooltip":""},scopedSlots:e._u([{key:"default",fn:function(t){return[r("span",[e._v(e._s(e.formatRoles(t.row.roleNames)))])]}}])}),e._v(" "),r("el-table-column",{attrs:{prop:"createAt",label:"创建时间","min-width":"20%",sortable:"custom","show-overflow-tooltip":""}}),e._v(" "),r("el-table-column",{attrs:{prop:"active",label:"状态","min-width":"10%",sortable:"custom"},scopedSlots:e._u([{key:"default",fn:function(t){return[r("img",{directives:[{name:"show",rawName:"v-show",value:t.row.active,expression:"scope.row.active"}],attrs:{src:s("7shL")}}),e._v(" "),r("img",{directives:[{name:"show",rawName:"v-show",value:!t.row.active,expression:"!scope.row.active"}],attrs:{src:s("IT+J")}})]}}])}),e._v(" "),r("el-table-column",{attrs:{label:"操作","min-width":"30%"},scopedSlots:e._u([{key:"default",fn:function(t){return[r("el-button",{attrs:{type:"primary",size:"small"},on:{click:function(s){return e.handleEdit(t.$index,t.row)}}},[e._v("编辑")]),e._v(" "),r("el-button",{attrs:{type:"info",size:"small",loading:e.statusChangeLoading},on:{click:function(s){return e.handleChangeStatus(t.$index,t.row)}}},[e._v("\n          "+e._s(!1===t.row.active?"启用":"禁用")+"\n        ")]),e._v(" "),r("el-button",{attrs:{type:"danger",size:"small"},on:{click:function(s){return e.handleDel(t.$index,t.row)}}},[e._v("删除")])]}}])})],1),e._v(" "),r("el-col",{staticClass:"toolbar",attrs:{span:24}},[r("el-pagination",{staticStyle:{float:"right"},attrs:{"page-sizes":[10,20,40],"page-size":e.size,layout:"total, sizes, prev, pager, next, jumper",total:e.totalNum},on:{"size-change":e.handleSizeChange,"current-change":e.handleCurrentChange}})],1),e._v(" "),r("el-dialog",{staticStyle:{width:"70%",left:"15%"},attrs:{title:"编辑用户",visible:e.editFormVisible,"close-on-click-modal":!1},on:{"update:visible":function(t){e.editFormVisible=t}}},[r("el-form",{ref:"editForm",attrs:{model:e.editForm,rules:e.editFormRules,"label-width":"80px"}},[r("el-form-item",{attrs:{label:"邮箱",prop:"email"}},[r("el-input",{attrs:{disabled:""},model:{value:e.editForm.email,callback:function(t){e.$set(e.editForm,"email","string"==typeof t?t.trim():t)},expression:"editForm.email"}})],1),e._v(" "),r("el-form-item",{attrs:{label:"角色",prop:"roleNames"}},e._l(e.rolesOption,function(t,s){return r("el-checkbox-group",{key:s,model:{value:e.editForm.roleNames,callback:function(t){e.$set(e.editForm,"roleNames",t)},expression:"editForm.roleNames"}},[r("el-checkbox",{attrs:{label:t.name}},[e._v(e._s(t.description))])],1)}),1),e._v(" "),r("el-form-item",{attrs:{label:"项目权限",prop:"userProjects"}},e._l(e.projectsOption,function(t){return r("el-checkbox-group",{key:t._id,model:{value:e.editForm.userProjects,callback:function(t){e.$set(e.editForm,"userProjects",t)},expression:"editForm.userProjects"}},[r("el-checkbox",{attrs:{label:t._id}},[e._v(e._s(t.name))])],1)}),1)],1),e._v(" "),r("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[r("span",[e._v("初始密码: "+e._s(e.initPassword))]),e._v(" "),r("el-button",{attrs:{type:"primary"},nativeOn:{click:function(t){return e.resetPwd(t)}}},[e._v("重置密码")]),e._v(" "),r("br"),e._v(" "),r("br"),e._v(" "),r("el-button",{attrs:{type:"primary",loading:e.editLoading},nativeOn:{click:function(t){return e.changeProjects(t)}}},[e._v("修改项目权限")]),e._v(" "),r("el-button",{attrs:{type:"primary",loading:e.editLoading},nativeOn:{click:function(t){return e.changeUserRoles(t)}}},[e._v("修改角色")]),e._v(" "),r("el-button",{nativeOn:{click:function(t){e.editFormVisible=!1}}},[e._v("取消")])],1)],1)],1)},staticRenderFns:[]};var c=s("VU/8")(n,l,!1,function(e){s("yjAe")},"data-v-62689651",null);t.default=c.exports},yjAe:function(e,t){}});
//# sourceMappingURL=21.ecf8e76fcb5fd632ea78.js.map