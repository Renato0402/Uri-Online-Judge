using System;

class URI
{

    static void Main(string[] args)
    {

        string input;


        while ((input = Console.ReadLine()) != null)
        {
            string[] numbers = input.Split(' ');
            string d = numbers[0];
            char[] n = numbers[1].ToCharArray();
            string aux = "";


            if (d[0] == '0' && n[0] == '0') break;

            for (int i = 0; i < n.Length; i++)
            {

                if (n[i] != d[0])
                {
                    aux += n[i];

                }
            }


            if (aux == "") Console.WriteLine(0);
            else
            {
                Console.WriteLine(aux.TrimStart('0').PadLeft(1, '0'));
            }

        }
    }

}