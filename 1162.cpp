#include <bits/stdc++.h>
using namespace std;

int bubbleSortSwaps(std::vector<int> q)
{
    int count=0;
    for(size_t i=0; i<q.size(); i++)
    {
        bool swapped = false;
        for (size_t j=0; j<q.size()-i-1; j++)
        {
            if(q[j]>q[j+1])
            {
                swapped = true;
                std::swap(q[j],q[j+1]);
                count++;
            }
        }
        if (!swapped) // if no swap happened, it's sorted
        {
            break;
        }
    }
    return count;
}

int main()
{
    std:: vector<int> arr;

    int i,n,j=0,l,resu,x;

    cin>>n;

    for(j=0; j<n; j++)
    {

        cin>>l;

        for(i=0; i<l; i++)
        {

            cin>>x;
            arr.push_back(x);



        }
        resu = bubbleSortSwaps(arr);

        cout<<"Optimal train swapping takes "<<resu<<" swaps."<<endl;

        arr.clear();

    }
}

