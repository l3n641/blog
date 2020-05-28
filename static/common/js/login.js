$(function () {
    $("#submit-btn").click(function (event) {
        event.preventDefault();
        var email = $("input[name='email']").val();
        var password = $("input[name='password']").val();
        var csrf_token = $("input[name='csrf_token']").val();
        console.log(email, password);
        zlajax.post({
            'url': '/admin/login',
            'data': {
                'email': email,
                'password': password,
                'csrf_token': csrf_token
            },
            'success': function (data) {
                if (data['code'] == 200) {
                    window.location.href = '/admin/index/';
                    console.log('登录成功！')
                } else {
                    zlalert.alertInfoToast(data['message'])
                }
            }
        })
    })

})