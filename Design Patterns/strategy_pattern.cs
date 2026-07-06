using System;

// Strategy Interface
public interface IPaymentStrategy
{
    void Pay(decimal amount);
}

// Concrete Strategy 1
public class CreditCardPayment : IPaymentStrategy
{
    public void Pay(decimal amount)
    {
        Console.WriteLine($"Paid ${amount} using Credit Card");
    }
}

// Concrete Strategy 2
public class PayPalPayment : IPaymentStrategy
{
    public void Pay(decimal amount)
    {
        Console.WriteLine($"Paid ${amount} using PayPal");
    }
}

// Concrete Strategy 3
public class UPIPayment : IPaymentStrategy
{
    public void Pay(decimal amount)
    {
        Console.WriteLine($"Paid ${amount} using UPI");
    }
}

// Context
public class PaymentProcessor
{
    private readonly IPaymentStrategy _paymentStrategy;

    public PaymentProcessor(IPaymentStrategy paymentStrategy)
    {
        _paymentStrategy = paymentStrategy;
    }

    public void Checkout(decimal amount)
    {
        Console.WriteLine("Starting checkout...");
        _paymentStrategy.Pay(amount);
        Console.WriteLine("Checkout complete.\n");
    }
}

// Client
class Program
{
    static void Main()
    {
        PaymentProcessor processor;

        processor = new PaymentProcessor(new CreditCardPayment());
        processor.Checkout(500);

        processor = new PaymentProcessor(new PayPalPayment());
        processor.Checkout(750);

        processor = new PaymentProcessor(new UPIPayment());
        processor.Checkout(100);
    }
}