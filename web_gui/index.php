<table border="1" cellspacing="5" cellpadding="5" width="100%">
	<thead>
		<tr>
			<th>user_ID</th>
            <th>Time Stamp</th>
			<th>First Name</th>
			<th>Last Name</th>
			<th>Gender</th>
			<th>Photo</th>
			<th>Birthdate</th>
			<th>Email</th>
			<th>Phone</th>
			<th>Longitude</th>
			<th>Latitude</th>
			<th>Biography</th>
			<th>State</th>
			<th>Mail Status</th>
			<th>Appointment</th>
		</tr>
	</thead>
	<tbody>
	<?php
		require_once('connection.php');
		$result = $conn->prepare("SELECT * FROM users ORDER BY user_id ASC");
		$result->execute();
		for($i=0; $row = $result->fetch(); $i++){
	?>
		<tr>
			<td><label><?php echo $row['user_id']; ?></label></td>
			<td><label><?php echo $row['time_stamp']; ?></label></td>
			<td><label><?php echo $row['first_name']; ?></label></td>
			<td><label><?php echo $row['last_name']; ?></label></td>
			<td><label><?php echo $row['gender']; ?></label></td>
			<td><label><?php echo $row['photo']; ?></label></td>
			<td><label><?php echo $row['birthdate']; ?></label></td>
			<td><label><?php echo $row['email']; ?></label></td>
			<td><label><?php echo $row['telephone']; ?></label></td>
			<td><label><?php echo $row['longitude']; ?></label></td>
			<td><label><?php echo $row['latitude']; ?></label></td>
			<td><label><?php echo $row['bio']; ?></label></td>
			<td><label><?php echo $row['state']; ?></label></td>
            <td><label><?php echo $row['mail_sent']; ?></label></td>
            <td><label><?php echo $row['Appointment']; ?></label></td>
        </tr>
		<?php } ?>
	</tbody>
</table>