<?php

if($_SERVER['REMOTE_ADDR'] !== "172.17.0.1" && $_SERVER['REMOTE_ADDR'] !== "123.207.24.193" )
{
    echo "You do not have permission\n";
    exit(-1);
}

include 'header.php';

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
	die("connect error~~~´¥: " . $conn->connect_error);
}

$stmt = $conn->prepare("select * from message where flag=0 limit 1");
//var_dump($stmt);

$stmt->execute();
$stmt->store_result();
$stmt->bind_result($id, $content, $createtime,$flag);

while ($stmt->fetch()) {
	printf ("%s, %s, %s, %s <br />", $id, $content, $createtime,$flag);    
}
$stmt->close();

$stmt = $conn->prepare("update message set flag=1 where id=?");
$stmt->bind_param("i", $id);
$stmt->execute();
$stmt->close();

$conn->close();
?>
