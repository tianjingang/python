<?php 
/*
 * 一个小球从高度100米落下，每次落地后反跳回原高度的一半，再落下。请写程序，输出第n次落地时，小球落下弹起共多少米。
 */
$num = 7; //总落地次数
$len = 100.0; //小球原始高度
$sum = 100; //小球落地总长
$height = 0; //每次弹起高度

for($i=0;$i<$num;$i++){
    if($num == 0){
        $sum = 100;
    }else{
        $len = $len/2;
        $height = $len;
        $sum = $sum+$height*2;
    }
}
print_r($sum);


?>