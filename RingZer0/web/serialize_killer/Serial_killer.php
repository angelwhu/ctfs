<?php
class RandomClass 
{ 
	private static $instance;
	private $uStruct;
	public function __construct() 
	{ 
		$this->uStruct = (object)array();
	} 
	public static function GetInstance() 
	{ 
		if(!isset(self::$instance))
		{ 
			self::$instance = new self();
		} 
		return self::$instance; 
	} 
	public function __set($key, $value) 
	{ 
		$this->uStruct->$key = $value; 
	} 
	public function __get($key) 
	{ 
		return $this->uStruct->$key; 
	} 
	public function DoAction() 
	{ 
		$action = $this->uStruct->action;
		$this->$action(); 
	} 
	public function GetCurrentDate() 
	{ 
		GetCurrentDate($this->uStruct); 
	} 
	public function ShowFlag() 
	{ 
		if($this->uStruct->time !== null && $this->uStruct->flag == 'Please?') 
		{ 
			ShowFlag($this->uStruct); 
		} 
	} 
	public function GetOutput() 
	{ 
		return $this->uStruct->output; 
	} 
}
?>
