#include <iostream>
#include <cstring>
using namespace std;

int findStr(char * line, char * s) {
    char *p;
    int k = 0;
    p = line;
    while(p = strstr(p, s)) {
        p = p + strlen(s);
        k++;
    }
    return k;
}

int main(){
    char line[1000], s[10];
    cout << "Enter your String: " ;
    cin.getline(line, 1000);
    cout << "Enter your SubString: ";
    cin.getline(s, 10);

    cout << findStr(line, s);

    return 0;
}
