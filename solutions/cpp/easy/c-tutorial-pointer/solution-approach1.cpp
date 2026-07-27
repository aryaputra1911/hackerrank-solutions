// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/challenges/c-tutorial-pointer/problem?isFullScreen=true
// Problem     Pointer
// Difficulty  Easy
// Subdomain   Introduction
// Platform    HackerRank
// Language    cpp
// Status      Accepted
// Submitted   2026-07-27, 11:00 a.m.
// ──────────────────────────────────────────────────

#include <stdio.h>

void update(int *a,int *b) {
    // Complete this function 
    int a_p =*a;
    int b_p = *b;
    *a = a_p + b_p;
    *b = (a_p - b_p);
    if(*b <0){
        *b = -*b;
    }    
       
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
