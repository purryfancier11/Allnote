using System;

public class Program()
{
    
    public static void Main()
    {
        Console.WriteLine("Hello, World!");
        ADA auu = new ADA();
        auu.Meow();

    }


}
public class Animal()
{
    public void Jump()
    {
        Console.WriteLine("wow");
    }
}

public class Dog : Animal
{
    public void Bac()
    {
        Jump();
        Console.WriteLine("wooa");
    }

    
    
}

public class ADA()
{
    public void Meow()
    {
        Dog adc = new Dog();
        adc.Jump();
        adc.Bac();
    }

}

