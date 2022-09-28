#include<stdio.h>
#include<bits/stdc++.h>
using namespace std;
int gcd(int m , int n)
{
    int i = min(m, n);
    int k = max(m, n);    
    int c;

    for(int j =1; j<= i; j++)
    {
        if(k%j == 0 && i%j==0 )
        {
            c=j;
        }
    }
    return c;
}

int totient(int m)
{

    if(m ==1 or m==2)
        return 1;
    int count = 0;
    for(int i=1; i<m; i++)
    {
        if(gcd(m, i) ==  1)
            count++;
    }
    return count;
}

vector<int> revT(int &c)
{
    cout<<"Your expected numbers are"<<endl;
    vector<int> a;
    if(c == 1)
    {
        a.push_back(1);
        a.push_back(2);
        return a;
    }

    for(int i = 3; i<c*5 ; i++)
    {
        if(totient(i)== c)
            {a.push_back(i);
              cout<<i<<endl;
            }
    }

    return a;
}
int main(){
    
    // cout<<gcd(8,4);
    // cout<<totient(4);
    int h;
    cout<<"Enter your Number"<<endl;
    cin>>h;
    revT(h);

    // vector<int>
    return 0;
}