using Inheritance.Humans;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Inheritance
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*List<Animal> animals = new List<Animal>();
            Animal cat = new Cat(30, "Ilusha");
            Animal dog = new Dog(20, "Igor");
            Animal cat_anonim = new Cat();
            Animal dog_anonim = new Dog();
            animals.Add(cat);
            animals.Add(dog);
            animals.Add(cat_anonim);
            animals.Add(dog_anonim);

            foreach (Animal anim in animals)
            {
                anim.Talk();
                anim.Feed(15);
                Console.WriteLine($"Вес: {anim.Weight}");
            }*/
            List<Persona> staff = new List<Persona>();
            Persona persona1 = new Employee("13.12.2004", "Alex", 233001, "03.11.2023");
            Persona persona2 = new Employee("30.02.2006", "Vitaliy", 199220, "03.11.2023");
            Persona persona3 = new Manager("12.13.2004", "Georgiy", 2000);
            persona3.HoursWorked(145);
            staff.Add(persona1);
            staff.Add(persona2);
            staff.Add(persona3);

            foreach (Persona persona in staff)
            {
                persona.GetSalary();
            }
        }
    }
}
