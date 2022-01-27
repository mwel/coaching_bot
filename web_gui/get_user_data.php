<?php

    // Make a database connection so that we can fetch data from a database.
    $conn = mysqli_connect("localhost", "root", "", "company"); // ... figure out here, how to use them. Syntax?
    
    // If error during connection, display error and exit. Else continue.
    if ($conn->connect_error) {
        die(">>>>> Connection failed: " . $conn->connect_error);
    }
    
    // SQL query to select data from a database.
    $sql = "SELECT * FROM user_data";
    // Execute SELECT query and store the result in $result
    $result = $conn->query($sql);
    
    // If $result contains more than 0 rows then display data in HTML table
    if ($result->num_rows > 0) {
        // output data of each row
        while($row = $result->fetch_assoc()) {
        echo "<tr><td>" . $row["id"]. "</td><td>" . $row["username"] . "</td><td>"
        . $row["password"]. "</td></tr>";
    }
    
    echo "</table>";
    } 
    // If $result contains 0 rows print “No results.” and close connection.
    else { echo "0 results"; }
    
    $conn->close();
?>