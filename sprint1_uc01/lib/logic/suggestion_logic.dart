import '../data/vcu_locations.dart';

/// Returns the predefined VCU locations that match [query].
///
/// Business rules covered:
///  * BR01 - only locations from the predefined list can ever be returned.
///  * BR02 - suggestion matching is NOT case-sensitive.
///
/// Equivalence behaviour:
///  * empty / whitespace-only query  -> the full list (nothing is rejected)
///  * query that matches at least one location (any letter case) -> the
///    matching subset
///  * query that matches nothing -> an empty list, which the UI turns into
///    the exception message of E01 ("No matching VCU locations")
List<String> filterSuggestions(
  String query, {
  List<String> pool = VcuLocations.suggestions,
}) {
  final String normalized = query.trim().toLowerCase();
  if (normalized.isEmpty) {
    return List<String>.of(pool);
  }
  return pool
      .where((String location) => location.toLowerCase().contains(normalized))
      .toList();
}

/// Enforces the 100-character limit of the `destination` data element.
///
/// Input at the boundary (exactly 100 characters) is accepted unchanged;
/// input just outside the boundary (101 characters) is truncated to 100.
String limitDestinationInput(String value) {
  if (value.length <= VcuLocations.destinationMaxLength) {
    return value;
  }
  return value.substring(0, VcuLocations.destinationMaxLength);
}
