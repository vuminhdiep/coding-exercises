#include <iostream>
#include<bits/stdc++.h>

using namespace std;

typedef long long VAR;
const int N = 30;
VAR sour[N], bitt[N];
int num;


int main () {

double res;

cin >> num;
for (int i = 0; i < num; i++)
cin >> sour[i] >> bitt[i];
res = 1e200;
for (int j = 1; j < 1 << num; j++)
{
    double S = 1;
    double B = 0;
    for (int k = 0; k < num; k++)
       if ((1 << k) & j) {
       S *= sour[k];
       B += bitt[k];
       }
    res = min (res, fabs (S - B));
}

cout << (round (res)) << endl;

return 0;
}
