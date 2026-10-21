/// Predefined data used by UC01 - Select a suggested destination.
///
/// Business rule BR01: suggestions come only from the predefined list of
/// VCU locations. The list is `const` so it cannot be modified at runtime.
class VcuLocations {
  VcuLocations._();

  /// Data description (UC01): destination is a String with max length 100.
  static const int destinationMaxLength = 100;

  /// Predefined list of common VCU locations shown in step 2 of the basic
  /// path. "Library" and "Engineering West Hall" are the examples given in
  /// the approved use case.
  static const List<String> suggestions = <String>[
    'Library',
    'Engineering West Hall',
    'Engineering East Hall',
    'University Student Commons',
    'Grace Harris Center',
    'Hibbs Hall',
    'Snead Hall',
    'Pollak Building',
    'Shafer Street Dining Center',
  ];
}
