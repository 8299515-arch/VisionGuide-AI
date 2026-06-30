import 'package:flutter_tts/flutter_tts.dart';

/// VoiceEngine handles TTS + future STT integration
class VoiceEngine {
  final FlutterTts _tts = FlutterTts();

  Future<void> init() async {
    await _tts.setLanguage("en-US");
    await _tts.setSpeechRate(0.5);
    await _tts.setVolume(1.0);
    await _tts.setPitch(1.0);
  }

  Future<void> speak(String text) async {
    await _tts.stop();
    await _tts.speak(text);
  }

  Future<void> stop() async {
    await _tts.stop();
  }

  /// Placeholder for Speech-to-Text (future integration)
  Future<String?> listen() async {
    // TODO: integrate speech_to_text package
    return "voice input not implemented yet";
  }
}
