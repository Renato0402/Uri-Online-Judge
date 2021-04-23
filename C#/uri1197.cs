using System;

class URI
{

    static void Main(string[] args)
    {
        string input;
        while (((input = Console.ReadLine()) != null && input != ""))
        {

            string[] numbers = input.Split(' ');
            int v = Convert.ToInt32(numbers[0]);
            int t = Convert.ToInt32(numbers[1]);


            Console.WriteLine(v * t * 2);
        }
    }

}