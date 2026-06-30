import 'package:flutter/material.dart';

void main() {
  runApp(const VisionGuideApp());
}

class VisionGuideApp extends StatelessWidget {
  const VisionGuideApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'VisionGuide AI',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.blue),
      ),
      home: const VoiceHomeScreen(),
    );
  }
}

class VoiceHomeScreen extends StatefulWidget {
  const VoiceHomeScreen({super.key});

  @override
  State<VoiceHomeScreen> createState() => _VoiceHomeScreenState();
}

class _VoiceHomeScreenState extends State<VoiceHomeScreen> {
  String status = "VisionGuide AI is ready";

  @override
  void initState() {
    super.initState();
    // TODO: initialize voice engine, permissions, AI client
  }

  void onVoiceCommand(String command) {
    setState(() {
      status = "Heard: $command";
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('VisionGuide AI'),
      ),
      body: Center(
        child: Semantics(
          label: "Voice assistant status",
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Icon(Icons.record_voice_over, size: 80),
              const SizedBox(height: 20),
              Text(status, textAlign: TextAlign.center),
              const SizedBox(height: 30),
              ElevatedButton(
                onPressed: () {
                  onVoiceCommand("help");
                },
                child: const Text("Activate Voice Command"),
              ),
            ],
          ),
        ),
      ),
    );
  }
}