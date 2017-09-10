$(document).ready(function() {
    //alert(wp_pagingbarJson);
    if (wp_pagingbarJson) {
        var pagingbar = eval(wp_pagingbarJson)[0];

        var pageSize = pagingbar.pageSize;
        var total = pagingbar.total;
        var pageIndex = pagingbar.pageIndex;
        var pages = pagingbar.pages;
        var currUrl = pagingbar.currURL;
        var firstUrl = pagingbar.firstURL;
        var prevUrl = pagingbar.prevURL;
        var nextUrl = pagingbar.nextURL;
        var lastUrl = pagingbar.lastURL;

        var pagingbarHtml = '';
        pagingbarHtml += (' <ul class="wp_paging clearfix"> ');
        pagingbarHtml += ('   <li class="pages_count"> ');
        pagingbarHtml += ('     <span class="per_page">每页<em class="per_count">' + pageSize + '</em>条记录</span> ');
        pagingbarHtml += ('     <span class="all_count">总共<em class="all_count">' + total + '</em>条记录</span> ');
        pagingbarHtml += ('   </li> ');
        pagingbarHtml += ('   <li class="page_nav"> ');
        pagingbarHtml += ('     <a class="first" href="' + firstUrl + '"><span>首页</span></a> ');
        pagingbarHtml += ('     <a class="prev" href="' + prevUrl + '"  ><span>上一页</span></a> ');
        pagingbarHtml += ('     <a class="next" href="' + nextUrl + '" ><span>下一页</span></a> ');
        pagingbarHtml += ('     <a class="last" href="' + lastUrl + '"><span>尾页</span></a> ');
        pagingbarHtml += ('   </li> ');
        pagingbarHtml += ('   <li class="page_jump"> ');
        pagingbarHtml += ('     <span class="pages">页码：<em class="curr_page" curr_page="' + pageIndex + '">' + pageIndex + '</em>/<em class="all_pages" pageCount="' + pages + '">' + pages + '</em></span> ');
        pagingbarHtml += ('     <span><input class="pageNum" type="text" /><input type="hidden" class="currPageURL" value=""></span></span> ');
        pagingbarHtml += ('     <span><a class="pagingJump" href="javascript:void(0);" onclick="wp_pagingJump(' + pages + ', \'' + currUrl + '\');">跳转</a></span> ');
        pagingbarHtml += ('   </li> ');
        pagingbarHtml += (' </ul> ');

        $("#wp_pagingbar_postion").html(pagingbarHtml);
    }


});

function wp_pagingJump(pages, currUrl) {
    var pageNum = $(".pageNum").val();
    if (pageNum === "") {
        alert("请输入页码！");
        return;
    }
    if (isNaN(pageNum) || pageNum <= 0 || pageNum > pages) {
        alert("请输入正确页码！");
        return;
    }
    var reg = new RegExp("/list", "g");
    window.location.href = currUrl.replace(reg, "/list" + pageNum);
}

