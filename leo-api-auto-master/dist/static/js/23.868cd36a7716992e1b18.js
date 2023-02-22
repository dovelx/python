webpackJsonp([23],{ZKLk:function(t,e,o){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var r=o("/FC1"),s={name:"TestReportCronJob",data:function(){return{filters:{reportId:""},testReports:[],size:10,skip:0,sortBy:"createAt",order:"descending",pageNum:1,totalNum:0,listLoading:!1,statusChangeLoading:!1,selects:[],cleanDate:null,cleanDateOptions:[{value:null,label:"未选择"},{value:30,label:"30天之前"},{value:7,label:"7天之前"},{value:0,label:"全部删除"}]}},methods:{queryTestReports:function(t){this.listLoading=!0;var e=this;""!==e.filters.reportId.trim()&&(t.reportId=e.filters.reportId.trim());Object(r.e)(this.$route.params.project_id,t,{}).then(function(t){var o=t.status,r=t.data;e.listLoading=!1,"ok"===o?(e.totalNum=r.totalNum,e.testReports=r.rows):e.$message.error({message:r,center:!0})}).catch(function(t){e.$message.error({message:"报告列表获取失败，请稍后刷新重试哦~",center:!0}),e.listLoading=!1})},getReports:function(){var t={size:this.size,skip:this.skip,sortBy:this.sortBy,order:this.order,projectId:this.$route.params.project_id,executionMode:"cronJob"};this.queryTestReports(t)},selectsChange:function(t){this.selects=t},handleSizeChange:function(t){this.size=t;var e={size:this.size,skip:this.skip,sortBy:this.sortBy,order:this.order,projectId:this.$route.params.project_id};this.queryTestReports(e)},handleCurrentChange:function(t){this.skip=(t-1)*this.size;var e={size:this.size,skip:this.skip,sortBy:this.sortBy,order:this.order,projectId:this.$route.params.project_id};this.queryTestReports(e)},reportRowStyle:function(t){var e=t.row;t.rowIndex;return e.totalCount>e.passCount?"background-color: #ddd;":""},ReportTableRow:function(t){t.row,t.rowIndex;return"reportTableRow"},sortChange:function(t){this.sortBy=t.prop,this.order=t.order;var e={size:this.size,skip:this.skip,sortBy:this.sortBy,order:this.order,projectId:this.$route.params.project_id};this.queryTestReports(e)},getPassRate:function(t,e,o){return t=parseFloat(t),e=parseFloat(e),isNaN(t)||isNaN(e)?"-":o?e<=0?"0%":Math.round(t/e*1e4)/100+"%":e<=0?0:Math.round(t/e*1e4)/100},cleanReports:function(){var t=this;this.$confirm("确认删除报告吗?","提示",{type:"warning"}).then(function(e){if(null!=t.cleanDate){var o=t;o.listLoading=!0;var s={cleanDate:o.cleanDate,projectId:o.$route.params.project_id,operator:o.$store.getters.email,executionMode:"cronJob"};Object(r.a)(t.$route.params.project_id,s,{}).then(function(e){o.listLoading=!1;var r=e.status,s=e.data;"ok"===r?(o.$message.info({message:"~~删除报告成功~~",center:!0}),t.getReports()):(o.$message.error({message:s,center:!0}),t.getReports())}).catch(function(e){o.listLoading=!1,o.$message.error({message:"删除报告失败，请稍后刷新重试哦~",center:!0}),t.getReports()})}else t.$message.error({message:"请选择删除日期",center:!0})})}},created:function(){this.getReports()}},a={render:function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("section",[r("strong",{staticClass:"title"},[t._v(t._s(t.$route.meta.title))]),t._v(" "),t.$store.getters.roles.includes("admin")?r("el-form",{attrs:{inline:!0}},[r("el-form-item",{staticStyle:{float:"right","margin-right":"30px"}},[r("el-select",{staticStyle:{"margin-right":"20px"},attrs:{placeholder:"删除日期"},model:{value:t.cleanDate,callback:function(e){t.cleanDate=e},expression:"cleanDate"}},t._l(t.cleanDateOptions,function(t,e){return r("el-option",{key:e+"",attrs:{label:t.label,value:t.value}})}),1),t._v(" "),r("el-form-item",[r("el-button",{staticClass:"el-icon-delete",attrs:{type:"danger"},on:{click:t.cleanReports}},[t._v(" 删除报告")])],1)],1)],1):t._e(),t._v(" "),r("el-table",{directives:[{name:"loading",rawName:"v-loading",value:t.listLoading,expression:"listLoading"}],staticStyle:{width:"100%"},attrs:{data:t.testReports,"row-style":t.reportRowStyle,"row-class-name":t.ReportTableRow,"highlight-current-row":""},on:{"sort-change":t.sortChange,"selection-change":t.selectsChange}},[r("el-table-column",{attrs:{type:"selection","min-width":"3%"}}),t._v(" "),r("el-table-column",{attrs:{prop:"_id",label:"报告编号","min-width":"15%",sortable:"custom","show-overflow-tooltip":""}}),t._v(" "),r("el-table-column",{attrs:{prop:"cronJobId",label:"定时任务","min-width":"10%",sortable:"custom","show-overflow-tooltip":""}}),t._v(" "),r("el-table-column",{attrs:{prop:"testEnvName",label:"测试环境","min-width":"8%","show-overflow-tooltip":""}}),t._v(" "),r("el-table-column",{attrs:{prop:"testStartTime",label:"开始时间","min-width":"20%",sortable:"custom","show-overflow-tooltip":""}}),t._v(" "),r("el-table-column",{attrs:{prop:"spendTimeInSec",label:"用时(秒)","min-width":"10%",sortable:"custom","show-overflow-tooltip":""}}),t._v(" "),r("el-table-column",{attrs:{prop:"totalCount",label:"总数","min-width":"8%","show-overflow-tooltip":""}}),t._v(" "),r("el-table-column",{attrs:{prop:"passCount",label:"通过数","min-width":"8%","show-overflow-tooltip":""}}),t._v(" "),r("el-table-column",{attrs:{prop:"failCount",label:"失败数","min-width":"8%","show-overflow-tooltip":""}}),t._v(" "),r("el-table-column",{attrs:{prop:"errorCount",label:"错误数","min-width":"8%","show-overflow-tooltip":""}}),t._v(" "),r("el-table-column",{attrs:{prop:"passRate",label:"通过率","min-width":"10%","show-overflow-tooltip":""},scopedSlots:t._u([{key:"default",fn:function(e){return[t._v("\n        "+t._s(t.getPassRate(e.row.passCount,e.row.totalCount,!0))+"\n      ")]}}])}),t._v(" "),r("el-table-column",{attrs:{prop:"status",label:"测试结果","min-width":"10%"},scopedSlots:t._u([{key:"default",fn:function(e){return[r("img",{directives:[{name:"show",rawName:"v-show",value:e.row.totalCount==e.row.passCount,expression:"scope.row.totalCount==scope.row.passCount"}],attrs:{src:o("7shL")}}),t._v(" "),r("img",{directives:[{name:"show",rawName:"v-show",value:e.row.totalCount>e.row.passCount,expression:"scope.row.totalCount>scope.row.passCount"}],attrs:{src:o("IT+J")}})]}}])}),t._v(" "),r("el-table-column",{attrs:{label:"操作","min-width":"20%"},scopedSlots:t._u([{key:"default",fn:function(e){return[r("router-link",{staticStyle:{"text-decoration":"none",color:"#000000"},attrs:{to:{name:"TestReportDetail",params:{project_id:t.$route.params.project_id,report_id:e.row._id}}}},[r("el-button",{attrs:{type:"primary",size:"small"}},[t._v("查看详情")])],1)]}}])})],1),t._v(" "),r("el-col",{staticClass:"toolbar",attrs:{span:24}},[r("el-pagination",{staticStyle:{float:"right"},attrs:{"page-sizes":[10,20,40],"page-size":t.size,layout:"total, sizes, prev, pager, next, jumper",total:t.totalNum},on:{"size-change":t.handleSizeChange,"current-change":t.handleCurrentChange}})],1)],1)},staticRenderFns:[]};var i=o("VU/8")(s,a,!1,function(t){o("v1di")},"data-v-3c1781af",null);e.default=i.exports},v1di:function(t,e){}});
//# sourceMappingURL=23.868cd36a7716992e1b18.js.map