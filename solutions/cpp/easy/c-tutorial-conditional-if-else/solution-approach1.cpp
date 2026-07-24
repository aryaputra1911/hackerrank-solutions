// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/challenges/c-tutorial-conditional-if-else/problem?isFullScreen=true
// Problem     Conditional Statements
// Difficulty  Easy
// Subdomain   Introduction
// Platform    HackerRank
// Language    cpp
// Status      Accepted
// Submitted   2026-07-24, 10:45 a.m.
// ──────────────────────────────────────────────────

#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

int main()
{
    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));
    
    // Write your code here
    if(n>=1 && n <=9){
        string nums[] = {"","one", "two", "three","four", "five", "six", "seven", "eight","nine"};
        cout<<nums[n];
    }else{
        cout<<"Greater than 9";
    }
    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
