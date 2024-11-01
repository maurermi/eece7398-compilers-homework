#include <stdio.h>

int main() {
    float x = 1.0, sum = 0.0;
    for (int i = 0; i < 5; i++) {
        sum += x / (i + 1);
        if (sum > 2.0) {
            sum *= 0.5;
        }
        x += 1.0;
    }
    printf("Final sum: %f\n", sum);
    return 0;
}