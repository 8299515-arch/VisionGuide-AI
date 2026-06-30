import 'package:speech_to_text/speech_to_text.dart' as stt;

/// SpeechEngine handles Speech-to-Text (STT)
/// for VisionGuide AI voice-first navigation.
class SpeechEngine {
  final stt.SpeechToText _speech = stt.SpeechToText();

  bool _isInitialized = false;

  Future<bool> init() async {
    _isInitialized = await _speech.initialize(
      onStatus: (status) {
        // You can log status changes here
        // e.g. listening, notListening
      },
      onError: (error) {
        // Handle STT errors gracefully
      },
    );
    return _isInitialized;
  }

  bool get isAvailable => _isInitialized;

  Future<void> startListening({required Function(String text) onResult}) async {
    if (!_isInitialized) return;

    await _speech.listen(
      onResult: (result) {
        final text = result.recognizedWords;
        if (text.isNotEmpty) {
          onResult(text);
        }
      },
      listenMode: stt.ListenMode.dictation,
      partialResults: true,
    );
  }

  Future<void> stopListening() async {
    await _speech.stop();
  }

  Future<void> cancel() async {
    await _speech.cancel();
  }
}
