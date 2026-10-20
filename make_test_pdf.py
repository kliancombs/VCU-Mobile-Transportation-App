#!/usr/bin/env python3
"""Builds Group08_TestCases.pdf - Assignment 3, Sprint 1 deliverable."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether,
)

OUT = "/Users/root1/untitled folder/Group08_TestCases.pdf"

# ---------------------------------------------------------------- team info --
GROUP = "8"
PROJECT = "VCU Parking Finder"
MEMBERS = [
    "Cedric Amoah-Awuah",
    "Ezra Hughes",
    "Cesar Facundo",
    "Yahya Alawneh",
    "Klian Combs",
]
UC_ID = "UC01"
UC_NAME = "Select a suggested destination"
UC_FR = "FR02 - The software must suggest common VCU locations as destinations"

# Filled in after running `flutter test`.
RESULTS = {
    "TC-01": (
        "PASS",
        "Home screen showed an empty destination field and the \"Input "
        "Destination\" button. After the tap, exactly the 8 predefined VCU "
        "locations were listed (no extra entries). Selecting \"Library\" "
        "returned to the home screen and the destination field read "
        "\"Library\". Matches expected results 1-4."),
    "TC-02": (
        "PASS",
        "Typing eNgInEeRiNg wE reduced the visible list to exactly "
        "\"Engineering West Hall\"; Library, Hibbett Hall and the other "
        "non-matching locations disappeared and no exception message was "
        "shown. After the tap the destination field read \"Engineering West "
        "Hall\". Case-insensitive matching (BR02) confirmed. Matches expected "
        "results 1-4."),
    "TC-03": (
        "PASS",
        "Typing zzz999 cleared the list (0 entries) and displayed \"No "
        "matching VCU locations\". Pressing Back returned to the home screen "
        "with the destination field still reading \"Library\" and the button "
        "visible - the rejected input changed no state. Matches expected "
        "results 1-5."),
    "TC-04": (
        "PASS",
        "Empty field (0 chars) showed the full 8-item list with no message; "
        "100 characters were accepted (counter 100/100); the attempted 101st "
        "character \"b\" was rejected - the field still held 100 characters "
        "ending in \"a\". Clearing restored the full list. Matches expected "
        "results 1-6."),
}
VIDEO_URL = "PASTE WORKING VIDEO URL HERE"

TASKS = [
    ("T1 - Data handling",
     "Predefined VCU suggestion list (BR01) and the 100-character destination "
     "limit constant. Files: lib/data/vcu_locations.dart",
     "Klian Combs"),
    ("T2 - Back-end logic / validation",
     "Case-insensitive suggestion matcher (BR02), no-match detection for E01, "
     "and destination input-length enforcement. Files: lib/logic/suggestion_logic.dart",
     "Cesar Facundo"),
    ("T3 - User interface: home screen",
     "Destination input field, \"Input Destination\" button, and receiving the "
     "selected location to fill the field (basic path steps 1 and 4). "
     "Files: lib/screens/home_screen.dart",
     "Ezra Hughes"),
    ("T4 - User interface: suggestion screen",
     "Search field with filtering (A01), suggestion list, \"No matching VCU "
     "locations\" message (E01), and back navigation (A02). "
     "Files: lib/screens/suggestion_screen.dart",
     "Yahya Alawneh"),
    ("T5 - Integration and developer checks",
     "Navigation wiring, app theme/entry point, running flutter analyze and "
     "the TC-01..TC-04 test suite before test execution. "
     "Files: lib/main.dart, test/uc01_test.dart",
     "Cedric Amoah-Awuah"),
]

# ---------------------------------------------------------------- styles -----
styles = getSampleStyleSheet()
H1 = ParagraphStyle("H1x", parent=styles["Heading1"], fontSize=16, spaceAfter=8,
                    textColor=colors.HexColor("#003F88"))
H2 = ParagraphStyle("H2x", parent=styles["Heading2"], fontSize=13, spaceBefore=10,
                    spaceAfter=6, textColor=colors.HexColor("#003F88"))
H3 = ParagraphStyle("H3x", parent=styles["Heading3"], fontSize=11, spaceBefore=8,
                    spaceAfter=4)
BODY = ParagraphStyle("BODYx", parent=styles["BodyText"], fontSize=9.5, leading=12.5)
SMALL = ParagraphStyle("SMALLx", parent=BODY, fontSize=8.5, leading=11)
CELL = ParagraphStyle("CELLx", parent=BODY, fontSize=9, leading=11.5)
CELLB = ParagraphStyle("CELLBx", parent=CELL, fontName="Helvetica-Bold")
CENTER = ParagraphStyle("CENTERx", parent=BODY, alignment=TA_CENTER)

TEST_CASES = [
    {
        "id": "TC-01",
        "objective": (
            "Verify that a user can open the suggestion list from the home screen, "
            "that the system displays exactly the predefined list of common VCU "
            "locations, and that selecting \"Library\" fills the destination input "
            "field. (Traces to UC01 basic path, steps 1-4.)"),
        "preconditions": (
            "1. The app is launched and the home screen is displayed "
            "(UC01 entry condition).<br/>"
            "2. The destination input field is empty.<br/>"
            "3. The suggestion list has not been opened yet in this session."),
        "steps": (
            "1. Confirm the home screen shows an empty Destination field and an "
            "\"Input Destination\" button.<br/>"
            "2. Tap the \"Input Destination\" button.<br/>"
            "3. Read the suggestion list now displayed by the system and count its "
            "entries.<br/>"
            "4. Tap the list entry \"Library\".<br/>"
            "5. Read the destination input field on the home screen."),
        "inputs": (
            "Typed input: none.<br/>"
            "Selection: <b>Library</b> (an entry of the predefined VCU list)."),
        "expected": (
            "1. Home screen shows Destination field containing 0 characters and the "
            "\"Input Destination\" button.<br/>"
            "2. The list contains exactly the 8 predefined locations - Library, "
            "Engineering West Hall, University Student Commons, Grace Harris Center, "
            "Hibbett Hall, Snead Hall, Pollak Building, Shafer Street Dining Center - "
            "and no free-typed or invented entries (BR01).<br/>"
            "3. Tapping \"Library\" returns to the home screen.<br/>"
            "4. The destination field now contains exactly the text \"Library\"."),
        "rationale": (
            "<b>Positive</b> scenario executing the complete basic path. Covers the "
            "valid equivalence class \"selection from the predefined list\". Useful "
            "because it proves the entry point, the display of suggestions (FR02) "
            "and the hand-off of the selected value to the destination field in one "
            "traceable run, and it verifies BR01 (no non-predefined suggestions)."),
    },
    {
        "id": "TC-02",
        "objective": (
            "Verify alternative path A01: typed text filters the suggestion list, "
            "the match ignores letter case (BR02), and choosing the filtered result "
            "fills the destination input field."),
        "preconditions": (
            "1. The app is launched and the home screen is displayed.<br/>"
            "2. The destination input field is empty.<br/>"
            "3. The suggestion list has not been opened yet in this session."),
        "steps": (
            "1. Tap the \"Input Destination\" button.<br/>"
            "2. Confirm the full suggestion list is displayed.<br/>"
            "3. Tap the \"Destination search\" field and type: "
            "<b>eNgInEeRiNg wE</b><br/>"
            "4. Read the list entries that remain visible.<br/>"
            "5. Tap \"Engineering West Hall\".<br/>"
            "6. Read the destination input field on the home screen."),
        "inputs": (
            "Search text: <b>eNgInEeRiNg wE</b> - deliberately mixed letter case; "
            "valid because it is a substring of a predefined location, but written "
            "in a case that does not literally appear in the list."),
        "expected": (
            "1. The full list of 8 locations appears first.<br/>"
            "2. After typing, exactly one entry remains: \"Engineering West Hall\". "
            "\"Library\", \"Hibbett Hall\" and the other non-matching locations are "
            "removed from the list.<br/>"
            "3. The message \"No matching VCU locations\" is NOT shown.<br/>"
            "4. After the tap the app returns home and the destination field "
            "contains exactly \"Engineering West Hall\"."),
        "rationale": (
            "<b>Positive</b> scenario for alternative path <b>A01</b> and an "
            "<b>equivalence-class</b> test of the input partitions of the search "
            "field: query that matches at least one location. The mixed-case value "
            "proves BR02 (matching is not case-sensitive) without retesting "
            "redundant same-case values. It exercises filtering, which TC-01 does "
            "not, so the two tests are not redundant."),
    },
    {
        "id": "TC-03",
        "objective": (
            "Verify exception path E01: text that matches no predefined location "
            "displays \"No matching VCU locations\" and offers no selectable "
            "suggestion, and that pressing back (A02) returns to the home screen "
            "with the previously selected destination unchanged."),
        "preconditions": (
            "1. The app is on the home screen.<br/>"
            "2. The destination input field already contains <b>Library</b>, set by "
            "an earlier run of the basic path.<br/>"
            "3. The suggestion list is closed."),
        "steps": (
            "1. Tap the \"Input Destination\" button.<br/>"
            "2. Tap the \"Destination search\" field and type: <b>zzz999</b><br/>"
            "3. Read the list area and any message shown.<br/>"
            "4. Press the Back button in the app bar.<br/>"
            "5. Read the home screen and the destination input field."),
        "inputs": (
            "Search text: <b>zzz999</b> - invalid because it is not a predefined "
            "VCU location and is not a substring of any entry in the suggestion "
            "list (invalid equivalence partition, exception condition E01)."),
        "expected": (
            "1. The suggestion list is displayed when opened.<br/>"
            "2. After typing zzz999 the list shows zero entries and the message "
            "<b>\"No matching VCU locations\"</b> appears.<br/>"
            "3. No list entry can be selected.<br/>"
            "4. After pressing Back the home screen is shown.<br/>"
            "5. The destination field still contains exactly \"Library\" - the "
            "rejected input changed no state - and the \"Input Destination\" "
            "button is visible again."),
        "rationale": (
            "<b>Negative</b> scenario covering <b>exception path E01</b> and the "
            "invalid equivalence class \"query matching nothing\". It also verifies "
            "the return flow of <b>A02</b> (back to home) and that a rejected "
            "input causes no partial data change. TC-01/TC-02 verify accepted "
            "input, so this test adds genuinely different behavior."),
    },
    {
        "id": "TC-04",
        "objective": (
            "Verify the ordered boundary of the destination data element "
            "(String, length 100): empty input, input exactly at the limit, and "
            "input just outside the limit."),
        "preconditions": (
            "1. The app is on the home screen with an empty destination field.<br/>"
            "2. The suggestion list is open.<br/>"
            "3. The search field is empty (0 characters) and the full list of 8 "
            "locations is visible."),
        "steps": (
            "1. With the search field empty, read the list area.<br/>"
            "2. Type a string of exactly 100 characters: the letter <b>a</b> "
            "repeated 100 times.<br/>"
            "3. Without clearing, attempt to type one more character: <b>b</b> "
            "(101 characters attempted).<br/>"
            "4. Read the contents of the search field.<br/>"
            "5. Delete all characters so the field is empty again.<br/>"
            "6. Read the list area."),
        "inputs": (
            "1. <b>''</b> (empty string, 0 characters - minimum boundary)<br/>"
            "2. <b>a</b> x 100 (exactly 100 characters - value at the boundary)<br/>"
            "3. <b>a</b> x 100 followed by <b>b</b> (101 characters attempted - "
            "value just outside the boundary)"),
        "expected": (
            "1. All 8 predefined locations are listed and no message is shown - "
            "empty input is valid, not an error.<br/>"
            "2. The field holds exactly 100 characters; the character counter "
            "reads 100/100.<br/>"
            "3.-4. The field still holds exactly 100 characters ending in \"a\"; "
            "the 101st character \"b\" is rejected and never stored.<br/>"
            "5.-6. The field is empty, the full list of 8 locations reappears and "
            "no exception message is displayed."),
        "rationale": (
            "<b>Boundary</b> value analysis on the ordered input length declared in "
            "the UC01 data description (destination, length 100): value at the "
            "boundary (100), just outside it (101), and the minimum (0 / empty "
            "input, explicitly listed as a boundary case in the assignment). It "
            "tests the data limit of the use case rather than the content matching "
            "tested in TC-02/TC-03, so it exercises a distinct aspect."),
    },
]


def test_case_table(tc):
    rows = [
        ("Test Case ID", tc["id"]),
        ("Test Objective", tc["objective"]),
        ("Preconditions", tc["preconditions"]),
        ("Test Steps", tc["steps"]),
        ("Input Values", tc["inputs"]),
        ("Expected Results", tc["expected"]),
        ("Coverage Rationale", tc["rationale"]),
    ]
    data = [[Paragraph(label, CELLB), Paragraph(text, CELL)] for label, text in rows]
    table = Table(data, colWidths=[1.35 * inch, 5.35 * inch], repeatRows=0)
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.6, colors.HexColor("#003F88")),
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#E8F0FA")),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return table


def info_table():
    rows = [
        ("Group number", GROUP),
        ("Project name", PROJECT),
        ("Team members", "<br/>".join(MEMBERS)),
        ("Selected use case", f"<b>{UC_ID} - {UC_NAME}</b>"),
        ("Traces to requirement", UC_FR),
        ("Actor", "User"),
        ("Implementation", "Dart / Flutter (mobile app), lib/ and test/ of the "
                           "sprint build; test suite test/uc01_test.dart"),
    ]
    data = [[Paragraph(a, CELLB), Paragraph(b, CELL)] for a, b in rows]
    t = Table(data, colWidths=[1.6 * inch, 5.1 * inch])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.6, colors.HexColor("#003F88")),
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#E8F0FA")),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t


def results_table():
    header = [Paragraph("<b>Test Case</b>", CELL),
              Paragraph("<b>Result</b>", CELL),
              Paragraph("<b>Observation recorded during execution</b>", CELL)]
    data = [header]
    for tc_id, (result, note) in RESULTS.items():
        data.append([
            Paragraph(tc_id, CELL),
            Paragraph(f"<b>{result}</b>", CELL),
            Paragraph(note, CELL),
        ])
    t = Table(data, colWidths=[0.9 * inch, 0.8 * inch, 5.0 * inch])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.6, colors.HexColor("#003F88")),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E8F0FA")),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t


def tasks_table():
    data = [[Paragraph("<b>Task</b>", CELL), Paragraph("<b>Scope and files</b>", CELL),
             Paragraph("<b>Assigned to</b>", CELL)]]
    for task, scope, owner in TASKS:
        data.append([Paragraph(task, CELL), Paragraph(scope, CELL),
                     Paragraph(owner, CELL)])
    t = Table(data, colWidths=[1.5 * inch, 3.9 * inch, 1.3 * inch])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.6, colors.HexColor("#003F88")),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E8F0FA")),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t


def build():
    doc = BaseDocTemplate(OUT, pagesize=letter,
                          leftMargin=0.75 * inch, rightMargin=0.75 * inch,
                          topMargin=0.7 * inch, bottomMargin=0.7 * inch,
                          title="Group08_TestCases.pdf",
                          author="Group 8 - Fundamentals of Software Engineering")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")

    def footer(canvas, d):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.grey)
        canvas.drawString(0.75 * inch, 0.45 * inch,
                          "Assignment 3 - Sprint 1 - Group 8 - UC01")
        canvas.drawRightString(letter[0] - 0.75 * inch, 0.45 * inch,
                               f"Page {canvas.getPageNumber()}")
        canvas.restoreState()

    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=footer)])

    story = []
    story.append(Paragraph(
        "FUNDAMENTALS OF SOFTWARE ENGINEERING | GROUP PROJECT", CENTER))
    story.append(Paragraph(
        "Assignment 3 - Sprint 1: Test Planning + Implementation", H1))
    story.append(Spacer(1, 6))
    story.append(Paragraph("Page 1 - Team and Use Case Information", H2))
    story.append(info_table())

    story.append(Spacer(1, 14))
    story.append(Paragraph("Activity B - Implementation Task Breakdown", H2))
    story.append(Paragraph(
        "The selected use case was divided into five tasks along the lines of "
        "data handling, back-end logic, interface work and integration, and "
        "assigned across the team before coding started.", BODY))
    story.append(Spacer(1, 4))
    story.append(tasks_table())
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "<b>Developer checks before test execution:</b> flutter analyze reported "
        "no issues and the TC-01..TC-04 suite was executed with flutter test "
        "(results on the last page).", SMALL))

    story.append(PageBreak())
    story.append(Paragraph("Page 2 - Test Cases (UC01 - Select a suggested destination)", H2))
    story.append(Paragraph(
        "Four test cases planned before implementation. Together they cover a "
        "positive basic path, a positive alternative path with equivalence-class "
        "filtering, a negative exception path, and boundary values of the "
        "destination input length.", BODY))
    for tc in TEST_CASES:
        story.append(Spacer(1, 10))
        story.append(KeepTogether([Paragraph(f"Test Case - {tc['id']}", H3),
                                   test_case_table(tc)]))

    story.append(PageBreak())
    story.append(Paragraph("Activity C - Test Execution Results", H2))
    story.append(Paragraph(
        "The four planned test cases were executed against the implemented "
        "UC01 build. Expected results were taken from Page 2 unchanged; each "
        "test was compared against the observed behavior of the system.", BODY))
    story.append(Spacer(1, 6))
    story.append(results_table())
    story.append(Spacer(1, 16))
    story.append(Paragraph("Test Execution Video", H2))
    story.append(Paragraph(
        "4-minute demonstration of UC01 executed against the planned test "
        "cases TC-01..TC-04:", BODY))
    story.append(Spacer(1, 4))
    story.append(Paragraph(f"<b>{VIDEO_URL}</b>", ParagraphStyle(
        "URL", parent=BODY, textColor=colors.HexColor("#003F88"))))

    doc.build(story)
    print("wrote", OUT)


if __name__ == "__main__":
    build()
