using System;

class URI
{

    static void Main(string[] args)
    {

        string input;

        while ((input = Console.ReadLine()) != null && input != "0")
        {
            int aux = input.Length;
            double soma = 0;
            int aux2 = 0;
            while (aux2 != input.Length)
            {

                int mul = 1;


                for (int i = aux; i >= 1; i--)
                {

                    mul *= i;

                }

                if (aux == 0)
                {
                    mul = 1;
                }


                soma += char.GetNumericValue(input[aux2]) * mul;
                aux--;
                aux2++;
            }


            Console.WriteLine(soma);

        }

    }

}