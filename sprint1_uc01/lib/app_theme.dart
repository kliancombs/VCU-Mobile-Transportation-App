import 'package:flutter/material.dart';

/// Black and gold (VCU Rams) theme used across the app.
class VcuTheme {
  VcuTheme._();

  /// VCU black.
  static const Color black = Color(0xFF000000);

  /// VCU gold - the "orange" accent of the theme.
  static const Color gold = Color(0xFFF8B133);

  /// Slightly raised surfaces (cards, text fields) on the black background.
  static const Color surface = Color(0xFF151515);

  static const Color outline = Color(0xFF3A3A3A);

  static ThemeData get theme => ThemeData(
        useMaterial3: true,
        brightness: Brightness.dark,
        scaffoldBackgroundColor: black,
        colorScheme: const ColorScheme.dark(
          primary: gold,
          onPrimary: black,
          secondary: gold,
          onSecondary: black,
          surface: surface,
          onSurface: Colors.white,
          error: Color(0xFFFF6B6B),
          onError: black,
        ),
        appBarTheme: const AppBarTheme(
          backgroundColor: black,
          foregroundColor: gold,
          elevation: 0,
          centerTitle: true,
          titleTextStyle: TextStyle(
            color: gold,
            fontSize: 20,
            fontWeight: FontWeight.w800,
            letterSpacing: 1.2,
          ),
        ),
        elevatedButtonTheme: ElevatedButtonThemeData(
          style: ElevatedButton.styleFrom(
            backgroundColor: gold,
            foregroundColor: black,
            minimumSize: const Size.fromHeight(52),
            textStyle:
                const TextStyle(fontSize: 16, fontWeight: FontWeight.w700),
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(10),
            ),
          ),
        ),
        inputDecorationTheme: InputDecorationTheme(
          filled: true,
          fillColor: surface,
          labelStyle: const TextStyle(color: gold),
          hintStyle: const TextStyle(color: Colors.white70),
          prefixIconColor: gold,
          suffixIconColor: gold,
          counterStyle: const TextStyle(color: gold),
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular(10),
            borderSide: const BorderSide(color: outline),
          ),
          enabledBorder: OutlineInputBorder(
            borderRadius: BorderRadius.circular(10),
            borderSide: const BorderSide(color: gold, width: 1.5),
          ),
          focusedBorder: OutlineInputBorder(
            borderRadius: BorderRadius.circular(10),
            borderSide: const BorderSide(color: gold, width: 2.5),
          ),
        ),
        listTileTheme: const ListTileThemeData(
          textColor: Colors.white,
          iconColor: gold,
        ),
        dividerTheme: const DividerThemeData(color: outline),
        textTheme: ThemeData.dark()
            .textTheme
            .apply(bodyColor: Colors.white, displayColor: Colors.white),
      );
}
