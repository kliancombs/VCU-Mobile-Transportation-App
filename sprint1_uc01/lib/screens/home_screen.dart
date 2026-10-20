import 'package:flutter/material.dart';

import '../app_theme.dart';
import 'suggestion_screen.dart';

/// Home screen - entry condition of UC01:
/// "The app is open in the home screen".
///
/// Holds the `destination` input field that the system fills in basic path
/// step 4, and the "input destination" button of basic path step 1.
class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final TextEditingController destinationController = TextEditingController();

  /// Basic path steps 1-4: open the suggestion list, wait for the location
  /// the actor selects, then fill the destination input field with it.
  Future<void> _openSuggestionList() async {
    final String? selected = await Navigator.push<String>(
      context,
      MaterialPageRoute<String>(
        builder: (BuildContext context) => const SuggestionScreen(),
      ),
    );
    if (selected != null && mounted) {
      setState(() {
        destinationController.text = selected;
      });
    }
  }

  @override
  void dispose() {
    destinationController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('VCU Parking Finder'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(24),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const Text(
              'Where are you going?',
              style: TextStyle(
                fontSize: 20,
                fontWeight: FontWeight.bold,
                color: VcuTheme.gold,
                letterSpacing: 0.5,
              ),
            ),
            const SizedBox(height: 16),
            TextField(
              key: const Key('destinationField'),
              controller: destinationController,
              maxLength: 100,
              // UC01 step 4: the system fills this field with the selected
              // location, so the user never types the destination here.
              // Tapping it opens the same suggestion list as the button.
              readOnly: true,
              showCursor: false,
              enableInteractiveSelection: false,
              onTap: _openSuggestionList,
              decoration: const InputDecoration(
                border: OutlineInputBorder(),
                labelText: 'Destination',
                hintText: 'Select a destination',
                suffixIcon: Icon(Icons.search),
              ),
            ),
            const SizedBox(height: 24),
            ElevatedButton(
              key: const Key('inputDestinationButton'),
              onPressed: _openSuggestionList,
              child: const Text('Input Destination'),
            ),
          ],
        ),
      ),
    );
  }
}
