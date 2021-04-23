using System;

class URI
{

    static void Main(string[] args)
    {

        string input;
        while ((input = Console.ReadLine()) != null)

        {
            string x = input.Split(' ')[0];
            string y = input.Split(' ')[1];
            if (x == y) break;
            if (Convert.ToInt32(x) < Convert.ToInt32(y)) Console.WriteLine("Crescente");
            if (Convert.ToInt32(x) > Convert.ToInt32(y)) Console.WriteLine("Decrescente");
        }

    }

}