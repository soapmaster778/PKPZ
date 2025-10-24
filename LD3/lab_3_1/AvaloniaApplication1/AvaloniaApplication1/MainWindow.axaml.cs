using Avalonia.Controls;
using System;

using System.Linq;
namespace AvaloniaApplication1;

public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();
    }

    private void CountButton_Click(object? sender, Avalonia.Interactivity.RoutedEventArgs e)
    {
        string input = InputTextBox.Text ?? string.Empty;
        
        string lowerInput = input.ToLower();
        
        int countR = lowerInput.Count(c => c == 'r');
        int countK = lowerInput.Count(c => c == 'k');
        int countT = lowerInput.Count(c => c == 't');

      
        string result =
            $"Кількість 'r': {countR}\n" +
            $"Кількість 'k': {countK}\n" +
            $"Кількість 't': {countT}";
        
        ResultTextBlock.Text = result;
    }
}