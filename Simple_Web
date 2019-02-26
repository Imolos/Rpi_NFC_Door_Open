<?php
	//Connection to MySQL  
$mysqli =new mysqli("127.0.0.1","user","password","database");
	
	//Connection Testing
    if ($mysqli->connect_errno) {
        echo "Connect failed: ".$mysqli->connect_error."\n";
        exit();
    }
//else {echo "Connected";}
//Preparing Query
    $sql = "SELECT * FROM list";
$result = $mysqli->query($sql);

if ($result->num_rows > 0) {
    echo "<table><tr><th><Column1></th><Column2></th><th><Column3></th></tr>";
    //Data comes out
    while($row = $result->fetch_assoc()) {
        echo "<tr><td>" . $row["<Column1>"]."". "</td><td>" . $row["<Column2>"]. "</td><td>" . $row["<Column3>"]. "</td></tr>";
    }
    echo "</table>";
} else {
    echo "0 results";
}

$mysqli->close();

?>
