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
    public partial class Question_5 : Form
    {
        Thread th;

        public static string AwnserQ5 = "";

        public Question_5()
        {
            InitializeComponent();
        }

        private void ButtonNext_Click(object sender, EventArgs e)
        {
            if (radioButtonJuist.Checked == true)
            {
                AwnserQ5 = Convert.ToString("Juist");
            }
            else if (radioButtonOnjuist.Checked == true)
            {
                AwnserQ5 = Convert.ToString("Onjuist");
            }

            this.Close();
            th = new Thread(opennewform);
            th.SetApartmentState(ApartmentState.STA);
            th.Start();
        }

        private void opennewform(object obj)
        {
            Application.Run(new Awnser_Overview());
        }

        private void RadioButton2_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void ButtonAwnserChangedQ5_Click(object sender, EventArgs e)
        {
            if (radioButtonJuist.Checked == true)
            {
                AwnserQ5 = Convert.ToString("Juist");
            }
            else if (radioButtonOnjuist.Checked == true)
            {
                AwnserQ5 = Convert.ToString("Onjuist");
            }

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
