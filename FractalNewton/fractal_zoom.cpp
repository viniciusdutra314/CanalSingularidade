#include "./matplotlib-cpp/matplotlibcpp.h"
#include <complex>
#include <vector>
using namespace std;
namespace plt = matplotlibcpp;

complex<float> polinomio(complex<float> z) {
    return pow(z,3)- float(1);  
}

complex<float> derivada(complex<float> z) {
    return float(3)*pow(z,2); 
}

int main() {
    float epsilon = 1e-3;
    int max_int = 100;
    float N=2e3;
    float scale_rate=1.1;
    vector<float> matriz(int(N) * int(N));
    for (int k=0; k<20;k++){
        float x_min=-1/(pow(scale_rate,k)), x_max=1/(pow(scale_rate,k));
        float y_min=-1/(pow(scale_rate,k)), y_max=1/(pow(scale_rate,k));
        for (int i=0;i<N;i++){
            for (int j=0;j<N;j++){
                int iterations = 0;
                complex<float> x0((x_max-x_min)*(i/N)+x_min, (j/N)*(y_max-y_min)+y_min);
                while (iterations < max_int) {
                    complex<float> newton_step = polinomio(x0) / derivada(x0);
                    if (abs(newton_step) < epsilon) {break;}
                    iterations += 1;
                    x0 = x0 - newton_step;}       
                matriz.at(int(N)*j +i)=float(x0.imag());}}
        plt::imshow(&(matriz[0]),int(N),int(N),1);
        plt::save("fractal"+to_string(k)+".png",1200);}

    }


