import "dart:io";

void main() {
  var report = File('input/input_day3').readAsLinesSync();
  print("Part one: ${partOne(report)}");
}

int partOne(List<String> report) {
  //Fill list with zeros
  List<int> gammaRate = [];
  for (int i = 0; i < report[0].length; i++) {
    gammaRate.add(0);
  }

  //Count number of 1 bits per position
  for (String line in report) {
    List<String> bits = line.split('');
    for (int i = 0; i < bits.length; i++) {
      gammaRate[i] += int.parse(bits[i]);
    }
  }

  List<int> epsilonRate = [];

  //Format gamma and epsilon rate
  for (int i = 0; i < gammaRate.length; i++) {
    if (gammaRate[i] > (report.length / 2)) {
      gammaRate[i] = 1;
      epsilonRate.add(0);
    } else {
      gammaRate[i] = 0;
      epsilonRate.add(1);
    }
  }

  int bitListToInt(List<int> binaryList) {
    String binaryString = "";
    for (int bit in binaryList) {
      binaryString += bit.toString();
    }
    return int.parse(binaryString, radix: 2);
  }

  return bitListToInt(gammaRate) * bitListToInt(epsilonRate);
}
