/*
 * 倒三角
 */
for($i=3;$i>=0;$i--)
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
