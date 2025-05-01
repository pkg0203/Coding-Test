#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// wallpaper_len은 배열 wallpaper의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int* solution(const char** wallpaper, size_t wallpaper_len) {
    int min_x = 50, min_y = 50;
    int max_x = 0, max_y = 0;

    for (int i = 0; i < wallpaper_len; i++) {
        for (int j = 0; wallpaper[i][j]; j++) {
            if (wallpaper[i][j] == '#') {
                if (i < min_x) min_x = i;
                if (j < min_y) min_y = j;
                if (i + 1 > max_x) max_x = i + 1;
                if (j + 1 > max_y) max_y = j + 1;
            }
        }
    }

    int* answer = (int*)malloc(sizeof(int) * 4);
    answer[0] = min_x;
    answer[1] = min_y;
    answer[2] = max_x;
    answer[3] = max_y;
    return answer;
}