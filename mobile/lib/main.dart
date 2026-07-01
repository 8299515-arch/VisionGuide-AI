import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:camera/camera.dart';
import 'package:web_socket_channel/web_socket_channel.dart';
import 'package:flutter_tts/flutter_tts.dart';

late List<CameraDescription> cameras;

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  cameras = await availableCameras();
  runApp(const VisionGuideApp());
}

class VisionGuideApp extends StatelessWidget {
  const VisionGuideApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'VisionGuide AI',
      theme: ThemeData.dark(),
      home: const HomePage(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  CameraController? controller;
  WebSocketChannel? channel;
  FlutterTts tts = FlutterTts();

  String lastDescription = "Waiting for AI...";

  @override
  void initState() {
    super.initState();
    initCamera();
    initWebSocket();
  }

  void initCamera() async {
    controller = CameraController(cameras[0], ResolutionPreset.medium);
    await controller!.initialize();
    setState(() {});
    startStream();
  }

  void initWebSocket() {
    channel = WebSocketChannel.connect(
      Uri.parse("ws://localhost:8000/ws"),
    );

    channel!.stream.listen((message) async {
      final data = jsonDecode(message);

      setState(() {
        lastDescription = data['description'] ?? '';
      });

      if (data['voice_output'] == true) {
        await tts.speak(lastDescription);
      }
    });
  }

  void startStream() async {
    while (true) {
      if (controller == null || !controller!.value.isInitialized) continue;

      final image = await controller!.takePicture();

      final bytes = await image.readAsBytes();
      final base64Image = base64Encode(bytes);

      channel?.sink.add(jsonEncode({
        "frame": base64Image,
        "voice": true
      }));

      await Future.delayed(const Duration(seconds: 2));
    }
  }

  @override
  void dispose() {
    controller?.dispose();
    channel?.sink.close();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("VisionGuide AI")),
      body: Column(
        children: [
          Expanded(
            child: controller != null && controller!.value.isInitialized
                ? CameraPreview(controller!)
                : const Center(child: CircularProgressIndicator()),
          ),
          Container(
            padding: const EdgeInsets.all(16),
            child: Text(
              lastDescription,
              style: const TextStyle(fontSize: 18),
            ),
          )
        ],
      ),
    );
  }
}
