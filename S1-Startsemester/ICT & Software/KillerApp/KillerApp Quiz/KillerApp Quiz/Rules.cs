using System;
using System.Threading;
using System.Windows.Forms;

namespace KillerApp_Quiz
{
    public partial class Rules : Form
    {
        Thread th;
        public Rules()
        {
            InitializeComponent();
        }

        private void LabelRules_Click(object sender, EventArgs e)
        {

        }

        private void LabelRule1_Click(object sender, EventArgs e)
        {

        }

        private void Button1_Click(object sender, EventArgs e)
        {
            this.Close();
            th = new Thread(opennewform);
            th.SetApartmentState(ApartmentState.STA);
            th.Start();
        }

        private void opennewform(object obj)
        {
            Application.Run(new Question_1());
        }

        private void Label1_Click(object sender, EventArgs e)
        {

        }

        private void Label2_Click(object sender, EventArgs e)
        {

        }
    }
}

