using System;

class URI
{

    static void Main(string[] args)
    {

        int[] arr = new int[10];
        for (int i = 0; i < 10; i++)
        {
            int m = Convert.ToInt32(Console.ReadLine());
            if (m <= 0) arr[i] = 1;
            else arr[i] = m;
            Console.WriteLine("X[{0}] = " + arr[i], i);
        }


    }

}