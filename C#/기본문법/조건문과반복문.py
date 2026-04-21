using System;

class Program
{
    static void Main()
    {
        // 홀짝 구분기
        Console.Write("숫자 아무거나 입력: ");
        int num = int.Parse(Console.ReadLine());

        if (num % 2 == 0)
        {
            Console.WriteLine("짝수");
        }
        else
        {
            Console.WriteLine("홀수");
        }

        // 1부터 5까지 출력 (for문 연습)
        Console.WriteLine("5번 반복");
        for (int i = 1; i <= 5; i++)
        {
            Console.WriteLine(i);
        }
    }
}
