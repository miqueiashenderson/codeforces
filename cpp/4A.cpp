#include <iostream>

int main(){
	int valor1;

	std::cin >> valor1;

	if (valor1 % 2 == 0 and valor1 > 2) {
		std::cout << "YES" << std::endl;
	}
	else{
		std::cout << "NO" << std::endl;
	}

	return 0;
}

