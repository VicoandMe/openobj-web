/**
 * Created by yoyo on 16/3/20.
 */

function register() {
    var input_username = $("#input_username").val();
    var input_email = $("#input_email").val();
    var input_password = $("#input_password").val();
	$.ajax( {
	         type : "POST",
	         url : "/usercenter/register/",
	         data : {
	         	username:input_username,
                email:input_email,
                password:input_password,
	         },
	         success : function(res) {
	            if(res['status'] == 0)
	            {
	            	window.location.href="/usercenter/register/success/";
	            }
	            else
	            {
	            	alert(res['msg'])
	            }
	         }
	        });
}

