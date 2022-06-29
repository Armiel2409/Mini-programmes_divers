#include <stdio.h>
#include <stdlib.h>
#include <conio.h>


void main()
{
    char lettre='a';
    int compteur = 0;

    printf("CONVERTISSEUR MINUSCULES-MAJUSCULES\nVeuillez rentrer une LETTRE\n");
    lettre = getch();

   do
   {
        if((lettre>=65) && (lettre<=90))
    {
        printf("La lettre que vous avez rentr%c est une majuscule.\n\n",130);
        printf("Sa minuscule est : %c\n\n",lettre+32);
        return(0);
    }
    else if((lettre >=97) && (lettre<=122))
    {
        printf("La lettre que vous avez rentr%c est une minuscule.\n",130);
        printf("Sa majuscule est : %c\n\n",lettre-32);
        return(0);
    }
    else
    {
        printf("Erreur de saisie.Pour sortir du programme : Echap\n");
        lettre=getch();
    }

   }while(lettre!=27);


}
