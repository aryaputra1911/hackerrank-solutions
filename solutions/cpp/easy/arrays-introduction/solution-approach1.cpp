// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/challenges/arrays-introduction/problem?isFullScreen=true
// Problem     Arrays Introduction
// Difficulty  Easy
// Subdomain   Introduction
// Platform    HackerRank
// Language    cpp
// Status      Accepted
// Submitted   2026-07-27, 06:42 p.m.
// ──────────────────────────────────────────────────

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    int arr[10000];
    cin >> n;
    for(int i = 0; i <= 10000; i++){
        cin >> arr[i];
    }
    std :: reverse(arr, arr+n);
    
    for(int i=0; i < n ; i++){
        cout<<arr[i]<<" ";
    }
    
    return 0;
}
