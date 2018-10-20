<?php

include 'header.php';

if(!empty($_POST['message']))
{
	$message = $_POST['message'];
	
	echo filter($message);
	exit(0);
}

?>

<!DOCTYPE html>
<html lang="zh-CN">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<link href="./css/bootstrap.min.css" rel="stylesheet">
	<title>本地测试</title>
</head>
<body>

<div class="container">
<div class="row">
	<h1 class="text-center">本地测试页面</h1>
</div>

<div class="row">
	<form action="test.php" method="post">
	  <div class="form-group">
	    <label for="message">留言内容：</label>
		<textarea class="form-control" rows="6" name="message" id="message"></textarea>	    
	  </div>
	  <button type="submit" class="btn btn-default">测试</button>
	</form>

</div>
</div>

</body>
</html>
