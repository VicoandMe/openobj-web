/**
 * Created by yoyo on 16/3/21.
 */
// get cookie
var getCookie = function (key) {
    var _cookie = document.cookie;
    if (!_cookie) {
        return null;
    }
    if (!key) {
        return _cookie;
    }
    var exp = new RegExp(key + '\=([^\;]+)');
    var result = _cookie.match(exp);
    if (result && result.length > 1) {
        return result[1];
    } else {
        return null;
    }
};

// ajax setup
$.ajaxSetup({
    cache: false,
    beforeSend: function (xhr, o) {
        if (o && o.type.toLowerCase() == 'post') {
            var csrfToken = getCookie('csrftoken') || '';
            xhr.setRequestHeader("X-CSRFToken", csrfToken);
        }
    }
});

function GetQueryString(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
    var r = window.location.search.substr(1).match(reg);
    if (r != null) return (r[2]); return null;
};