#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int letter_count (string text);
int main(void)
{


//take user input
string text = get_string("The sentence is: ");












return 0;
}

int letter_count (char *text)
{
int letters = 0;
for (int i = 0; i < strlen(text); i++ )
{
    if (isalpha(text[i]))
    {
        letters++;
    }

}
printf("%i letters", letters);
return letters;
}