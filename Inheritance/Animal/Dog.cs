using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace Inheritance
{
    internal class Dog:Animal
    {
        string name;
        string type = "Собака";

        public Dog(int weight, string name):base(weight, name)
        {
            this.name = name;
            Console.WriteLine($"Создана {type} {this.name}, {this.weight}");
        }
        public Dog()
        {
            Console.WriteLine("Конструктор собаки без праметров");
        }

        public override void Talk()
        {
            Console.WriteLine("Woof");
        }
    }
}
