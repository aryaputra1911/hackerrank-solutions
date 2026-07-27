// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/challenges/c-tutorial-strings/problem?isFullScreen=true
// Problem     Strings
// Difficulty  Easy
// Subdomain   Strings
// Platform    HackerRank
// Language    cpp
// Status      Accepted
// Submitted   2026-07-27, 11:32 a.m.
// ──────────────────────────────────────────────────

#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string a,b;
    cin >> a;
    cin >> b;
    cout<<a.size()<<" "<<b.size()<<endl;
    cout<<a+b<<endl;
    char a0 = b[0];
    char b0= a[0];
    a[0]=a0;
    b[0]=b0;    
    cout << a <<" "<< b;
    return 0;
}
