class Program
{
    static void Main()
    {
        Console.OutputEncoding = System.Text.Encoding.UTF8;
        Console.InputEncoding = System.Text.Encoding.UTF8;

        Console.WriteLine("Введіть R: ");
        double R = Convert.ToDouble(Console.ReadLine());

        Console.WriteLine("Введіть x: ");
        double x = Convert.ToDouble(Console.ReadLine());

        Console.WriteLine("Введіть y: ");
        double y = Convert.ToDouble(Console.ReadLine());

        string result = CheckPoint(x, y, R);
        Console.WriteLine("Результат: " + result);
    }

    static string CheckPoint(double x, double y, double R)
    {
        if (x <= 0 && y >= 0)
        {
            double dist2 = x * x + y * y;
            if (dist2 == R * R || x == 0 || y == 0)
                return "На межі";
            if (dist2 < R * R)
                return "Так";
        }
        
        if (x >= 0 && y <= 0)
        {
            if (PointInTriangle(x, y, 0, 0, R, 0, R / 2, -R, out bool onBorder))
            {
                if (onBorder)
                    return "На межі";
                return "Так";
            }
        }

        return "Ні";
    }
    
    static bool PointInTriangle(double px, double py,
                                double x1, double y1,
                                double x2, double y2,
                                double x3, double y3,
                                out bool onBorder)
    {
        double area = Math.Abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0);
        double area1 = Math.Abs((px * (y2 - y3) + x2 * (y3 - py) + x3 * (py - y2)) / 2.0);
        double area2 = Math.Abs((x1 * (py - y3) + px * (y3 - y1) + x3 * (y1 - py)) / 2.0);
        double area3 = Math.Abs((x1 * (y2 - py) + x2 * (py - y1) + px * (y1 - y2)) / 2.0);

        double sum = area1 + area2 + area3;
        onBorder = (sum == area) && (area1 == 0 || area2 == 0 || area3 == 0);

        return sum == area;
    }
}
