<?php 

/*
 * 正三角形
 */
for($i=0;$i<=3;$i++)
{
    for($j=0;$j<=3-$i;$j++){
        echo '&nbsp';
    }
    for($k=0;$k<=2*$i;$k++)
    {
        echo '*';
    }
echo '<br>';
}


?>