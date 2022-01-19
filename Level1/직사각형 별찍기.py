a, b = map(int, input().strip().split(' '))#a와 b의 값을 받아줌
answer = ("*"*a+"\n")*b
print(answer)
#자바파일을 못만들어서 올려 놓는 자바
'''
import java.util.Scanner;
class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        for(int i=0; i<b; i++){
            for(int j=0; j<a; j++){
                System.out.print("*");
            }
            System.out.println("");
        }
    }
}'''