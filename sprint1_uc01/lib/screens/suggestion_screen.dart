import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../app_theme.dart';
import '../data/vcu_locations.dart';
import '../logic/suggestion_logic.dart';

/// Suggestion screen - basic path steps 2-3 of UC01 plus alternative path
/// A01 (typing filters the suggestions) and exception path E01 (typed text
/// matches no suggestion -> "No matching VCU locations").
class SuggestionScreen extends StatefulWidget {
  const SuggestionScreen({super.key});

  @override
  State<SuggestionScreen> createState() => _SuggestionScreenState();
}

class _SuggestionScreenState extends State<SuggestionScreen> {
  final TextEditingController searchController = TextEditingController();
  String query = '';

  /// A01: every keystroke re-filters the suggestions (BR02: matching ignores
  /// letter case). The 100-character destination limit is enforced both by
  /// [LengthLimitingTextInputFormatter] and explicitly, so the rule holds on
  /// every platform.
  void _onQueryChanged(String value) {
    final String limited = limitDestinationInput(value);
    if (limited != value) {
      searchController.value = TextEditingValue(
        text: limited,
        selection: TextSelection.collapsed(offset: limited.length),
      );
    }
    setState(() => query = limited);
  }

  @override
  void dispose() {
    searchController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final List<String> results = filterSuggestions(query);

    return Scaffold(
      appBar: AppBar(
        title: const Text('Select Destination'),
      ),
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Padding(
            padding: const EdgeInsets.fromLTRB(16, 16, 16, 0),
            child: TextField(
              key: const Key('searchField'),
              controller: searchController,
              autofocus: true,
              maxLength: VcuLocations.destinationMaxLength,
              inputFormatters: <TextInputFormatter>[
                LengthLimitingTextInputFormatter(
                  VcuLocations.destinationMaxLength,
                ),
              ],
              onChanged: _onQueryChanged,
              decoration: const InputDecoration(
                border: OutlineInputBorder(),
                labelText: 'Destination search',
                hintText: 'Type to filter VCU locations',
                prefixIcon: Icon(Icons.search),
              ),
            ),
          ),
          Expanded(
            child: results.isEmpty
                ? const Center(
                    child: Padding(
                      padding: EdgeInsets.all(16),
                      child: Text(
                        'No matching VCU locations',
                        key: Key('noMatchMessage'),
                        textAlign: TextAlign.center,
                        style: TextStyle(
                          fontSize: 16,
                          color: VcuTheme.gold,
                          fontWeight: FontWeight.w600,
                        ),
                      ),
                    ),
                  )
                : ListView.builder(
                    itemCount: results.length,
                    itemBuilder: (BuildContext context, int index) {
                      final String location = results[index];
                      return ListTile(
                        key: Key('suggestion_$location'),
                        title: Text(location),
                        onTap: () => Navigator.pop(context, location),
                      );
                    },
                  ),
          ),
        ],
      ),
    );
  }
}
