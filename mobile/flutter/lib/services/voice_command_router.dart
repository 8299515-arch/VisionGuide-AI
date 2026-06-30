import 'dart:convert';

/// VoiceCommandRouter interprets speech text into app actions
/// for VisionGuide AI (voice-first assistant).
class VoiceCommandRouter {
  final Function(String message)? onSpeak;

  VoiceCommandRouter({this.onSpeak});

  /// Main entry point: raw speech → intent
  void handleCommand(String input) {
    final text = input.toLowerCase().trim();

    if (text.isEmpty) return;

    // Navigation commands
    if (text.contains('navigate') || text.contains('go to')) {
      _navigate(text);
      return;
    }

    // Emergency
    if (text.contains('help') || text.contains('emergency') || text.contains('sos')) {
      _emergency();
      return;
    }

    // Describe environment
    if (text.contains('what do i see') || text.contains('describe') || text.contains('what is in front')) {
      _describe();
      return;
    }

    // Read text
    if (text.contains('read') || text.contains('text')) {
      _readText();
      return;
    }

    // Default fallback
    _unknown();
  }

  void _navigate(String text) {
    onSpeak?.call("Starting navigation mode");
    // TODO: connect to backend /navigation
  }

  void _emergency() {
    onSpeak?.call("Emergency mode activated. Contacting help.");
    // TODO: trigger SOS API
  }

  void _describe() {
    onSpeak?.call("Analyzing environment...");
    // TODO: call /ai/vision
  }

  void _readText() {
    onSpeak?.call("Reading text from camera...");
    // TODO: call /ai/ocr
  }

  void _unknown() {
    onSpeak?.call("Sorry, I didn't understand that command.");
  }
}