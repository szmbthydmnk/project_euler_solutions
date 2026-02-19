#include <iostream>
#include <string>
#include <vector>

int digit_at(int n) {
    int digits_per_number = 1;
    int count = 9;
    while (n > digits_per_number * count) {
        n -= digits_per_number * count;
        digits_per_number++;
        count *= 10;
    }
    n -= 1; // zero-based index within this digit block
    int start_num = 1;
    for (int i = 1; i < digits_per_number; ++i) {
        start_num *= 10;
    }
    int num = start_num + n / digits_per_number;
    int digit_pos = n % digits_per_number;

    std::string s = std::to_string(num);
    return s[digit_pos] - '0'; // convert char digit to int
}

int clever_champernowne() {
    std::vector<int> indices = {1, 10, 100, 1000, 10000, 100000, 1000000};
    int product = 1;
    for (int idx : indices) {
        product *= digit_at(idx);
    }
    return product;
}

int main() {
    std::cout << "Product of digits: " << clever_champernowne() << std::endl;
    return 0;
}