<?php
// CLARET website — contact form handler.
// Sends each message from the site's form to Enzo's inbox.

header('Content-Type: application/json; charset=utf-8');

$TO_EMAIL = 'enzo@sowattmedia.com';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['ok' => false, 'error' => 'method']);
    exit;
}

// Spam trap: real visitors never see or fill this field.
if (!empty($_POST['website'])) {
    echo json_encode(['ok' => true]);
    exit;
}

function clean_line($v) {
    $v = trim((string)$v);
    return str_replace(["\r", "\n"], ' ', $v); // no header injection
}

$name    = clean_line($_POST['name'] ?? '');
$email   = clean_line($_POST['email'] ?? '');
$project = trim((string)($_POST['project'] ?? ''));
$lang    = (($_POST['lang'] ?? 'en') === 'fr') ? 'FR' : 'EN';

if ($name === '' || $project === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)
    || mb_strlen($name) > 200 || mb_strlen($project) > 8000) {
    http_response_code(400);
    echo json_encode(['ok' => false, 'error' => 'invalid']);
    exit;
}

$host = preg_replace('/^www\./', '', $_SERVER['HTTP_HOST'] ?? 'localhost');
$host = preg_replace('/[^a-z0-9.\-]/i', '', $host);

$subject = '=?UTF-8?B?' . base64_encode("New project enquiry from $name (CLARET website)") . '?=';

$body  = "New message from the CLARET website ($lang)\n";
$body .= "----------------------------------------\n\n";
$body .= "Name:  $name\n";
$body .= "Email: $email\n\n";
$body .= "Project:\n$project\n";

$headers  = "From: CLARET website <no-reply@$host>\r\n";
$headers .= "Reply-To: $name <$email>\r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
$headers .= "Content-Transfer-Encoding: 8bit\r\n";

$sent = @mail($TO_EMAIL, $subject, $body, $headers);

if ($sent) {
    echo json_encode(['ok' => true]);
} else {
    http_response_code(500);
    echo json_encode(['ok' => false, 'error' => 'send']);
}
