$(function () {
    $("#submit").click(function (event) {
        event.preventDefault();
        var oldpwd_input = $("input[name='oldpwd']");
        var newpwd_input = $("input[name='newpwd']");
        var newpwd2_input = $("input[name='newpwd2']");
        var oldpwd = oldpwd_input.val();
        var newpwd = newpwd_input.val();
        var newpwd2 = newpwd2_input.val();
        var csrf_token = $("input[name='csrf_token']").val();
        zlajax.post({
            'url': '/admin/repassword',
            'data': {
                'oldpwd': oldpwd,
                'newpwd': newpwd,
                'newpwd2': newpwd2,
                'csrf_token': csrf_token
            },
            'success': function (data) {
                if (data['code'] == 200) {
                    zlalert.alertSuccessToast('恭喜，密码修改成功');
                    oldpwd_input.val("")
                    newpwd_input.val("")
                    newpwd2_input.val("")
                } else {
                    zlalert.alertInfoToast(data['message'])
                }
            }
        })
    })
})