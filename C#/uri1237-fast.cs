using System;

class URI
{

    static void Main(string[] args)
    {


        int x1 = 0;

        string s1;
        while ((s1 = Console.ReadLine()) != null)
        {
            //string s1 = Console.ReadLine();
            string s2 = Console.ReadLine();
            int[,] dp = new int[2, s2.Length + 1];

            for (int i = 1; i <= s1.Length; i++)
            {

                for (int j = 1; j <= s2.Length; j++)
                {
                    if (s1[i - 1] == s2[j - 1])
                    {
                        dp[i % 2, j] = dp[(i - 1) % 2, j - 1] + 1;
                        if (dp[i % 2, j] > x1) x1 = dp[i % 2, j];
                    }
                    else
                    {
                        dp[i % 2, j] = 0;
                    }
                }
            }
            Console.WriteLine(x1);
            x1 = 0;
        }

    }

}