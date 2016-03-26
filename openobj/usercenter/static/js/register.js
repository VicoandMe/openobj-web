/**
 * Created by yoyo on 16/3/20.
 */

$(function () {
    $("#regForm").validate({
        rules: {
            email: {
                required: true,
                email: true
            },
            username: {
                required: true,
                rangelength: [6, 20],
                pltusername: true
            },
            password: {
                required: true,
                rangelength: [6, 20]
            }
        },
        messages: {
            email: {
                required: "请输入邮箱",
                email: "请输入正确邮箱"
            },
            username: {
                required: "请输入用户名",
                rangelength: "用户名6-20位字符",
                pltusername: "用户名只能包含数字、字母、下划线"
            },
            password: {
                required: "请输入密码",
                rangelength: "密码长度6-20位"
            }
        },
        errorElement: "em",
        errorPlacement: function (error, element) {
            error.addClass("valid-msg");
            error.insertAfter(element.parents(".input-group,.my-group"));
        },
        highlight: function (element, errorClass, validClass) {
            $(element).parents(".input-group,.my-group").addClass("has-error").removeClass("has-success");
        },
        unhighlight: function (element, errorClass, validClass) {
            $(element).parents(".input-group,.my-group").addClass("has-success").removeClass("has-error");
        }
    });

    document.onkeydown = function (e) {
        if (e.keyCode == 13)
            register();
    };

    $("#btnRegister").click(register);

});

function register() {
    if (!$("#regForm").valid()) {
        return;
    }

    var input_username = $("#input-username").val();
    var input_email = $("#input-email").val();
    var input_password = $("#input-password").val();
    $.ajax({
        type: "POST",
        url: "/usercenter/register/",
        data: {
            username: input_username,
            email: input_email,
            password: input_password,
        },
        success: function (res) {
            if (res['status'] == 0) {
                window.location.href = "/usercenter/register/success/";
            }
            else {
                showMessage(res['msg']);
            }
        }
    });
}

function showMessage(msg) {
    $("#div-fail-alert").html('<div class="alert alert-danger"><a class="close" data-dismiss="alert" href="#">×</a>' + msg + '</div>');
}
