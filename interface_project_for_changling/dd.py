html_data = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="pragma" content="no-cache">
    <meta http-equiv="cache-control" content="no-cache">
    <meta http-equiv="expires" content="0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="renderer" content="webkit">
    <title></title>
    <!--<link rel="Shortcut Icon" href="/favicon.ico">-->
    <link rel="stylesheet" href="/static_ext/menuicon/iconfont.css">
    <script type="text/javascript" src="/static/common/js/jquery-1.11.3.min.js"></script>
    <script type="text/javascript" src="/static/common/js/jquery.xdomainrequest.min.js"></script>
    <script type="text/javascript" src="/static/common/js/jquery-mousewheel.js"></script>
    <script type="text/javascript" src="/static/common/js/config.min.js?97267ef08b7f8a0ca5c039b8abe0501f"></script>
    <script type="text/javascript" src="/static/common/js/style.min.js?51fb4bbd0a92be3ba9232c392438c34c"></script>
    <script type="text/javascript" src="/static/common/js/echarts.min.js"></script>
    <script type="text/javascript" src="/static/common/js/callback.min.js?567901fd5251d68ecd55c8a77115eca9"></script>
    <script type="text/javascript" src="/static/common/js/const.min.js?id=1&ab4cea05060ec30480ed5d10eff69634"></script>
    <script type="text/javascript" src="/static/common/js/services.min.js?d1a286372e12fdb9814ef06925ce56a1"></script>
    <script type="text/javascript" src="/static/common/js/template.min.js?0384d604a00847ca79a6b6f9df9fb73e"></script>
    <script type="text/javascript" src="/static/common/js/data.min.js?9a55ab9e4402d58f8a8711f7192afb8b"></script>
    <script type="text/javascript" src="/static/common/js/ajax_form.js"></script>
    <script type="text/javascript" src="/static/common/js/sha256.js"></script>
    <script type="text/javascript" src="/static/common/js/hdsecurity.js"></script>
    <script type="text/javascript" src="/static/common/js/security.js"></script>
    <script type="text/javascript" src="/static/common/js/formula.min.js?4d308dbf5f31f9e62eadeb96ed3cca3d"></script>

    <script type="text/javascript">window._downloadurl={oldversion:"/static/download/common/browser/49.0.2623.112_Chrome_x86.exe", newversion:"/static/download/common/browser/62.0.3202.94_Chrome_x64.exe"}</script>
    <script type="text/javascript" src="/static/portal/js/style.min.js?77c8df6610da829bc86cf4ea34de76da"></script>
</head>
<body>
<div id="page" template="page"></div>
<script type="text/javascript">
    window.csrf = 'c5ba6c0024e549a48b1c5c06fa970df8';

    var doc = document;
    var heads = doc.getElementsByTagName("head");
    var link = doc.createElement("link");
    link.setAttribute("rel", "Shortcut Icon");
    link.setAttribute("type", "");
    link.setAttribute("type", "image/x-icon");
    if (window.localconfig()) {
        window.homeclass = window.localconfig()["homeclass"];
        var logopng = window.localconfig()["icon"];
        var doctitle = window.localconfig()["title"];
        if (logopng) {
            link.setAttribute("href", logopng);
            if(heads.length) {
                heads[0].appendChild(link);
            } else {
                doc.documentElement.appendChild(link);
            }
        }
        if (doctitle) {
            doc.title = doctitle;
        }
    } else {
        doc.title = "现场总管";
        link.setAttribute("href", "/static/common/imgs/hd_favicon.ico");
        if(heads.length) {
            heads[0].appendChild(link);
        } else {
            doc.documentElement.appendChild(link);
        }
    }


    //    $.template.hash(JSON.stringify({"mc":"sy", "fc":"SY_FORM", "uc":"017000900020"}));
    $.template.layout("/static/common/" + "");
//    page.type("home");
</script>
</body>
</html>
'''
from bs4 import BeautifulSoup
from lxml import etree
#html_data = "window.csrf = 'c5ba6c0024e549a48b1c5c06fa970df8';"
#html_data = 'window'
import re
searchObj = re.search("window.csrf = '(.+?)';", html_data, re.M | re.I)
#searchObj = re.search('wind(.+?)w', html_data, re.M | re.I)

if searchObj:
    print(   "searchObj.group() : ", searchObj.group())
    print(    "searchObj.group(1) : ", searchObj.group(1))
    #print(    "searchObj.group(2) : ", searchObj.group(2))
else:
    print ("Nothing found!!")