using System;

class URI
{

    static void Main(string[] args)
    {
        int entrada = Convert.ToInt32(Console.ReadLine());

        for (int i = 0; i < entrada; i++)
        {
            string input2 = Console.ReadLine();
            string[] numero = input2.Split(' ');

            int x = Convert.ToInt32(numero[0]);
            int y = Convert.ToInt32(numero[1]);

            var rafael = Math.Pow((3 * x), 2) + Math.Pow(y, 2);
            var beto = 2 * Math.Pow(x, 2) + Math.Pow(5 * y, 2);
            var carlos = -100 * x + (Math.Pow(y, 3));

            if (rafael > carlos && rafael > beto)
            {
                Console.WriteLine("Rafael ganhou");
            }
            else if (carlos > rafael && carlos > beto)
            {
                Console.WriteLine("Carlos ganhou");
            }
            else
            {
                Console.WriteLine("Beto ganhou");
            }
        }


    }

}