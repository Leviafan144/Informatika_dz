using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Inheritance
{
    internal class Cat:Animal
    {
        string name;
        string type = "Кошка";
        public Cat()
        {
            Console.WriteLine("Конструктор кота без параметров");
        }
        public Cat(int weight,string name): base(weight,name)
        {
            this.name = name;
            Console.WriteLine($"Создана {type} {this.name}, {this.weight}");
        }

        public override void Talk()
        {
            Console.WriteLine("Meow");
        }
    }
}
