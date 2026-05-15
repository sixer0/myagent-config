<?php
/**
 * Nailla Chat API Endpoint
 * Routes chat messages to OpenClaw agent
 * 
 * Usage: Include this in your website backend or run as standalone PHP server
 */

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

// Handle CORS preflight
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

// OpenClaw Gateway Configuration
$OPENCLAW_GATEWAY_URL = 'http://localhost:3000'; // Adjust to your OpenClaw gateway URL
$OPENCLAW_AGENT_ID = 'nailla-cs';
$OPENCLAW_API_KEY = getenv('OPENCLAW_API_KEY') ?: 'your-api-key-here';

// Get request data
$input = json_decode(file_get_contents('php://input'), true);

if (!$input || !isset($input['message'])) {
    http_response_code(400);
    echo json_encode(['error' => 'Invalid request']);
    exit;
}

$message = $input['message'];
$sessionId = $input['sessionId'] ?? session_id();

// Call OpenClaw Gateway
$ch = curl_init();
curl_setopt_array($ch, [
    CURLOPT_URL => $OPENCLAW_GATEWAY_URL . '/api/agents/' . $OPENCLAW_AGENT_ID . '/chat',
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => json_encode([
        'message' => $message,
        'sessionId' => $sessionId,
        'context' => [
            'source' => 'website_chat',
            'timestamp' => time()
        ]
    ]),
    CURLOPT_HTTPHEADER => [
        'Content-Type: application/json',
        'Authorization: Bearer ' . $OPENCLAW_API_KEY
    ],
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_TIMEOUT => 30
]);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

if ($httpCode === 200) {
    $data = json_decode($response, true);
    echo json_encode(['response' => $data['response'] ?? $data['text'] ?? '']);
} else {
    // Fallback response if agent unavailable
    echo json_encode([
        'response' => "Hai! Terima kasih sudah menghubungi. Saat ini Nailla sedang offline. Silakan kirim email ke hello@sixer0-bk.my.id atau WhatsApp ke +62xxx untuk respon lebih cepat."
    ]);
}
?>