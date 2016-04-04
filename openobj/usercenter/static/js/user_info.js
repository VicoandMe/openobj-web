/**
 * Created by Administrator on 2016/4/2.
 */

$(function(){
	var checkNewPassword = function(){
		var now_password = $("#now_password").val().trim();
		var new_Password = $("#new_password").val().trim();
		if(new_Password!=""&&new_Password.length >= 6 && new_Password.length <= 20) {
			if (new_Password == now_password) {
				showError("new_password","新密码不能和老密码一致");
				return;
			}
			var hasNum = new_Password.match(/[0-9]/gi);
			var hasW = new_Password.match(/[A-Za-z]/gi);
			var has_ = new_Password.match(/[^0-9A-Za-z]/gi);
			var st = (hasNum ? 1 : 0) + (hasW ? 1 : 0) + (has_ ? 1 : 0);
			if (st == 1) {
				showPasswordStrength("weak");
			} else if (st == 2) {
				showPasswordStrength("middle");
			} else if (st == 3) {
				showPasswordStrength("strong");
			}
			checkForm_password += 1;
		}else{
			showError("new_password","");
		}
	}
	var showError = function(id,word){
		if(word.trim()!=""){
			$("."+id+"-tr .redtxt").html(word);
		}
		$("."+id+"-tr .redtxt").parent().siblings().hide();
		$("."+id+"-tr .redtxt").parent().show();
	}
	var showPasswordStrength = function(strength){
		$(".new_password-tr #prompt-"+strength).siblings().hide();
		$(".new_password-tr #prompt-"+strength).show();
	}
	var initError = function(id){
		$("."+id+"-tr .error-td").children().hide();
	}
	var checkNewPassword2 = function(){
		var new_Password = $("#new_password").val().trim();
		var confirm_Password = $("#confirm_password").val().trim();
		if(confirm_Password!=""&&new_Password!=""&&confirm_Password==new_Password){
			showError("confirm_password","");
			$(".confirm_password-tr .error-td em").removeClass("id-password-ico1");
			$(".confirm_password-tr .error-td em").addClass("id-password-ico2");
			$(".confirm_password-tr .error-td .redtxt").html("");
			checkForm_password += 1;
		}else if(confirm_Password!=""&&new_Password!=""&&confirm_Password!=new_Password){
			$(".confirm_password-tr .error-td em").removeClass("id-password-ico2");
			$(".confirm_password-tr .error-td em").addClass("id-password-ico1");
			showError("confirm_password","两次输入的密码不一致");
		}
	}
	var checkPassword = function(){
		var now_password = $("#now_password").val().trim();
		if(now_password.length == 0){
			showError("now_password","请输入密码");
		}else{
			initError("now_password");
			checkForm_password += 1;
		}
	}
	$("#now_password").blur(function(){
		checkPassword();
	})
	$("#now_password").focus(function(){
		initError("now_password");
	})
	$("#new_password").blur(function(){
		checkNewPassword("");
	})
	$("#new_password").focus(function(){
		initError("new_password");
	})
	$("#confirm_password").blur(function(){
		checkNewPassword2();
	})
	$("#confirm_password").focus(function(){
		initError("confirm_password");
	})
	window.resetSuccess = function(){
		$("#setsuccessbox").hide();
		window.location.href = "usercenter/user/info";
	}
	window.checkForm_password = 0;
	function pwdsavecheck() {
		checkForm_password = 0;
		checkNewPassword2(checkNewPassword(checkPassword(dataverify_password())));
		console.log("check over : " + checkForm_password);
		if (checkForm_password == 4) {
			//console.log("准备提交");
			var now_password = $("#now_password").val();
			var new_password = $("#new_password").val();
			var confirm_password = $("confirm_password").val();
			$.ajax({
				type: "post",
				url: "usercenter/user_info",
				data: {
					nowpassword: now_password,
					newpassword: new_password,
					confirmpassword: confirm_password,
				},
				success: function (res) {
					if (data.errorCode == 0 && res['status'] == 0) {
						$("#setsuccessbox").show();
						setTimeout("resetSuccess()", 1000);
					} else if (data.errorCode == 5) {
						$(".password-checkcode .gt_refresh_tips").trigger("click");
						$("#now_password").val("");
						$("#new_password").val("");
						$("#confirm_password").val("");
						initError("new_password");
						initError("confirm_password");
						showError("now_password", "密码不正确");
					}
				}
			})
		}
	}
	$("#passwordsave").click(function(){
		pwdsavecheck();
	})
});
