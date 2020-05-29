

$(function () {
    $("#submit-btn").click(function () {
        var content = CKEDITOR.instances.ckeditor.getData();

        var title = $("input[name='title']").val();
        if (title.length == 0) {
            swal('请输入标题')
            return;
        }
        console.log(content.length)
        if (content.length == 11 | content.length == 4) {
            swal('请输入内容')
            return;
        }
        var tags = []
        $.each($('input:checkbox:checked'), function () {
            tags.push($(this).val())
        });
        if (tags.length > 3) {
            swal('最多添加选3个标签哦~')
            return;
        }
        if (tags.length < 1) {
            swal('至少添加一个标签o ~')
            return;
        }
        zlajax.post({
            'url': '/admin/post',
            traditional: true,
            'data': {
                'content': content,
                'title': title,
                'tags': tags
            },
            'success': function (data) {
                if (data['code'] == 201) {
                    swal('发表成功');
                    setTimeout(function () {
                        window.location.href = '/'
                    })
                } else {
                    swal('发表失败', '', 'error')
                }
            }
        })

    })
})