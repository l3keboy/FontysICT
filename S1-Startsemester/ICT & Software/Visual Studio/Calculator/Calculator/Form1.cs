using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Calculator
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void ButtonPlus_Click(object sender, EventArgs e)
        {
            //When Pressed the numbers will be added up.
            double resultplus = Convert.ToDouble(Txtbox1.Text) + Convert.ToDouble(textBox1.Text);

            if (resultplus < 0)
            {
                textBox2.Text = resultplus.ToString();
                textBox2.ForeColor = Color.Red;
            }
            else
            {
                textBox2.Text = resultplus.ToString();
                textBox2.ForeColor = Color.Black;
            }
        }

        private void ButtonMultiply_Click(object sender, EventArgs e)
        {
            //When Pressed the numbers will be multiplyed.
            double resultmultiply = Convert.ToDouble(Txtbox1.Text) * Convert.ToDouble(textBox1.Text);
            
            if (resultmultiply < 0)
            {
                textBox2.Text = resultmultiply.ToString();
                textBox2.ForeColor = Color.Red;
            }
            else
            {
                textBox2.Text = resultmultiply.ToString();
                textBox2.ForeColor = Color.Black;
            }

        }

        private void Txtbox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void TextBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void TextBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void ButtonDivide_Click(object sender, EventArgs e)
        {
            //When Pressed the numbers will be divided.
            double resultdivide = Convert.ToDouble(Txtbox1.Text) / Convert.ToDouble(textBox1.Text);

            if (Convert.ToDouble(textBox1.Text) == 0) 
            {
                MessageBox.Show("Delen door 0 is niet mogelijk");
            }
            else
            {
                textBox2.Text = resultdivide.ToString();
            }
            
            if (resultdivide < 0)
            {
                textBox2.Text = resultdivide.ToString();
                textBox2.ForeColor = Color.Red;
            }
            else
            {
                textBox2.Text = resultdivide.ToString();
                textBox2.ForeColor = Color.Black;
            }
        }

        private void ButtonW_Click(object sender, EventArgs e)
        {
            //When Pressed the root of number 1 or 2 will be taken.
            //Een min getal heeft geen wortel.
            double resultroot = Math.Sqrt(Convert.ToDouble(Txtbox1.Text));
            textBox2.Text = resultroot.ToString();

            if (resultroot < 0)
            {
                textBox2.Text = resultroot.ToString();
                textBox2.ForeColor = Color.Red;
            }
            else
            {
                textBox2.Text = resultroot.ToString();
                textBox2.ForeColor = Color.Black;
            }
        }
    }
}
