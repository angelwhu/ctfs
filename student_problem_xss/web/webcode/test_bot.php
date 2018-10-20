<?php  
if($_SERVER['REMOTE_ADDR'] !== "172.17.0.1" && $_SERVER['REMOTE_ADDR'] !== "123.207.24.193" )
{
    echo "You do not have permission\n";
    exit(-1);
}
echo "success\n";
?>
<link rel="prefetch" href="http://121.42.175.111:2333/">
<!-- <script src="http://121.42.175.111:8089/myjs/my_xss.js"></script> -->

