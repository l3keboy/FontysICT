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
    public partial class Awnser_Overview : Form
    {
        Thread th;

        public static string yourName = "";
        public static string next = "";

        public Awnser_Overview()
        {
            InitializeComponent();
        }

        private void Awnser_Overview_Load(object sender, EventArgs e)
        {
            labelAwnser1.Text = Question_1.AwnserQ1;
            labelAwnser2.Text = Question_2.AwnserQ2;
            labelAwnser3.Text = Question_3.AwnserQ3;
            labelAwnser4.Text = Question_4.AwnserQ4;
            labelAwnser5.Text = Question_5.AwnserQ5;
        }

        public void ButtonNext_Click(object sender, EventArgs e)
        {
            yourName = Convert.ToString(textBoxName.Text);
            next = "yes";

            this.Close();
            th = new Thread(opennewform);
            th.SetApartmentState(ApartmentState.STA);
            th.Start();
        }

        private void opennewform(object obj)
        {
            Application.Run(new High_Score());
        }

        private void LabelT_Click(object sender, EventArgs e)
        {
            
        }

        private void ButtonChange1_Click(object sender, EventArgs e)
        {
            
            this.Close();
            th = new Thread(question1);
            th.SetApartmentState(ApartmentState.STA);
            th.Start();
        }

        private void ButtonChange2_Click(object sender, EventArgs e)
        {
            this.Close();
            th = new Thread(question2);
            th.SetApartmentState(ApartmentState.STA);
            th.Start();
        }

        private void ButtonChange3_Click(object sender, EventArgs e)
        {
            this.Close();
            th = new Thread(question3);
            th.SetApartmentState(ApartmentState.STA);
            th.Start();
        }

        private void ButtonChange4_Click(object sender, EventArgs e)
        {
            this.Close();
            th = new Thread(question4);
            th.SetApartmentState(ApartmentState.STA);
            th.Start();
        }

        private void ButtonChange5_Click(object sender, EventArgs e)
        {
            this.Close();
            th = new Thread(question5);
            th.SetApartmentState(ApartmentState.STA);
            th.Start();
        }

        private void question1(object obj)
        {
            Application.Run(new Question_1());
        }
        private void question2(object obj)
        {
            Application.Run(new Question_2());
        }
        private void question3(object obj)
        {
            Application.Run(new Question_3());
        }
        private void question4(object obj)
        {
            Application.Run(new Question_4());
        }
        private void question5(object obj)
        {
            Application.Run(new Question_5());
        }

        public void TextBoxName_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
