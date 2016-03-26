/**
 * Created by yoyo on 16/3/20.
 */

$(function () {
    //todo 已登录转到首页

    $("#loginForm").validate({
        rules: {
            email: {
                required: true,
                email: true
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
            password: {
                required: "请输入密码",
                rangelength: "密码为6-20个字符"
            }
        },
        errorElement: "em",
        errorPlacement: function (error, element) {
            error.addClass("valid-msg");
            error.insertAfter(element.parents(".input-group"));
        },
        highlight: function (element, errorClass, validClass) {
            $(element).parents(".input-group").addClass("has-error").removeClass("has-success");
        },
        unhighlight: function (element, errorClass, validClass) {
            $(element).parents(".input-group").addClass("has-success").removeClass("has-error");
        }
    });

    document.onkeydown = function (e) {
        if (e.keyCode == 13)
            login();
    };

});

function showMessage(msg) {
    $("#div-fail-alert").html('<div class="alert alert-danger"><a class="close" data-dismiss="alert" href="#">×</a>' + msg + '</div>');
}

function login() {
    if (!$("#loginForm").valid()) {
        return;
    }

    var input_email = $("#login-username").val();
    var input_password = $("#login-password").val();
    $.ajax({
        type: "POST",
        url: "/usercenter/login/",
        data: {
            email: input_email,
            password: input_password,
        },
        success: function (res) {
            if (res['status'] == 0) {
                var url = GetQueryString("refer");
                if (url == null || url == "")
                    url = "/";
                window.location.href = url;
            }
            else {
                showMessage(res['msg']);
                $(".input-group").removeClass("has-success");
            }
        }
    });
}


