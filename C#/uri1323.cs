using System;

class URI
{

    static void Main(string[] args)
    {
        string input;
        double answer = 0;
        while ((input = Console.ReadLine()) != "0" && input != "")
        {
            int number = Convert.ToInt32(input);

            for (int i = number; i >= 1; i--)
            {
                answer += Math.Pow(i, 2);
            }

            Console.WriteLine(answer);
            answer = 0;
        }
    }

}