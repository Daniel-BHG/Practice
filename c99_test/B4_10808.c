#include <stdio.h>
#include <string.h>

int main(void){
    char str[101];
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\r\n")] = '\0';

    int alphabet[26] = {0};
    for (int i = 0; i < strlen(str); i++) {
        if (str[i] >= 'a' && str[i] <= 'z'){
            alphabet[str[i] - 'a']++;
            // printf("cnt++ the %c to %dth word\n", str[i], str[i]-'a');
        }
    }
    
    for (int j = 0; j < 26; j++) {
        if (j < 26-1)
            printf("%d ", alphabet[j]);
        else
            printf("%d", alphabet[j]);
    }

    return 0;
}

/*
get the string

get the each char
    cnt++ for matching alphabet
*/