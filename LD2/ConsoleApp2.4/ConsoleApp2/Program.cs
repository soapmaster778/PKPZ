using System;

//lab 2.4


class Program
{
    static void Main()
    {
        Console.OutputEncoding = System.Text.Encoding.UTF8;
        Console.InputEncoding = System.Text.Encoding.UTF8;
        
        Console.Write("Введіть кількість рядків зубчастого масиву n: ");
        int n = int.Parse(Console.ReadLine());
        
        int[][] jaggedArray = new int[n][];
        Random rand = new Random();
        
        for (int i = 0; i < n; i++)
        {
            Console.Write($"Введіть кількість елементів у рядку {i + 1}: ");
            int m = int.Parse(Console.ReadLine());

            jaggedArray[i] = new int[m];
            for (int j = 0; j < m; j++)
            {
                jaggedArray[i][j] = rand.Next(-50, 50); 
            }
        }
        
        Console.WriteLine("\nЗубчастий масив:");
        for (int i = 0; i < jaggedArray.Length; i++)
        {
            Console.WriteLine($"Рядок {i + 1}: {string.Join(" ", jaggedArray[i])}");
        }
        
        int[] positivesCount = new int[n];

        for (int i = 0; i < n; i++)
        {
            int count = 0;
            foreach (int val in jaggedArray[i])
            {
                if (val > 0) count++;
            }
            positivesCount[i] = count;
        }


        Console.WriteLine("\nКількість додатних елементів у кожному рядку:");
        for (int i = 0; i < n; i++)
        {
            Console.WriteLine($"Рядок {i + 1}: {positivesCount[i]}");
        }
    }
}