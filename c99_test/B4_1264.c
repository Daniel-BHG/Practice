#include <stdio.h>
#include <string.h>
#include <ctype.h>

/*
get the line until meeting '\n'
count the vowel
print the num of vowel
get the line ...
if encounter '#', quit
*/
    

int main(void) {
    char str[256];

    while (1) {
        int cnt = 0;

        // fgets(str, sizeof(str), stdin);
        // str[strcspn(str, "\r\n")] = '\0';
        gets(str);

        if (strcmp(str, "#") == 0)
            break;
        // count the vowel
        // printf("result: %d\n", count_vowel(str));
        
        for (int i=0; str[i] != '\0'; i++) {
            if (str[i] == 'a' || str[i] == 'A')
                cnt++;
            else if (str[i] == 'e' || str[i] == 'E')
                cnt++;
            else if (str[i] == 'i' || str[i] == 'I')
                cnt++;
            else if (str[i] == 'o' || str[i] == 'O')
                cnt++;
            else if (str[i] == 'u' || str[i] == 'U')
                cnt++;
        }
        printf("%d\n", cnt);
    }

    return 0;
}