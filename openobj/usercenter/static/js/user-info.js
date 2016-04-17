/**
 * Created by Administrator on 2016/4/17.
 */

function showMessage(msg) {
    html = "<div id='alert-cgpwd' class='alert'> <a class='close' data-dismiss='alert' href='#'>×</a>" + msg + "</div>";
    $("#div-fail-alert").html(html);
}
$(document).ready(function(){
    $("#user_sex").find('input[type=checkbox]').bind('click', function(){
        $('#user_sex').find('input[type=checkbox]').not(this).attr("checked", false);
    });
    function getValue(){
        var value = '';
        var checked = $('input[type="checkbox"]:checked');
        value = checked.val();
        return value;
    }
    $("#inputAlias").focus(function(){
        if($("#inputAlias").val().length == 0){
            $("#nicknameTip").show();
        }
    });
    $("#inputAlias").blur(function(){
       	 $("#nicknameTip").hide();
    });
    $("#inputBirthday").focus(function(){
        if($("#inputBirthday").val().length == 0) {
            $("#birthdayTip").show();
        }
    });
     $("#inputBirthday").blur(function(){
       	 $("#birthdayTip").hide();
    });
    function save_userinfo(){
        var nick_name = $("#inputAlias").val();
        var user_sex = getValue();
        var user_bir = $("#inputBirthday").val();
        $.ajax({
            type: "POST",
            url :"/usercenter/info/",
            data: {
                nick_name :nick_name,
                sex : user_sex,
                birthday: user_bir
            },
            success:function(res){
                if(res['status'] == 0){
                    showMessage(res['msg']);
                    //alert("更新资料成功！");
                }
            }
        });
    }
    $("#btnsaveinfo").click(save_userinfo);
});
