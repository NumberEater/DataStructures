#include <iostream>
#include <Windows.h>

int main()
{
  std::cout << "Are you sure you want to start?" << std::endl;
  char answer;
  std::cin >> answer;

  if (answer == 'y') {
    if (system("start ./ex/Main.py") != 0) {
      MessageBox(NULL, "Could not find ./ex/Main.py\nError Code: 0x00000001", "Exception!", NULL);
    }
    return 0;
  } else {
    return -1;
  }
}