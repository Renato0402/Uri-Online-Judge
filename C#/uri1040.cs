using System;
using System.Globalization;
class URI
{

    static void Main(string[] args)
    {

        string[] input = Console.ReadLine().Split(' ');
        string exame;



        double n1 = double.Parse(input[0], CultureInfo.InvariantCulture);
        double n2 = double.Parse(input[1], CultureInfo.InvariantCulture);
        double n3 = double.Parse(input[2], CultureInfo.InvariantCulture);
        double n4 = double.Parse(input[3], CultureInfo.InvariantCulture);


        double media = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10;

        if (Math.Round(media, 1, MidpointRounding.ToEven).ToString(CultureInfo.InvariantCulture).Length == 1)
            Console.WriteLine("Media: {0}.0", Math.Round(media, 1, MidpointRounding.ToEven).ToString(CultureInfo.InvariantCulture));
        else
        {
            Console.WriteLine("Media: {0}", Math.Round(media, 1, MidpointRounding.ToEven).ToString(CultureInfo.InvariantCulture));
        }

        if (media >= 7)
        {
            Console.WriteLine("Aluno aprovado.");

        }
        else if (media < 5)
        {
            Console.WriteLine("Aluno reprovado.");

        }
        else
        {

            Console.WriteLine("Aluno em exame.");
            double n5 = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
            media = (n5 + media) / 2;

            if (n5.ToString(CultureInfo.InvariantCulture).Length == 1)
                Console.WriteLine("Nota do exame: {0}.0", n5.ToString(CultureInfo.InvariantCulture));
            else
            {
                Console.WriteLine("Nota do exame: {0}", n5.ToString(CultureInfo.InvariantCulture));
            }

            if (media >= 5)
            {
                Console.WriteLine("Aluno aprovado.");
            }
            else
            {
                Console.WriteLine("Aluno reprovado.");
            }

            if (Math.Round(media, 1, MidpointRounding.ToEven).ToString(CultureInfo.InvariantCulture).Length == 1)
                Console.WriteLine("Media final: {0}.0", Math.Round(media, 1, MidpointRounding.ToEven).ToString(CultureInfo.InvariantCulture));
            else
            {
                Console.WriteLine("Media final: {0}", Math.Round(media, 1, MidpointRounding.ToEven).ToString(CultureInfo.InvariantCulture));
            }

        }

    }

}