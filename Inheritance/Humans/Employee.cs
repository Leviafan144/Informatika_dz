using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Inheritance
{
    internal class Employee:Persona
    {
        decimal salary;
        string date_empoeyment;

        public Employee(string date_birth, string name, decimal salary, string date_empoeyment) : base(date_birth,name)
        {
            this.salary = salary;
            this.date_empoeyment = date_empoeyment;
        }

        public override void GetSalary()
        {
            Console.WriteLine(salary.ToString());
        }
    }
}
