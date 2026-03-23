using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Inheritance.Humans
{
    internal class Manager:Persona
    {
        decimal salary_per_hour;
        int hour = 0;

        public Manager(string date_birth, string name, decimal salary_per_hour) : base(date_birth, name)
        {
            this.salary_per_hour = salary_per_hour;
        }

        public override void HoursWorked(int a)
        {
            this.hour += a;
        }

        public override void GetSalary()
        {
            Console.WriteLine((salary_per_hour * hour).ToString());
        }
    }
}
