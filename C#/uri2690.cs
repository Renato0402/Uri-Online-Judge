using System;
using System.Collections.Generic;
class URI
{

    static void Main(string[] args)
    {

        var lista = new List<Tuple<int, string>>();
        lista.Add(new Tuple<int, string>(0, "GQaku"));
        lista.Add(new Tuple<int, string>(1, "ISblv"));
        lista.Add(new Tuple<int, string>(2, "EOYcmw"));
        lista.Add(new Tuple<int, string>(3, "FPZdnx"));
        lista.Add(new Tuple<int, string>(4, "JTeoy"));
        lista.Add(new Tuple<int, string>(5, "DNXfpz"));
        lista.Add(new Tuple<int, string>(6, "AKUgq"));
        lista.Add(new Tuple<int, string>(7, "CMWhr"));
        lista.Add(new Tuple<int, string>(8, "BLVis"));
        lista.Add(new Tuple<int, string>(9, "HRjt"));

        string input = Console.ReadLine();
        for (int i = 0; i < Convert.ToInt32(input); i++)
        {
            string aux = "";
            string s = Console.ReadLine();
            for (int j = 0; j < s.Length; j++)
            {
                if (aux.Length >= 12) break;

                for (int k = 0; k < 10; k++)
                {
                    string s1 = s[j].ToString();
                    if (lista[k].Item2.Contains(s1))
                    {
                        aux += lista[k].Item1.ToString();
                        continue;
                    }
                }
            }

            Console.WriteLine(aux);

        }

    }

}