using System;

class URI
{

    static void Main(string[] args)
    {

        int input = Convert.ToInt32(Console.ReadLine());
        string m;
        int aux = input;
        int a = 0;
        int qtd = 1;
        if (input < 0) qtd = 2;
        while ((m = Console.ReadLine()) != null)
        {
            if (input < Convert.ToInt32(m))
            {
                a = Convert.ToInt32(m);
                break;
            }

        }

        while (a > input)
        {
            qtd++;
            aux++;
            input = aux + input;

        }

        Console.WriteLine(qtd);

    }

}