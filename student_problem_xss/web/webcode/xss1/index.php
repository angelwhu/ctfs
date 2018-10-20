<?php
include 'header.php';
?>
<!DOCTYPE html>
<html lang="zh-CN">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<link href="./css/bootstrap.min.css" rel="stylesheet">
	<title>XSS留言板</title>
</head>
<body>

	<div class="container">
		<div class="row">
			<h1 class="text-center">软件安全实验课题目------XSS留言板</h1>
		</div>
		
		<div class="row alert alert-info">
			<p class="lead">提示：1. 目的是获取管理员的Cookie。</p>
			<p class="lead">2. 先使用测试页面(<a href="./test.php" target="_blank">test.php</a>)构造好Payload后，再使用本页面发送。</p>
		</div>
		
		<div class="row">
			<form action="postmessage.php" method="post">
			  <div class="form-group">
			    <label for="message">消息内容：</label>
				<textarea class="form-control" rows="6" name="message" id="message"></textarea>	    
			  </div>
			  
			  <div class="form-group">
			    
				<div id="embed-captcha"></div>
				<div id="wait" class="show alert alert-danger">正在加载验证码......</div>
				<div id="notice_validate" class="alert alert-danger">请先完成验证</div>	 
				
			  </div>
			  
			  <button type="submit" id="embed-submit" class="btn btn-success">发送消息给管理员</button>
			  <button type="button" class="btn btn-danger" id="testButton">本地测试页面</button>
			</form>
		
		</div>
	</div>

</body>

<script src="./js/jquery-3.2.1.min.js"></script>
<script src="./js/bootstrap.min.js"></script>
<script src="./js/gt.js"></script>

<script type="text/javascript">

$("#testButton").click(function(){
	window.open("./test.php"); 
});

</script>

<script>
	$("#notice_validate").hide();
    var handlerEmbed = function (captchaObj) {
        $("#embed-submit").click(function (e) {
            var validate = captchaObj.getValidate();
            if (!validate) {
                $("#notice_validate").show(500);
                setTimeout(function () {
                    $("#notice_validate").hide(500);
                }, 3000);
                e.preventDefault();
            }
        });
        // 将验证码加到id为captcha的元素里，同时会有三个input的值：geetest_challenge, geetest_validate, geetest_seccode
        captchaObj.appendTo("#embed-captcha");
        captchaObj.onReady(function () {
            $("#wait")[0].className = "hide";
        });
        // 更多接口参考：http://www.geetest.com/install/sections/idx-client-sdk.html
    };
    $.ajax({
        // 获取id，challenge，success（是否启用failback）
        url: "./gt3-php-sdk-master/web/StartCaptchaServlet.php?t=" + (new Date()).getTime(), // 加随机数防止缓存
        type: "get",
        dataType: "json",
        success: function (data) {
            console.log(data);
            // 使用initGeetest接口
            // 参数1：配置参数
            // 参数2：回调，回调的第一个参数验证码对象，之后可以使用它做appendTo之类的事件
            initGeetest({
                gt: data.gt,
                challenge: data.challenge,
                new_captcha: data.new_captcha,
                product: "embed", // 产品形式，包括：float，embed，popup。注意只对PC版验证码有效
                offline: !data.success // 表示用户后台检测极验服务器是否宕机，一般不需要关注
                // 更多配置参数请参见：http://www.geetest.com/install/sections/idx-client-sdk.html#config
            }, handlerEmbed);
        }
    });
</script>

</html>
