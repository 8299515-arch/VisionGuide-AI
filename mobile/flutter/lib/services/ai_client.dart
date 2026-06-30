import 'dart:convert';
import 'package:http/http.dart' as http;

/// AIClient connects Flutter app to FastAPI backend
/// VisionGuide AI core communication layer
class AIClient {
  final String baseUrl;
  String? token;

  AIClient({required this.baseUrl});

  void setToken(String jwt) {
    token = jwt;
  }

  Map<String, String> get _headers {
    return {
      'Content-Type': 'application/json',
      if (token != null) 'Authorization': 'Bearer $token',
    };
  }

  /// Login request
  Future<Map<String, dynamic>> login(String email, String password) async {
    final res = await http.post(
      Uri.parse('$baseUrl/auth/login'),
      headers: _headers,
      body: jsonEncode({
        'email': email,
        'password': password,
      }),
    );
    return jsonDecode(res.body);
  }

  /// Register request
  Future<Map<String, dynamic>> register(String email, String username, String password) async {
    final res = await http.post(
      Uri.parse('$baseUrl/auth/register'),
      headers: _headers,
      body: jsonEncode({
        'email': email,
        'username': username,
        'password': password,
      }),
    );
    return jsonDecode(res.body);
  }

  /// Vision AI request (camera frame → description)
  Future<Map<String, dynamic>> analyzeVision(String imageBase64) async {
    final res = await http.post(
      Uri.parse('$baseUrl/ai/vision'),
      headers: _headers,
      body: jsonEncode({
        'image': imageBase64,
      }),
    );
    return jsonDecode(res.body);
  }

  /// OCR text recognition
  Future<Map<String, dynamic>> recognizeText(String imageBase64) async {
    final res = await http.post(
      Uri.parse('$baseUrl/ai/ocr'),
      headers: _headers,
      body: jsonEncode({
        'image': imageBase64,
      }),
    );
    return jsonDecode(res.body);
  }

  /// Emergency SOS
  Future<Map<String, dynamic>> sendEmergency(double lat, double lng) async {
    final res = await http.post(
      Uri.parse('$baseUrl/emergency/sos'),
      headers: _headers,
      body: jsonEncode({
        'lat': lat,
        'lng': lng,
      }),
    );
    return jsonDecode(res.body);
  }
}