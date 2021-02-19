Ajax，全称为 Asynchronous JavaScript and XML，即异步的 JavaScript 和 XML。它利用 JavaScript 在保证页面不被刷新、页面链接不改变的情况下与服务器交换数据并更新部分网页。

发送 Ajax 请求到网页更新的这个过程可以简单分为三步
1. 发送请求
    
    这是由 JavaScript 实现的，实际执行了如下代码
    ```javascript
    var xmlhttp;
    if (window.XMLHttpRequest) {
        //code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp = new XMLHttpRequest();
    } else { //code for IE6, IE5
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function() {
        if (xmlhttp.readyState==4 && xmlhttp.status==200) {
            document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
        }
    }
    xmlhttp.open("POST","/ajax/",true);
    xmlhttp.send()
    ```
2. 解析内容

    得到响应之后，`onreadystatechange` 属性就会被触发，此时利用 xmlhttp 的 responseText 属性便可取到响应内容。返回的内容可能是 HTML 也可能是 JSON，接下来只需要用 JavaScript 进一步处理即可。
3. 渲染网页

    在解析完响应内容之后，就可以通过一些操作，比如 DOM 操作，对网页的内容进行更改。

### Ajax 分析方法
打开浏览器开发者工具，在 `Network` 选项下，我们可以发现一个特殊的 Type 类型——xhr，这是一个 Ajax 请求。在 Request Headers 中有一个信息为 `X-Requested-With:XMLHttpRequest`，这就标记了请求是 Ajax 请求。点击 `Preview`，即可看到响应的内容。

使用 Chrome 开发者工具的筛选功能筛选出所有的 Ajax 请求。当我们滑动网页的时候（以微博网页为例）就会有一个个 Ajax 请求出现，根据这个想法，我们便可模拟请求。
