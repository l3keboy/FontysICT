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
    public partial class Form1 : Form
    {
        Thread th;

        public Form1()
        {
            InitializeComponent();
        }

        private void LabelName1_Click(object sender, EventArgs e)
        {
           
        }

        private void LabelName2_Click(object sender, EventArgs e)
        {
           
        }

        private void ButtonNext_Click(object sender, EventArgs e)
        {
            this.Close();
            th = new Thread(opennewform);
            th.SetApartmentState(ApartmentState.STA);
            th.Start();
        }

        private void ButtonHS1_Click(object sender, EventArgs e)
        {
            this.Close();
            th = new Thread(openhighscore);
            th.SetApartmentState(ApartmentState.STA);
            th.Start();
        }

        private void openhighscore(object obj)
        {
            Application.Run(new High_Score());
        }

        private void opennewform(object obj)
        {
            Application.Run(new Rules());
        }


    }
}
