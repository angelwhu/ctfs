<?php

include 'header.php';

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
	die("connect error~~~: " . $conn->connect_error);
}
if(empty($_GET['r']))
{
	echo "error~";
	exit(-1);
}
$readlink = $_GET['r'];

$stmt = $conn->prepare("select * from message where readlink=?");
//var_dump($stmt);
$stmt->bind_param("s", $readlink);
$stmt->execute();
$stmt->store_result();
$stmt->bind_result($id, $content, $createtime,$flag,$readlink);
while ($stmt->fetch()) {
	//printf ("%s, %s, %s, %s, %s <br />", $id, $content, $createtime,$flag,$readlink);
	printf ("%s", $content);
}
$stmt->close();


$stmt = $conn->prepare("update message set flag=1 where readlink=?");
$stmt->bind_param("s", $readlink);
$stmt->execute();
$stmt->close();

$conn->close();
?>
