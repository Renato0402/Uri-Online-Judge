using System;

class URI
{

    static void Main(string[] args)
    {

        string input;
        while ((input = Console.ReadLine()) != null)
        {
            string[] numbers = input.Split(' ');
            int A = Convert.ToInt32(numbers[0]);
            int B = Convert.ToInt32(numbers[1]);
            int C = Convert.ToInt32(numbers[2]);
            int D = Convert.ToInt32(numbers[3]);

            if (B > C && D > A && (C + D) > (A + B) && C > 0 && D > 0 && A % 2 == 0)
            {
                Console.WriteLine("Valores aceitos");
            }
            else
            {
                Console.WriteLine("Valores nao aceitos");
            }
        }
    }

}