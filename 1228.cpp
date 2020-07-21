#include <stdio.h>
#include <stdlib.h>

main()
{

    int x,vet1[24],vet2[24],i=0,k=0,u=0;

    scanf("%d",&x);
    

    for(i=0; i < x; i++)
    {

        scanf("%d",&vet1[i]);

    }


    for(i=0; i < x; i++)
    {

        scanf("%d",&vet2[i]);

    }


    i=0;
    k=0;


    do
    {

        if(vet1[i] != vet2[k] && k != x + 1)
        {
        	
            k++;
        
		}
        else
        {

            if(i < k)
            {

                u = u + (k - i);

            }

            i++;
            k = 0;

        }


    }
    while(i != x);

    printf("%d\n",u);

}

