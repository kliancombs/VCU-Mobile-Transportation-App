# Assignment 3 - Sprint 1 - Group 8 - UC01

Selected use case: **UC01 – Select a suggested destination** (FR02),
chosen because the Activity 2 feedback showed UC03's spec never actually
sorts or shows results (and its entry condition/BR02 contradict its own
steps) while UC02's steps contradict its entry condition (copied from
UC01). UC01 was the only internally consistent specification.

## Layout

| Path | Purpose |
|---|---|
| `../Group08_TestCases.pdf` | The deliverable (page 1 info, test cases, execution results, video URL) |
| `../make_test_pdf.py` | Regenerates the PDF (edit `VIDEO_URL` at the top, then `python3 make_test_pdf.py`) |
| `lib/data/vcu_locations.dart` | Predefined VCU list (BR01) + 100-char limit (task T1) |
| `lib/logic/suggestion_logic.dart` | Case-insensitive filter (BR02), input length limit (task T2) |
| `lib/screens/home_screen.dart` | Home screen, destination field, "Input Destination" button (task T3) |
| `lib/screens/suggestion_screen.dart` | Search + filtered list + "No matching VCU locations" (task T4) |
| `lib/main.dart` | App entry / integration (task T5) |
| `test/uc01_test.dart` | TC-01..TC-04, identical IDs/inputs/expected results to the PDF |

## Verified checks (Oct 20, 2026)

- `flutter analyze` → No issues found
- `flutter test` → **All 4 tests passed** (TC-01, TC-02, TC-03, TC-04 = PASS)
- `flutter build web --release` → built successfully

PATH note: Flutter is at `/opt/homebrew/bin/flutter` —
`export PATH="$PATH:/opt/homebrew/bin"` in a new terminal.

## Recording the 4-minute video

1. Run the app: `cd sprint1_uc01 && flutter run -d chrome`
2. Record: QuickTime Player → File → New Screen Recording (or `⌘⇧5`),
   choose the Chrome window, enable narration. Keep it to 4:00.
3. Suggested script:
   - 0:00–0:25 – "Group 8, UC01 Select a suggested destination, tests TC-01..TC-04"
   - 0:25–1:20 – **TC-01**: show empty home → tap Input Destination → full 8-item list → tap Library → destination field reads "Library" → **PASS**
   - 1:20–2:15 – **TC-02**: type `eNgInEeRiNg wE` → only "Engineering West Hall" left → tap → field reads "Engineering West Hall" → **PASS**
   - 2:15–3:05 – **TC-03**: select Library first, reopen list, type `zzz999` → "No matching VCU locations" → Back → field still "Library" → **PASS**
   - 3:05–3:45 – **TC-04**: empty field shows full list → type 100 `a`s (counter 100/100) → 101st character `b` rejected (still 100) → clear → list restored → **PASS**
   - 3:45–4:00 – summary: all four planned tests match their expected results
4. Upload unlisted/public with **no permission request needed**, copy the URL.
5. Put the URL in `make_test_pdf.py` (`VIDEO_URL = ...`), rerun
   `python3 make_test_pdf.py`, submit the regenerated `Group08_TestCases.pdf`.
