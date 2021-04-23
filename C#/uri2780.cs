using System;

class URI
{

    static void Main(string[] args)
    {

        int d = Convert.ToInt32(Console.ReadLine());

        if (d <= 800) Console.WriteLine("1");
        if (d > 800 && d <= 1400) Console.WriteLine("2");
        if (d > 1400 && d <= 2000) Console.WriteLine("3");

    }

}