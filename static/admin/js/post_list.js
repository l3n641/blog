$(function () {

    $("#vue").css('display', 'none');
    new Vue({
        el: '#demo',
        delimiters: ['[[', ']]'],
        data: {
            posts: [],
        },
        methods: {
            Search: function () {
                var post_name = $("input[name='post_name']").val();
                var vm = this;
                zlajax.post({
                    'url': '/admin/post_search',
                    async: false,
                    'data': {
                        'title': post_name,
                    },
                    'success': function (data) {
                        if (data['code'] == 200) {
                            $("#jinjia").hide();
                            $("#vue").show();
                            var posts = [];
                            var posts_return = data['data'];
                            for (var i = 0; i < posts_return.length; i++) {
                                var my_title = posts_return[i].title.replace(post_name, '<span style="color: red">' + post_name + '</span>');
                                var my_content = posts_return[i].content.replace(post_name, '<span style="color: red">' + post_name + '</span>');
                                my_title = my_title.substr(0, 50)
                                my_content = my_content.substr(0, 50)
                                posts.push(
                                    {
                                        'title': my_title,
                                        'content': my_content,
                                        'username': posts_return[i].username,
                                        'email': posts_return[i].email,
                                        'create_time': posts_return[i].create_time,
                                        'post_id': posts_return[i].id,
                                        'user_id': posts_return[i].author_id
                                    }
                                )
                            }
                            vm.posts = posts;
                        } else {
                            swal('帖子不存在');
                        }
                    }
                })
            },

            delpost: function (e) {
                var post_id = e.target.attributes.post_id.nodeValue;
                var current = e.target
                var par = $(current).parent().parent();
                var that = this;
                zlalert.alertConfirm({
                    "cancelText": "取消",
                    "confirmText": "确定",
                    "msg": "确定要删除帖子？",
                    "confirmCallback": function () {
                        zlajax.post({
                            'url': '/admin/post_list',
                            'data': {
                                'id': post_id
                            },
                            'success': function (data) {
                                swal('删除成功');
                                par.empty();

                            }
                        })
                    }
                })
            }
        }
    })
})


$(function () {
    var open = 0;
    $("#checkAll").click(function () {
        if (open === 0) {
            $("input[type='checkbox']").attr('checked', true);
            open = 1
        } else {
            $("input[type='checkbox']").attr("checked", false);
            open = 0
        }
        // $("input[type='checkbox']").prop("checked",$(this).prop("checked"));
    })


    $("#group-del").click(function () {
        var post_ids = [];
        var comments_ches = $('input:checkbox:checked')
        if (comments_ches.length === 0) {
            swal('请勾选需要删除的帖子')
            return;
        }
        for (var i = 0; i < comments_ches.length; i++) {
            var cro = comments_ches[i].getAttribute('data-post-id');
            post_ids.push(cro)
            var par = comments_ches[i].parentNode.parentNode
        }
        zlalert.alertConfirm({
            "cancelText": "取消",
            "confirmText": "确定",
            "msg": "确定要删除帖子吗？",
            "confirmCallback": function () {
                zlajax.post({
                    'url': '/admin/post_list',
                    traditional: true,
                    'data': {
                        'id': post_ids,
                    },
                    'success': function (data) {
                        swal('删除成功')
                        for (var i = 0; i < comments_ches.length; i++) {
                            var cro = comments_ches[i].getAttribute('data-post-id');
                            var par = comments_ches[i].parentNode.parentNode
                            par.remove();
                        }
                    }
                })
            }
        })
    })
})


$(function () {
    //删除单个帖子
    $(".del-btn").click(function () {
        var post_id = $(this).attr('data-id');
        console.log(post_id);
        zlalert.alertConfirm({
            "cancelText": "取消",
            "confirmText": "确定",
            "msg": "确定要删除帖子？",
            "confirmCallback": function () {
                zlajax.post({
                    'url': '/admin/post_list',
                    'data': {
                        'id': post_id
                    },
                    'success': function (data) {
                        swal('删除成功');
                        setTimeout(function () {
                            window.location.reload()
                        }, 500)

                    }
                })
            }
        })
    })
})