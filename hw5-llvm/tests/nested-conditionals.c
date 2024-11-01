#include <stdio.h>
#include <math.h>

int main() {
    float a = 3.7, b = 2.5, result = 0.0;

    if (a > b) {
        result = pow(a, 2) - sqrt(b);
    } else {
        result = log(a + b) * sin(a);
    }

    if (result > 5.0) {
        result /= 2.0;
    } else if (result < -5.0) {
        result *= -1.0;
    } else {
        result += 1.5;
    }

    printf("Final result: %f\n", result);
    return 0;
}
