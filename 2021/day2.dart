import 'dart:io';

void main() {
  var instructions = File('input/input_day2').readAsLinesSync();
  print(partOne(instructions));
}

int partOne(List<String> instructions) {
  var x = 0, y = 0;
  for (String instruction in instructions) {
    var temp = instruction.split(" ");
    switch (temp[0]) {
      case 'forward':
        x += int.parse(temp[1]);
        break;
      case 'up':
        y -= int.parse(temp[1]);
        break;
      case 'down':
        y += int.parse(temp[1]);
        break;
    }
  }
  return x * y;
}
