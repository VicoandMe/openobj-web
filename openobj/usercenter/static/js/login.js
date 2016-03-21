/**
 * Created by yoyo on 16/3/20.
 */

function login() {
    var input_email = $("#input_email").val();
    var input_password = $("#input_password").val();
	$.ajax( {
	         type : "POST",
	         url : "/usercenter/login/",
	         data : {
                email:input_email,
                password:input_password,
	         },
	         success : function(res) {
	            if(res['status'] == 0)
	            {
	            	window.location.href="/";
	            }
	            else
	            {
	            	alert(res['msg'])
	            }
	         }
	        });
}


