<?php
/*
$error = null;
$success = null;

if(isset($_GET['u']) && isset($_GET['p'])) {
        $link = mysql_connect('127.0.0.1', 'root', 'XyEN85vx7ZK2MmZ');
        $username = str_replace(' ', '', urldecode($_GET['u'])); // bug fix
        mysql_select_db('login', $link);
        $result = mysql_query('SELECT * FROM users WHERE username = (\'' . $username . '\')');

        if(mysql_num_rows($result) == 0) {
                $error =  'Invalid username cannot find hot mom.';
        } else {
                while(($row = mysql_fetch_assoc($result))) {
                        $key = GetKey('/askldjlkeasulawe/key.private');
                        openssl_private_decrypt(base64_decode($row['password']), $output, openssl_get_privatekey($key));

                        if(trim($output) == $_GET['p']) {
                                $success = true;
                        } else {
                                $error = 'Invalid password cannot find hot mom.';
                        }
                }
        }
}

function GetKey($path) {
        $fd = fopen($path,"r");
        $output = fread($fd, 8192);
        fclose($fd);
        return $output;
}
*/
$key = '-----BEGIN RSA PRIVATE KEY-----
MIICWwIBAAKBgQC1CL8cDO5zDlQnww5n378N4Azh0ilEmCEZy1upB6sZykWOxyjG
BmojDYe/LWtqmar9Rx4kSeYs16r334Xu7w9OOupFck0otGdFRM3+kCAj839fKTZS
5b6aAGySPSROeJNxvlrFbLFWbBc1DyZxhofBLitirgUdKEoXbzmeZvAz4QIDAQAB
AoGAeIipTdDiVqLcr1i0175mo6NgkF5wcaZkq5r1nXZompRNecHqyOZudoZEsqpY
EbLc4SQf0oONiJ/TypP9xddPtWP7ef/FJoa29FLXDCpFmZeO6N8sYBgqOj57MzUB
UDdFFcBpfYwC+CN7mgN8bMyusVyjktI41Zccu5qSOsKzAJECQQDpDjVm+FMVUdKl
E81r92/90XnE5xkqL+sO/lHWtqKp4b4lcyrAYIf7Uh2tKGLET7ezqcMshI6l3xMu
EdaNiEV9AkEAxttsXRLFoRHf5q3HFZZNaX5rQtlw6b7EAz1k7olI+5Xkfpup9wzo
kZ0xn+uZTz/McZnQtNtS5Y3eDDzFMqXlNQJATgYwwMGAZ1HWeOfRTUUw3EQmRVKt
bR9Pzdw9H+pTORbXpwgQlwl6XRyXzOIJdvnNYbwDGMNkUooFjNXyA75MrQJAdYIe
Q9We8TJF0+OmvEvoDMnGimdBgO7Yl22FIiv/86M8tdA4nKOFHt77/xtSqfDyV8Lk
AKuGDd5Kc4LJqMc9bQJAZBtVs2DDiJFvPiNhkP2l7LD064x806IaUXeZaYCsSuNM
eZ0EFbn41y7L2oHJlaFrosHMv/gArr4EinLbuNYoLg==
-----END RSA PRIVATE KEY-----';
$password = 'aWzode4/Rbdd51trYTrWPFG/nq5yOPZg+A7Jh+OdMlKuCwJW7F+hByRisBsjTzeB67WGTyifOJwUEAo16FarJkYMDJh4TbG5wvIvg3ZWx89gbbVCnF7jN71KgPVtV+t5rcN9iLbz6QDy3UVsjnjq0uk57mMC2ANjNMl5QkCatfE=';

openssl_private_decrypt(base64_decode($password), $output, openssl_get_privatekey($key));

echo $output."\n";

?>