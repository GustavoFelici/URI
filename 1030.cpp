#include <stdio.h>
int josephus(int n, int k, int iniPoint)
{
    if(n == 1)
        return 1;

    int nPoint, sobrevive;

    nPoint = (iniPoint + k - 2) % n + 1;
    sobrevive = josephus(n - 1, k, nPoint);

    if(sobrevive < nPoint)
    {
        return sobrevive;
    }
    else
    {
        return sobrevive + 1;
    }
}



int main()
{
    int nc, n, k, s, i;
    scanf("%i", &nc);

    for (i = 1; i <= nc; ++i)
    {
        scanf("%i %i", &n, &k);
        s = josephus(n, k,1);
        printf("Case %i: %i\n", i, s);
    }

    
}

