<?php
/*
	$time = time();
	srand($time);
	$token = rand(1000000000000000,9999999999999999);
	echo $time.'<br/>';
	echo $token.'<br/>';

	srand(1429079211);
	$token = rand(1000000000000000,9999999999999999);
	echo $token.'<br/>';
	
	$date = date('Y-m-d H:i:s',"1285724523");
	echo $date.'<br/>';

	$time = mktime(2,59,13,4,15,2015) + 400;
	echo $time.'<br/>';
*/	
	srand($argv[1]);
	$token = rand(1000000000000000,9999999999999999);
	echo $token;
/*
if(URL_HANDLE::GetInstance()->get->k != null) {
	$result = reset($hSql->FastQuery('SELECT * FROM chal_113 WHERE ip_addr = ? AND recovery_key = ? ', array($_SERVER['REMOTE_ADDR'], URL_HANDLE::GetInstance()->get->k)));
	if($hSql->RowCount() != 0) {
		if($result->expired_time > time()) {
			$success = '<div class="success">Here\'s your new password: XXXXXXXXXXXXXX</div>';
		} 
		else {
			$success = '<div class="error">Expired recovery key!</div>';
		}
	} 
	else {
		$success = '<div class="error">Invalid recovery key!</div>';
	}
}*/
?>
