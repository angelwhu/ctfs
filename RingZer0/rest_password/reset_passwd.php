
if(isset($_POST['reset_username'])) {
		srand(time());
		$token =
		rand(1000000000000000,9999999999999999);
				
		$success = '<div class="success">Reset password link has been sent to admin@youdontownthisemail.com. Please follow the link ...
		$hSql->FastQuery('DELETE FROM chal_113 WHERE ip_addr = ?', array($_SERVER['REMOTE_ADDR']));
		$hSql->FastQuery('insert into chal_113 values (?,?,?)', array($_SERVER['REMOTE_ADDR'], $token, time() + 3600));
}

if(URL_HANDLE::GetInstance()->get->k != null) {
		$result = reset($hSql->FastQuery('SELECT * FROM chal_113 WHERE ip_addr = ? AND recovery_key = ? ', array($_SERVER['REMOTE_ADDR'], URL_HANDLE::GetInstance()->get->k)));
		if($hSql->RowCount() != 0) {
				if($result->expired_time > time()) {
						$success = '<div class="success">Here\'s your new password: XXXXXXXXXXXXXX</div>';
				} else {
						$success = '<div class="error">Expired recovery key!</div>';
				}
		} else {
				$success = '<div class="error">Invalid recovery key!</div>';
		}
}
