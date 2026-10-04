#include <iostream>
#include <fstream>

int main() {

    // Image

    int image_width = 256;
    int image_height = 256;

    // Render

    std::cout << "P3\n" << image_width << ' ' << image_height << "\n255\n";

    for (int y = 0; y < image_height; y++) {
        for (int x = 0; x < image_width; x++) {
            double r = x;
            double g = y;
            double b = 0.0;

            std::cout << r << ' ' << g << ' ' << b << '\n';
        }
    }
}
