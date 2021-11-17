$(window).bind("hashchange", function() {
    // 有些浏览器不返回#，这里统一去掉#
    var hash = window.location.hash.replace('#', '');
    var url = null;
    // 根据hash值得不同，选择对应的页面URL
    if (hash === 'app') {
        url = app_page_url
    } else {
        url = intro_page_url
    }
    // 向对应的页面URL发送get请求，服务器端会返回对应的局部模块
    $.ajax({
        type: 'GET',
        url: url,
        success: function(data) {
            $('#main').hide().html(data).fadeIn(800); // 插入子页面
            activeM(); // 激活新插入的页面中的Materialize组件
        }
    });
});

if (window.location.hash === '') {
    window.location.hash = '#intro';
} else {
    $(window).trigger("hashchange"); // 触发hashchange事件
}