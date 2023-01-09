#include <iostream>
#include <fstream>
#include <ctime>
#include <string>

using namespace std;

int main(){
    srand(time(0));
    float p =1, p1;
    int n = 100;
    string ns, ps;
    ofstream fout1, fout2;
    ifstream fin;
    fout1.open("nodes.txt");
    fout2.open("edges.txt");
    fin.open("data.txt");
    getline(fin, ns);
    n = stoi(ns);
    getline(fin, ps);
    p = stof(ps);
    for (int i=0; i< n; i++){
        fout1 << i;
        if(i!= (n-1))
            fout1 << '\n';
    }
    for (int i=0; i<n; i++){
        for (int j = i+1; j<n; j++){
            p1 = ((float)(rand()%1000))/1000;
            if (p1<=p){
                fout2<<i<<" "<<j<<'\n';
            }
        }
    }
    fin.close();
    fout1.close();
    fout2.close();
    return 0;
}
