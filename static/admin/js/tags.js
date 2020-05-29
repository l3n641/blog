$(function () {
    new Vue({
        el: "#app",
        delimiters: ['[[', ']]'],
        data: {
            tags: []
        },
        computed: {},
        beforeCreate() {
            var that = this
            this.$nextTick(function () {

                zlajax.get(
                    {
                        'url': '/admin/tag',
                        traditional: true,

                        'success': function (data) {
                            that.tags = data.tags
                        }
                    }
                )
            })
        },
        methods: {
            Addtag: function () {
                var tagname = $("input[name='tagname']").val();
                if (tagname.length === 0) {
                    swal('请输入标签名！');
                    return
                }

                for (key in this.tags) {
                    if (tagname == this.tags[key].name) {
                        swal('标签已存在,无需重复添加', '', 'error')
                        return;
                    }
                }
                var that = this

                zlajax.post({
                    'url': '/admin/tag',
                    traditional: true,
                    'data': {
                        'tag': tagname
                    },
                    'success': function (data) {
                        that.tags.push(data['data'])

                    }
                })
            },
            get_tag: function () {
                zlajax.get(
                    {
                        'url': '/admin/tag',
                        traditional: true,

                        'success': function (data) {
                            this.tags = data.tags
                        }
                    }
                )
            }
        }
    })
})