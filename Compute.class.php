<?php

class Compute{

	public function jisuan($compute,$num1,$num2){
          switch ($compute) {
          	case '+':
          		$sum=$num1+$num2;
          		echo $sum;
          		break;
          	case '-':
          		$sum=$num1-$num2;
          		echo $sum;
          		break;
          	case '*':
          		$sum=$num1*$num2;
          		echo $sum;
          		break;
          	case '/':
          		$sum=$num1/$num2;
          		echo $sum;
          		break;		
          	default:
          		echo "失败";
          }
          
	}
}
?>
