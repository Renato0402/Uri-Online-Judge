using System;
using System.Globalization;
class URI
{

    static void Main(string[] args)
    {

        string[] input = Console.ReadLine().Split(' ');
        double a1 = double.Parse(input[0], CultureInfo.InvariantCulture);
        double an = double.Parse(input[1], CultureInfo.InvariantCulture);
        double n = an - a1 + 1;
        double soma = ((a1 + an) * n) / 2;

        Console.WriteLine(Convert.ToInt64(soma));
    }

}