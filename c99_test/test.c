#include <stdio.h>
#include <string.h>

int main(void){
    char first = 'a';
    char second = 'c';
    printf("%d\n", second-first);
    char str1[10] = "bcd";
    printf("%d\n", str1[0]-'a');
    printf("sizeof str is %lu\n", sizeof(str1));
    printf("second alphabet is %c and ASCII code is %d\n", first+1, first+1);

    int alphabet[27] = {0};
    for (int i=0; i<27; i++){
        printf("%d ", alphabet[i]);
    }
    printf("\nSize of alphabet int array is %lu\n", sizeof(alphabet)/4);

    char str[100];
    printf("\n\nfgets example. Insert sentence : ");
    fgets(str, sizeof(str), stdin);
    printf("\nBefore strcspn : %s", str);
    printf("\nstrcspn index pos : %d", strcspn(str, "\n"));
    str[strcspn(str, "\n")] = '\0';
    printf("\nAfter doing strcspn : %s", str);

    return 0;
}