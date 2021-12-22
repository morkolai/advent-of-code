import 'dart:io';

void main() {
  var instructions = File('input/input_day2').readAsLinesSync();
  print("Part one: ${partOne(instructions)}");
  print("Part two: ${partTwo(instructions)}");
}

int partOne(List<String> instructions) {
  var x = 0, y = 0;

  for (String instruction in instructions) {
    var text = instruction.split(" ")[0],
        number = int.parse(instruction.split(" ")[1]);

    switch (text) {
      case 'forward':
        x += number;
        break;
      case 'up':
        y -= number;
        break;
      case 'down':
        y += number;
        break;
    }
  }
  return x * y;
}

int partTwo(List<String> instructions) {
  int x = 0, y = 0, aim = 0;

  for (String instruction in instructions) {
    var text = instruction.split(" ")[0],
        number = int.parse(instruction.split(" ")[1]);

    switch (text) {
      case "down":
        aim += number;
        break;
      case "up":
        aim -= number;
        break;
      case "forward":
        x += number;
        y += aim * number;
    }
  }
  return x * y;
}
