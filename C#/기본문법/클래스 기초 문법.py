using System;

public class Program()
{
    public int ad = 123; 

    static void Main()
    {
        sayhello();
        shauting();
        Abc();

    }
    static void sayhello()
    {
        Console.WriteLine("Hello World!");
    }
    
    static void shauting()
    {
        Console.WriteLine("HELLO WORLD!!!");
    }

    static void Abc()
    {
        Process pro = new Process();
        pro.la2();
        pro.inas(12,"ada");

    }

}

public class Process()
{
    
        
    public void la2()
    {
        Console.WriteLine("This is a method in the process class.");
    }

    public void inas(int a, string b)
    {
        Console.WriteLine($"The integer is: {a} and the string is: {b}");
    }


}
