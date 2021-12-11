// INFO: This file is parked here for later use, if module is developed.

<?php

    // Grab a Form data and store it in  $username and $password .
    $username = filter_input(INPUT_POST, 'username');
    $password = filter_input(INPUT_POST, 'password');

    // Check, whether this username and password are empty or not. If they are not empty then we can continue a process.
    if (!empty($username)){
    if (!empty($password)){

    // Establish DB connection
    $host = "localhost";
    $dbusername = "root";
    $dbpassword = "";
    $dbname = "youtube";
    // Create the actual connection
    $conn = new mysqli ($host, $dbusername, $dbpassword, $dbname);

    // Check for error while connecting. If yes, show error message and exit. Else continue.
    if (mysqli_connect_error()){
    die('Connect Error ('. mysqli_connect_errno() .') '
    . mysqli_connect_error());
    }
    else{
    // SQL query, to insert data into a database table.    
    $sql = "INSERT INTO account (username, password)
    values ('$username','$password')";
    // If insert query is executed, print “New record is inserted successfully”
    if ($conn->query($sql)){
    echo "New record is inserted sucessfully";
    }
    else{
        // If query fails, show error message.
    echo "Error: ". $sql ."
    ". $conn->error;
    }
    // Close the database connection.
    $conn->close();
    }
    }
    else{
    echo "Password should not be empty";
    die();
    }
    }
    else{
    echo "Username should not be empty";
    die();
    }
?>