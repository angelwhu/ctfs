<?php
header("Content-Security-Policy: default-src 'self' *.geetest.com; script-src 'self' *.geetest.com;img-src 'self' data: *.geetest.com;");

header("Content-type: text/html; charset=utf-8");

$servername = "mysql_db";
$username = "root";
$password = "root";
$dbname = "xss2";
//$servername = "localhost";
//$username = "root";
//$password = "";
//$dbname = "xss2";
function filter($in)
{
    $out = str_replace("script","",$in);
    $out = str_replace("svg","",$out);
    $out = str_replace("img","",$out);
    return $out;
}
