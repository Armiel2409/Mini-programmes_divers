#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int bcl=0;
    int bclbis = 0;
    int rng=0;
    int entree=0;

    srand(time(NULL));
    rng = ((rand()%101));

    printf("[JEU PLUS OU MOINS] : Nombre entre 0 et 100 g%cn%cr%c. Essayez de le deviner.\n",130,130,130);

    while(entree!=rng)
    {
        bcl++;
        scanf("\n%d",&entree);
        if(entree==rng)
        {
            printf("F%clicitations! Le nombre g%cn%cr%c %ctait bien %d!\n",130,130,130,130,130, rng);
            printf("Nombre de tentatives : %d\n",bcl);

        }

        else if(entree>rng)
        {
            printf("Plus petit\n");
        }

        else
        {
            printf("Plus grand\n");
        }

    }


}
