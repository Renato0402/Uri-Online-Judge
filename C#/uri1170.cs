using System;
using System.Globalization;
class URI
{

    static void Main(string[] args)
    {

        string input = Console.ReadLine();
        int days = 0;
        for (int i = 0; i < Convert.ToInt32(input); i++)
        {
            double kg = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
            while (kg > 1)
            {
                kg = kg / 2;
                days++;
            }

            Console.WriteLine("{0} dias", days);
            days = 0;
        }

    }

}