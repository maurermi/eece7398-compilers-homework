#include <stdio.h>

int main()
{
    float a = 1.1, b = 2.2, c = 3.3, d = 4.4, e = 5.5;
    float f = 6.6, g = 7.7, h = 8.8, i = 9.9, j = 10.1;

    float result1 = a * b;
    float result2 = c * d;
    float result3 = e * f;
    float result4 = g * h;
    float result5 = i * j;

    float result6 = a * c;
    float result7 = e * g;
    float result8 = i * a;
    float result9 = b * f;
    float result10 = d * h;

    return 0;
}