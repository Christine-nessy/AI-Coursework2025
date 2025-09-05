
// you can use libraries, for example:
// import 'dart:math'
// you can write to stdout for debugging purposes, e.g.
// print("this is a debug message");

int solution(int N) {
    // Implement your solution here
    while(N > 0 && (N & 1) == 0){
     N >>= 1; 
    }
    int maxGap = 0;
    int current = 0;
    //now everytime we see a 1 we close a gap; zeros extend the current gap
    while (N >0){
        if ((N & 1)== 0){
            current++;
        }else{
            if(current > maxGap) maxGap = current;
            current = 0;
        }
        N >>= 1;
    }
    return maxGap;
}
void main(){
    print(solution(9));//2
    print(solution(529));//4
    print(solution(20));//1
    print(solution(15));//0
    print(solution(32));//0
    print(solution(1041));//5

}