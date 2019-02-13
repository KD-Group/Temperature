#include <iostream>
#include <string>

#include "temp.h"

int main(int argc, char** argv) {
	std::string cmd;
	while (std::cin >> cmd) {
		if (cmd == "get_temp") {
			std::cout << "temperature" << " = " << get_temp() << std::endl;
			std::cout << "EOF" << std::endl;
		}
	}
	return 0;
}