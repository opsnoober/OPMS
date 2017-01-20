$('#loginbtn').on('click',function(e){
      var user = $('#username').val();
      var pwd = $('#password').val();
      var msg = $('#msg');
      if (user&&pwd) {
	$.ajax({
        url: "/api/auth/checklogin",
        type: "post",
        data: {"username":user,"password":pwd},
        dataType: "json",
	success:function(res){
		//alert(res.code);
	    if (res.code == 0){
			//swal('登录成功');
			location.href='/index';	
            		//window.location='/index'
			}else{
			swal('','用户名或密码错误','error');	
			}
        	}
	    });
	}else{
		swal('','请输入用户名密码','info')
	}
})


$(document).keyup(function(event){
  if(event.keyCode ==13){
    $("#loginbtn").trigger("click");
  }
});
/*
        $.post('/api/auth/checklogin',{username:user,password:pwd},function(res){
          if (res.code==0) {
            //location.href='/index'
            window.location='/index'
          }else{
            msg.html('用户名或密码错误')
          }
        })
      }else{
        msg.html('请输入用户名和密码')
      }
    })
*/
