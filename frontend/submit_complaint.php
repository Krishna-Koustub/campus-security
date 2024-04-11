<?php
// Check if the form was submitted using POST method
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve the form data
    $complaintTitle = htmlspecialchars($_POST['complaintTitle']);
    $complaintMessage = htmlspecialchars($_POST['complaintMessage']);
    $complaintCategory = htmlspecialchars($_POST['complaintCategory']);
    $fullName = htmlspecialchars($_POST['fullName']);
    $email = htmlspecialchars($_POST['email']);
    $phoneNumber = htmlspecialchars($_POST['phoneNumber']);

    // Validate required fields
    if (empty($complaintTitle) || empty($complaintMessage) || empty($complaintCategory) || empty($fullName) || empty($email) || empty($phoneNumber)) {
        // Handle empty fields error
        http_response_code(400); // Bad Request
        echo json_encode(array("message" => "All fields are required."));
        exit();
    }

    // In a real application, you would process and store the complaint data in a database or send it to relevant stakeholders
    // For demonstration, let's just log the complaint details
    $timestamp = date("Y-m-d H:i:s");
    $logMessage = "New Complaint Submitted on {$timestamp}:\n";
    $logMessage .= "Title: {$complaintTitle}\n";
    $logMessage .= "Message: {$complaintMessage}\n";
    $logMessage .= "Category: {$complaintCategory}\n";
    $logMessage .= "Submitted By: {$fullName}\n";
    $logMessage .= "Email: {$email}\n";
    $logMessage .= "Phone Number: {$phoneNumber}\n";

    // Append to a log file (for demonstration purposes)
    file_put_contents("complaints.log", $logMessage . "\n", FILE_APPEND);

    // Send a success response back to the client-side JavaScript
    http_response_code(200); // OK
    echo json_encode(array("message" => "Complaint submitted successfully."));
} else {
    // Handle non-POST requests
    http_response_code(405); // Method Not Allowed
    echo json_encode(array("message" => "Method not allowed."));
}
?>
