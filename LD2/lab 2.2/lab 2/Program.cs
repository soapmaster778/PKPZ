using System;
using System.Collections.Generic;

//lab 2.2

class Program
{
    static void Main()
    {
        Console.OutputEncoding = System.Text.Encoding.UTF8;
        Console.InputEncoding = System.Text.Encoding.UTF8;
        
        const int n = 5;
        int[,] A = new int[n, n];
        Random rand = new Random();
        
        Console.WriteLine("Матриця A:");
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                A[i, j] = rand.Next(-50, 50);
                Console.Write($"{A[i, j],4}");
            }
            Console.WriteLine();
        }
        
        Console.Write("\nВведіть число x: ");
        int x = int.Parse(Console.ReadLine());
        
        HashSet<int> rowsToRemove = new HashSet<int>();
        HashSet<int> colsToRemove = new HashSet<int>();

        LinearSearch(A, n, x, rowsToRemove, colsToRemove);
        
        if (rowsToRemove.Count == 0)
        {
            Console.WriteLine("\nЕлемент x не знайдено у матриці.");
            return;
        }
        
        int newRows = n - rowsToRemove.Count;
        int newCols = n - colsToRemove.Count;
        int[,] B = new int[newRows, newCols];

        int bi = 0;
        for (int i = 0; i < n; i++)
        {
            if (rowsToRemove.Contains(i)) continue;
            int bj = 0;
            for (int j = 0; j < n; j++)
            {
                if (colsToRemove.Contains(j)) continue;
                B[bi, bj] = A[i, j];
                bj++;
            }
            bi++;
        }
        
        Console.WriteLine("\nМатриця B після вилучення рядків і стовпців:");
        for (int i = 0; i < newRows; i++)
        {
            for (int j = 0; j < newCols; j++)
            {
                Console.Write($"{B[i, j],4}");
            }
            Console.WriteLine();
        }
    }
    static void LinearSearch(int[,] A, int n, int x, HashSet<int> rows, HashSet<int> cols)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (A[i, j] == x)
                {
                    rows.Add(i);
                    cols.Add(j);
                }
            }
        }
    }
}
