#include <stdio.h>
#include <string.h>

int main(void) {
    int num;
    scanf("%d", &num);
    // after enter, there're 50\n in the buffer, but scanf only takes 50, so \n is still remaining. Then fgets reads the \n\0 and end the fgets, so need to consume the buffer with getchar
    while (getchar() != '\n');
    for (int i = 0; i < num; i++) {
        printf("String #%d\n", i+1); // String #10
        char str[51];
        fgets(str, sizeof(str), stdin);
        str[strcspn(str, "\n")] = '\0';
        for (int j = 0; j < strlen(str); j++) { // A~Z ASCII 65~90
            str[j] = (str[j] - 'A' + 1) % 26 + 'A'; // convert to +1 ASCII
        }
        printf("%s\n\n", str);
    }
    
    return 0;
}

/*
input
    number of names
    computer names ...
print
    ASCII +1. utilize %c, %d
    if Z, then A
*/