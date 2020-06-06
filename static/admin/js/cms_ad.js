$(function () {

    $("#save-ad-btn").click(function () {
        var img_url = $("input[name='image_url']").val();
        var link_url = $("input[name='link_url']").val();
        if (img_url.length === 0 || link_url.length === 0) {
            swal('请输入完整数据', '', 'error')
            return;
        }
        zlajax.post({
            'url': '/cms/advertisement/',
            'data': {
                'img_url': img_url,
                'link_url': link_url
            },
            'success': function (data) {
                if (data['code'] == 200) {
                    swal('添加成功', '', 'success')
                    window.location.reload()
                } else {
                    swal(data['message'], '', 'error')
                }
            }
        })
    })
})

$(document).on("click", '.ad-edeit', function () {
    var type = $(this).attr('data-type');
    var ad_id = $(this).attr('data-ad-id');
    var par = $(this).parent()
    zlajax.post({
        'url': '/cms/ad_type/',
        'data': {
            'ad_id': ad_id
        },
        'success': function (data) {
            if (data['code'] == 200) {
                if (type === 'using') {
                    par.html('<a class="ui red circular label ad-edeit" data-ad-id="' + ad_id + '" data-type="block">禁用</a>')
                    type = 'block'
                } else {
                    par.html('<a class="ui green circular label ad-edeit" data-ad-id="' + ad_id + '" data-type="using">使用中</a>')
                    type = 'using'
                }
            }
        }
    })
})

$(function () {
    $(".ad-del").click(function () {
        var ad_id = $(this).attr('data-ad-id');
        var par = $(this).parent().parent();
        zlajax.post({
            'url': '/cms/del_ad/',
            'data': {
                'ad_id': ad_id,
            },
            'success': function (data) {
                if (data['code'] == 200) {
                    par.empty();
                } else {
                    swal(data['message'], '', 'error')
                }
            }
        })
    })
})
