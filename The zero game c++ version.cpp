//Shereen Hassan Mohamed
//ID:20170130
//the game number zero: 21 coins game



#include <iostream>

using namespace std;

int main()
{
    int p1,p2,n=21;
    while (n<=21){
        cout<<"Player one play: "<<endl;
        cin>>p1;
        while(p1<1 || p1>3){
                cout<<"Error, please enter a number between 1 and 3: "<<endl;
                cin>>p1;
        }
        if(p1>=1 && p1<=3){
            n=n-p1;
            cout<<"n="<<n<<endl;
            if(n==1){
            cout<<"Player one WINS!";
            break;
            }
        }

        cout<<"Player two play: ";
        cin>>p2;
        while(p2<1 || p2>3){
                cout<<"Error, please enter a number between 1 and 3: "<<endl;
                cin>>p2;
        }
        if(p2>=1 && p2<=3){
            n=n-p2;
            cout<<"n="<<n<<endl;
            if(n==1){
            cout<<"Player two WINS!";
            break;
            }
        }



    }
    return 0;
}
