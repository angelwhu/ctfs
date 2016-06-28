<?php
/**
 * Created by PhpStorm.
 * User: phithon
 * Date: 16/6/8
 * Time: 上午12:24
 */

 session_start();

class SafeBox {

    private function _read_file($filename)
    {
        $filename = dirname(__FILE__) . "/" . $filename;
        return file($filename);
    }

    public function read()
    {
        $filename = isset($_POST['filename']) ? $_POST['filename'] : "box.txt";
        return $this->_read_file($filename);
    }

    public function view()
    {
        $lines = $this->_read_file('box.txt');
        $i = isset($_POST['i']) ? intval($_POST['i']) : 0;
        return isset($lines[$i]) ? $lines[$i] : "None";
    }

    public function alist()
    {
        $lines = $this->_read_file('box.txt');
        return $lines;
    }

    public function random()
    {
        $lines = $this->_read_file('box.txt');
        return $lines[array_rand($lines)];
    }
}

function _fd_init()
{
    //定义role必须为guest
    $_SESSION["userinfo"] = [
        "role" => "guest"
    ];
    $cookie = isset($_COOKIE['userinfo']) ? base64_decode($_COOKIE['userinfo']) : "";
    if(empty($cookie) || strlen($cookie) < 32) {
        return false;
    }

    $h1 = substr($cookie, 0, 32);
    $h2 = substr($cookie, 32);
    if($h1 !== hash_hmac("md5", $h2, $_SESSION['SECRET_KEY'])) {
        return false;
    }

    //防止身份伪造
    if(strpos($h2, "admin") !== false || strpos($h2, "user") !== false) {
        return false;
    }
    $s = json_decode($h2, true);
    $s['role'] = strval($s['role']);
    if($s['role'] == 'admin') {
        return false;
    }
    $_SESSION["userinfo"] = array_merge($_SESSION["userinfo"], $s);
    return true;
}

function fd_show_source()
{
    return file_get_contents(__FILE__);
}

function fd_config()
{
    return include_once __DIR__ . "/config.php";
}

function fd_error($msg)
{
    return "Error: {$msg}";
}

function fg_safebox()
{
    _fd_init();
    $config = fd_config();
    $action = isset($_POST['method']) ? $_POST['method'] : "";
    $role = isset($_SESSION["userinfo"]['role']) ? $_SESSION["userinfo"]['role'] : "";
    if(!in_array($role, ['admin', 'user'])) {
        return fd_error('Permission denied!!');
    }
    if(in_array($action, $config['role']['admin']) && $role != "admin") {
        return fd_error('Admin permission denied!!');
    }
    $box = new SafeBox();
    if(method_exists($box, $action)) {
        return call_user_func([$box, $action]);
    } else {
        return null;
    }
}