/// Assignment 3 - Sprint 1 - Activity A test cases, executed (Activity C)
/// against the UC01 "Select a suggested destination" implementation.
///
/// TC-01 .. TC-04 mirror the test cases in Group08_TestCases.pdf one-to-one:
/// same IDs, same preconditions, same input values, same expected results.
library;

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:vcu_parking_finder/data/vcu_locations.dart';
import 'package:vcu_parking_finder/main.dart';

/// Preconditions shared by the tests: the app is open on the home screen
/// (entry condition of UC01).
Future<void> _pumpHome(WidgetTester tester) async {
  await tester.pumpWidget(const VcuParkingApp());
  await tester.pumpAndSettle();
}

/// Basic path steps 1-2: tap "Input Destination" and let the system display
/// the list of common VCU locations.
Future<void> _openSuggestionList(WidgetTester tester) async {
  await tester.tap(find.byKey(const Key('inputDestinationButton')));
  await tester.pumpAndSettle();
}

String _destinationValue(WidgetTester tester) => tester
    .widget<TextField>(find.byKey(const Key('destinationField')))
    .controller!
    .text;

String _searchValue(WidgetTester tester) =>
    tester.widget<TextField>(find.byKey(const Key('searchField'))).controller!.text;

void main() {
  group('UC01 - Select a suggested destination', () {
    testWidgets(
      'TC-01 | Positive / basic path: select a suggestion from the full list',
      (WidgetTester tester) async {
        // Preconditions: app open on the home screen, destination field empty.
        await _pumpHome(tester);
        expect(find.byKey(const Key('destinationField')), findsOneWidget);
        expect(_destinationValue(tester), '');
        expect(
          find.widgetWithText(ElevatedButton, 'Input Destination'),
          findsOneWidget,
        );

        // Step 1: actor selects the "input destination" button.
        await _openSuggestionList(tester);

        // Step 2: system displays the full predefined list of VCU locations
        // (BR01 - suggestions come only from the predefined list).
        for (final String location in VcuLocations.suggestions) {
          expect(
            find.text(location),
            findsOneWidget,
            reason: 'Predefined location "$location" must be suggested',
          );
        }
        expect(find.byType(ListTile),
            findsNWidgets(VcuLocations.suggestions.length));

        // Step 3: actor selects a location from the list.
        await tester.tap(find.text('Library'));
        await tester.pumpAndSettle();

        // Step 4: system fills the destination input field with the selection.
        expect(_destinationValue(tester), 'Library');
        expect(find.byKey(const Key('inputDestinationButton')), findsOneWidget);
      },
    );

    testWidgets(
      'TC-02 | Positive / alternative A01: case-insensitive filtering (BR02)',
      (WidgetTester tester) async {
        // Preconditions: app open on the home screen, destination field empty.
        await _pumpHome(tester);
        expect(_destinationValue(tester), '');

        // Steps 1-2: open the suggestion list.
        await _openSuggestionList(tester);

        // A01: actor types in the destination search field; mixed letter case.
        await tester.enterText(
          find.byKey(const Key('searchField')),
          'eNgInEeRiNg wE',
        );
        await tester.pumpAndSettle();

        // System filters suggestions to match the text, ignoring case.
        expect(find.text('Engineering West Hall'), findsOneWidget);
        expect(find.byType(ListTile), findsOneWidget);
        expect(find.text('Library'), findsNothing);
        expect(find.text('Hibbs Hall'), findsNothing);
        expect(find.byKey(const Key('noMatchMessage')), findsNothing);

        // A01 step 4 / basic path step 3-4: select and fill the field.
        await tester.tap(find.text('Engineering West Hall'));
        await tester.pumpAndSettle();

        expect(_destinationValue(tester), 'Engineering West Hall');
      },
    );

    testWidgets(
      'TC-03 | Negative / exception E01: no matching suggestion, then back (A02)',
      (WidgetTester tester) async {
        // Preconditions: home screen with destination already set to "Library"
        // by a previous run of the basic path.
        await _pumpHome(tester);
        await _openSuggestionList(tester);
        await tester.tap(find.text('Library'));
        await tester.pumpAndSettle();
        expect(_destinationValue(tester), 'Library');

        // Step 1: actor opens the suggestion list again.
        await _openSuggestionList(tester);

        // Step 2: actor types text that matches no predefined location.
        await tester.enterText(find.byKey(const Key('searchField')), 'zzz999');
        await tester.pumpAndSettle();

        // E01: system shows the exception message and offers no selection.
        expect(find.byKey(const Key('noMatchMessage')), findsOneWidget);
        expect(find.text('No matching VCU locations'), findsOneWidget);
        expect(find.byType(ListTile), findsNothing);

        // A02: actor presses "back"; system returns to the home screen and
        // the previously selected destination is unchanged.
        await tester.tap(find.byTooltip('Back'));
        await tester.pumpAndSettle();

        expect(find.byKey(const Key('destinationField')), findsOneWidget);
        expect(_destinationValue(tester), 'Library');
        expect(
          find.widgetWithText(ElevatedButton, 'Input Destination'),
          findsOneWidget,
        );
      },
    );

    testWidgets(
      'TC-04 | Boundary: destination search length 0 / 100 / 101 characters',
      (WidgetTester tester) async {
        // Preconditions: app open on the home screen, suggestion list open,
        // search field empty.
        await _pumpHome(tester);
        await _openSuggestionList(tester);
        expect(_searchValue(tester), '');

        // Minimum boundary (0 characters): the full list stays visible and no
        // exception message is shown.
        expect(find.byType(ListTile),
            findsNWidgets(VcuLocations.suggestions.length));
        expect(find.byKey(const Key('noMatchMessage')), findsNothing);

        // Boundary value: exactly 100 characters are accepted.
        await tester.enterText(
          find.byKey(const Key('searchField')),
          'a' * 100,
        );
        await tester.pump();
        expect(_searchValue(tester).length, 100,
            reason: 'A 100-character destination must be accepted');

        // Just outside the boundary: the 101st character must be rejected.
        await tester.enterText(
          find.byKey(const Key('searchField')),
          'a' * 100 + 'b',
        );
        await tester.pump();
        expect(_searchValue(tester).length, 100,
            reason: 'Input must stop at the 100-character limit');
        expect(_searchValue(tester).contains('b'), isFalse,
            reason: 'The 101st character must not be stored');

        // Clearing back to the minimum restores the full predefined list.
        await tester.enterText(find.byKey(const Key('searchField')), '');
        await tester.pump();
        expect(_searchValue(tester), '');
        expect(find.byType(ListTile),
            findsNWidgets(VcuLocations.suggestions.length));
        expect(find.byKey(const Key('noMatchMessage')), findsNothing);
      },
    );
  });
}
