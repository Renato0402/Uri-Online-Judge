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


            for (int i = 0; i < s2.Length; i++)
            {

                for (int j = s2.Length - i; j > 0; j--)
                {
                    if (s1.Contains(s2.Substring(i, j)))
                    {
                        if (x1 < s2.Substring(i, j).Length)
                        {
                            x1 = s2.Substring(i, j).Length;
                        }
                    }
                }
            }
            Console.WriteLine(x1);
            x1 = 0;
        }

    }

}