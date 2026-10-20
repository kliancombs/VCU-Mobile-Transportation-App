import 'package:flutter/material.dart';

import 'app_theme.dart';
import 'screens/home_screen.dart';

void main() => runApp(const VcuParkingApp());

/// VCU Parking Finder - Sprint 1 build.
///
/// This build implements UC01 "Select a suggested destination" (FR02),
/// the use case selected for Assignment 3 - Sprint 1.
class VcuParkingApp extends StatelessWidget {
  const VcuParkingApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'VCU Parking Finder',
      debugShowCheckedModeBanner: false,
      theme: VcuTheme.theme,
      home: const HomeScreen(),
    );
  }
}
