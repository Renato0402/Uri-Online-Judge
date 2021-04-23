using System;

class URI
{

    static void Main(string[] args)
    {
        int q = 0;
        for (int i = 0; i < 5; i++)
        {
            if (Convert.ToInt32(Console.ReadLine()) % 2 == 0) q++;
        }

        Console.WriteLine("{0} valores pares", q);

    }

}