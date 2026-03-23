using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Inheritance
{
    internal abstract class Persona
    {
        string date_birth;
        string name;

        public Persona(string data, string name)
        {
            this.date_birth = data;
            this.name = name;
        }

        public abstract void GetSalary();
        public virtual void HoursWorked(int a) { }
    }
}
