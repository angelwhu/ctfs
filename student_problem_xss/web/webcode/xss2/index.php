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
			<h1 class="text-center">软件安全实验课题目------有点复杂的XSS</h1>
		</div>
		
		<div class="row alert alert-info">
			<p class="lead">提示：1. 环境要求最新的chrome浏览器</p>
			<p class="lead">2. Referer很重要~~</p>
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
<script src="./js/mycode.js"></script>

</html>
