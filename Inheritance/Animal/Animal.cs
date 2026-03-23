using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Inheritance
{
    internal abstract class Animal
    {
        string name;
        public int weight;

        public int Weight { get => weight; }

        public Animal(int weight, string name)
        {
            this.weight = weight;
            this.name = name;
            Console.WriteLine($"Создано животное");
        }
        public Animal()
        {
            this.name = "";
            this.weight = 1;
            Console.WriteLine("Конструктор животного без прарметров");
        }

        public abstract void Talk();
        public virtual void Feed(int m)
        {
            this.weight += m;
        }
        public override string ToString()
        {
            return $"{this.name}";
        }
    }
}
