<?php  
    
    $str = "9e9".chr(0)."*SGBM*";
    var_dump(ereg('^[a-zA-Z0-9]+$', $str));
    var_dump(strpos($str, '*SGBM*'));
    var_dump(strlen($str)); 
    var_dump($str > 999999999);
    $url = "//afds.fdadfsa";
    preg_match('/^([a-z\/.]+)$/', $url, $matches); 
    var_dump($matches);
    echo mktime(18,46,14,05,21,2016);//h:m:s month:date:year
?>
