using System;

class URI
{

    static void Main(string[] args)
    {

        int aux = 0;
        string input = Console.ReadLine();
        for (int i = 0; i < Convert.ToInt32(input); i++)
        {
            double x = Convert.ToDouble(Console.ReadLine());
            if (x == 2)
            {
                Console.WriteLine("Prime");
                aux = 0;
            }
            else
            {
                if (x % 2 == 0)
                {
                    Console.WriteLine("Not Prime");
                    aux = 0;
                }
                else
                {
                    for (int j = 3; j <= Math.Sqrt(x); j += 2)
                    {
                        if (x % j == 0) aux++;
                        if (aux >= 1)
                        {
                            Console.WriteLine("Not Prime");

                            break;
                        }
                    }

                    if (aux == 0)
                    {

                        Console.WriteLine("Prime");

                    }

                    aux = 0;

                }
            }
        }

    }

}