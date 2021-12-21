import 'dart:io';

void main() {
  var file = File('input/input_day1').readAsLinesSync();
  List<int> input = file.map(int.parse).toList();
  print("Part one: ${partOne(input)}");
  print("Part two: ${partTwo(input)}");
}

int partOne(List<int> input) {
  var numberOfIncreases = 0;
  for (var i = 0; i < input.length - 1; i++) {
    if (input[i + 1] > input[i]) {
      numberOfIncreases++;
    }
  }
  return numberOfIncreases;
}

int partTwo(input) {
  int numberOfIncreases = 0;
  for (int i = 0; i < input.length - 3; i++) {
    var currentWindow = input[i] + input[i + 1] + input[i + 2];
    var nextWindow = input[i + 1] + input[i + 2] + input[i + 3];
    if (nextWindow > currentWindow) {
      numberOfIncreases++;
    }
  }
  return numberOfIncreases;
}
