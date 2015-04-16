<?php
$mongo = new  MongoClient();
$db = $mongo->mydb; //选择数据库
$coll = $db->test; //选择集合
$lock = $_POST['lock'];
$key  = $_POST['key'];
 
if (is_array($lock)) 
{
	$data = array('lock'=>$lock);

	$data = $coll->find($data);
	if ($data->count()>0) 
	{
		echo 'the lock is right,but wrong key';
	}
	else
	{
		echo 'lock is wrong';               
	}
}
else
{
	if ($lock == '9cc32bd6'&&$key=='9cc32bd6') 
	{               
		echo 'Your flag is xxxxxxx';
	}
	else
	{
		echo 'key or lock is wrong';           
	}
}
?>
