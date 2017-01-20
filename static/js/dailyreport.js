var $table=$("#dailytable");
		$table.bootstrapTable({
			url: '/api/dailyreport/list',
			method: 'get',                      //请求方式（*）
            toolbar: '#toolbar',                //工具按钮用哪个容器
			striped: true,                      //是否显示行间隔色
            cache: false,                       //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
 		    pagination: true,                   //是否显示分页（*）
    		sortable: true,                     //是否启用排序
    		sortOrder: "desc",                   //排序方式
    		sidePagination: "server",           //分页方式：client客户端分页，server服务端分页（*）
    		pageNumber: 1,                       //初始化加载第一页，默认第一页
    		pageSize: 10,                       //每页的记录行数（*）
    		pageList: [10, 20, 50, 100],        //可供选择的每页的行数（*）
    		search: true,                       //是否显示表格搜索，此搜索是客户端搜索，不会进服务端，所以，个人感觉意义不大
    		strictSearch: true,
    		showColumns: true,                  //是否显示所有的列
    		showRefresh: true,                  //是否显示刷新按钮
    		minimumCountColumns: 2,             //最少允许的列数
    		clickToSelect: true,                //是否启用点击选中行
    		height: 600,                        //行高，如果没有设置height属性，表格自动根据记录条数觉得表格高度
    		uniqueId: "daily_id",                     //每一行的唯一标识，一般为主键列
    		showToggle: true,                    //是否显示详细视图和列表视图的切换按钮
    		cardView: false,                    //是否显示详细视图
    		detailView: false,                   //是否显示父子表
    		// rowStyle: function (row, index) {
      //           //这里有5个取值代表5中颜色['active', 'success', 'info', 'warning', 'danger'];
      //           	var strclass = "";
      //           		if (row.status == "wks") {
      //               			strclass = 'info';//还有一个active
      //           		}
      //           		else if (row.status == "jxz") {
      //               			strclass = 'warning';
      //           		}
      //           		else if (row.status == "ywc") {
      //               			strclass = 'success';
      //           		}
      //           		else {
      //               			return {};
      //           		}
      //           		return { classes: strclass }
      //       		},
	    		// showExport: true,                     //是否显示导出
       //      		exportDataType: "basic",              //basic', 'all', 'selected'.
	                //queryParamsType : "undefined",   
	                queryParamsType : "limit",   
            		queryParams: function queryParams(params) {   //设置查询参数  
				// var userid = GetQueryString("userid");
                var userid = $('#userid').text();
              	var param = {    
    					userid:userid,
    					offset: params.offset, //起始
    					limit: params.limit,  //限制
    					order: params.order,  
    					sort: params.sort,
              		};    
              			    return param;                   
            			},
			columns: [{
			    checkbox: true
			}, {
			    field: 'daily_id',
			    title: 'id',
			    visible: false,
			    sortable: true,
			}, {
			//    field: 'userid',
			  //  title: 'userid',
			    //visible: false,
			//}, {
			    // field: 'week',
			    // title: '周',
			    // editable: {
       //                          type: 'select',
       //                          name: '周',
       //                          sortable: true,
       //                          source: [
       //                              {value:'mon' , text: '周一'},
       //                              {value:'thu' , text: '周二'},
       //                              {value:'wed' , text: '周三'},
       //                              {value:'thu' , text: '周四'},
       //                              {value:'fri' , text: '周五'},
       //                              {value:'sat' , text: '周六'},
       //                              {value:'sun' , text: '周日'},
       //                          ]
       //                      }
			// }, {
			    field: 'content',
			    title: '工作内容',
			}, {
			    field: 'status',
			    title: '状态',

                formatter: function(value,row,index) {  
            //通过判断单元格的值，来格式化单元格，返回的值即为格式化后包含的元素  
            var text='';
            var a='';
                if(value == "wks"){
                    var text = "未开始";
                    var a = '<span class="text-info">'+text+'</span>';
                }else if(value == "ywc"){
                    var text = "已完成";
                    var a = '<span class="text-success">'+text+'</span>';
                }else if(value == "jxz"){
                    var text = "进行中";
                    var a = '<span class="text-warning">'+text+'</span>';
                };
                return a;  
        },
			    // editable: {
       //                          type: 'select',
       //                          name: '状态',
       //                          sortable: true,
       //                          class: 'text-danger',
       //                          source: [
       //                              {value:'wks' , text: '未开始'},
       //                              {value:'ywc' , text: '已完成'},
       //                              {value: 'jxz', text: '进行中'},
       //                          ]
       //                      }

			}, {
			    field: 'man_hours',
			    title: '工时',
			    editable: {
                    		type: 'text',
                    		title: '工时',
                    		}
			}, {
                field: 'createtime',
                title: '创建时间',
                sortable: true,
            }, {
			    field: 'operation',
			    title: '操作',
                formatter:function(value,row,index){
                    var s = '<a class = "edit" href="javascript:void(0)">修改</a>';
                    var d = '<a class = "remove" href="javascript:void(0)">删除</a>';
                    return '<span>'+s+' '+d+'<span>';
                    },
                events: 'operateEvents'
			}, ],

			//oneditable 事件
			onEditableSave: function (field, row, oldValue, $el) {
			$table.bootstrapTable("resetView");
                	$.ajax({
               			type: "post",
                    		url: "/api/dailyreport/edit",
                    		data: row,
                    		dataType: 'JSON',
                    		success: function (data, status) {
                        		if (status == "success") {
                            			alert('提交数据成功');
						$table.bootstrapTable("refresh");
					
                        		}
                    		},
                    		error: function () {
                        		alert('编辑失败');
                    		},
                    		complete: function () {

                    		}

                	    });
            		}

		});

window.operateEvents = {
    'click .edit': function (e, value, row, index) {
        $.ajax({
            type: "post",
            data: row,
            url: '/api/dailyreport/edit',
            success: function (data) {
                alert('修改成功');
            }
        });
    },
    'click .remove': function (e, value, row, index) {
        $.ajax({
            type: "post",
            data: row,
            url: '/api/dailyreport/del',
            success: function (data) {
                alert('删除成功');
                $('#querylist').bootstrapTable('remove', {
                    field: 'MeterMeasureHistoryID',
                    values: [row.MeterMeasureHistoryID]
                });
            }
        });
    }
};