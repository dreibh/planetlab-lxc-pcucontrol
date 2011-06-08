<?php 

$DEBUG=FALSE;
function logit($string){
    global $DEBUG;
    if ( $DEBUG )
    {
		$f = fopen("output.log", 'a');
		fwrite($f, $string);
		fclose($f);
    }
}

function run_hp_script($script, $host, $username, $password)
{
	$cmd = "hpilo/locfg.pl -s $host -f $script -u $username -p '$password' 2>&1"; 
	logit("cmd: " . $cmd);
	return system($cmd);

		$f = fopen("output.log", 'a');
		fwrite($f, print_r($_REQUEST, TRUE));
		fclose($f);

}

	if ( isset($_REQUEST['hostname']) && 
		 isset($_REQUEST['username']) && 
		 isset($_REQUEST['password']) &&
		 isset($_REQUEST['model']) )
	{
		$host=$_REQUEST['hostname'];
		$username=$_REQUEST['username'];
		$password=$_REQUEST['password'];
		$model=$_REQUEST['model'];
		if ( isset($_REQUEST['dryrun']) ) 
		{
			$dryrun = $_REQUEST['dryrun'];
			settype($dryrun, "boolean");
		} else {
			$dryrun = TRUE;
		}

		logit(print_r($_REQUEST, TRUE));

		if (strcmp($model,"HPiLOProxy") == 0) {
			if ( $dryrun ) 
			{
				run_hp_script("hpilo/iloxml/Get_Network.xml", $host, $username, $password);
			} else {
				run_hp_script("hpilo/iloxml/PowerOn_Server.xml", $host, $username, $password);
				echo run_hp_script("hpilo/iloxml/Reset_Server.xml", $host, $username, $password);
			}
		} elseif ( strcmp($model,"OpenIPMIProxy") == 0 )
		{
			# cmd = "ipmitool -I lanplus -H $host -U $username -P '$password' user list"
			# cmd = "ipmitool -I lanplus -H $host -U $username -P '$password' power cycle"
			echo system("which ipmitool 2>&1");
		} else 
		{
			echo "Unrecognized pcu type: $model";
		}

	} else {
		echo "Please provide hostname, username, and password";
	}

?>
