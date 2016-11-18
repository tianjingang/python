<?php 
include "Compute.class.php";

$num1=$_POST['num1'];
//echo $num1;die;
$num2=$_POST['num2'];
$compute=$_POST['compute'];
$qq=new Compute();
$bb = $qq->jisuan($compute, $num1, $num2);
echo $bb;


?>