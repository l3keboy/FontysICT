using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Threading;

namespace KillerApp_Quiz
{
    public partial class Question_3 : Form
    {
        Thread th;

        public static string AwnserQ3 = "";

        public Question_3()
        {
            InitializeComponent();
        }

        private void ButtonNext_Click(object sender, EventArgs e)
        {
            AwnserQ3 = txtBoxAwnser3.Text;

            this.Close();
            th = new Thread(opennewform);
            th.SetApartmentState(ApartmentState.STA);
            th.Start();
        }

        private void opennewform(object obj)
        {
            Application.Run(new Question_4());
        }

        private void ButtonAwnserChangedQ3_Click(object sender, EventArgs e)
        {
            AwnserQ3 = txtBoxAwnser3.Text;

            this.Close();
            th = new Thread(anwserOverview);
            th.SetApartmentState(ApartmentState.STA);
            th.Start();
        }

        private void anwserOverview(object obj)
        {
            Application.Run(new Awnser_Overview());
        }
    }
}
