$(function () {
    $("#account_form").validate({
        rules: {
            inputOldPwd: {
                required: true,
                rangelength: [6, 20]
            },
            inputNewPwd: {
                required: true,
                rangelength: [6, 20],
                notEqual:"#inputOldPwd"
            },
            inputConfirmPwd: {
                required: true,
                rangelength: [6, 20],
                equalTo: "#inputNewPwd"
            }
        },
        messages: {
            inputOldPwd: {
                required: "请输入密码",
                rangelength: "密码为6-20个字符"
            },
            inputNewPwd: {
                required: "请输入密码",
                rangelength: "密码为6-20个字符",
                notEqual:"新密码不能和老密码一致"
            },
            inputConfirmPwd: {
                required: "请输入密码",
                rangelength: "密码为6-20个字符",
                equalTo: "两次密码必须相同"
            }
        },
        errorElement: "em",
        errorPlacement: function (error, element) {
            error.insertAfter(element.parents(".col-sm-5"));
        },
        highlight: function (element, errorClass, validClass) {
            $(element).parents(".form-group").addClass("has-error").removeClass("has-success");
        },
        unhighlight: function (element, errorClass, validClass) {
            $(element).parents(".form-group").addClass("has-success").removeClass("has-error");
        }
    });

    $("#btnChangePwd").click(changePwd);
});

function showMessage(msg, issuccess) {
    cls = issuccess ? "alert-success" : "alert-danger";
    html = "<div id='alert-cgpwd' class='alert'> <a class='close' data-dismiss='alert' href='#'>×</a>" + msg + "</div>";
    $("#div-fail-alert").html(html);
    $("#alert-cgpwd").addClass(cls);
}

function changePwd() {
    if (!$("#account_form").valid()) {
        return;
    }

    var oldpwd = $("#inputOldPwd").val();
    var newpwd = $("#inputNewPwd").val();
    $.ajax({
        type: "POST",
        url: "/usercenter/account/",
        data: {
            old_pwd: oldpwd,
            new_pwd: newpwd
        },
        success: function (res) {
            if (res['status'] == 0) {
                showMessage(res['msg'], true);
                $("#inputNewPwd").val("");
                $("#inputOldPwd").val("");
                $("#inputConfirmPwd").val("");
            }
            else {
                showMessage(res['msg'], false);
                $(".form-group").removeClass("has-success");
            }
        }
    });
}


