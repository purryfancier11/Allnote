using System;

class Program
{
    static void Main()
    {
        // 내 정보 저장해보기
        string name = "김진찬";
        int age = 216 - 20;
        double height = 175.5;
        bool isStudent = true;

        Console.WriteLine("이름: " + name);
        Console.WriteLine("나이: " + age);
        Console.WriteLine("학생인가요? " + isStudent);

        // 사칙연산 연습
        int a = 10;
        int b = 3;
        Console.WriteLine("더하기: " + (a + b));
        Console.WriteLine("나누기 하면 소수점 잘림 : " + (a / b));
    }
}
