using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace EuroDrollarConverter
{
    public partial class Form1 : Form
    {
        
        public Form1()
        {
            InitializeComponent();
        }

        private void ButtonLeft_Click(object sender, EventArgs e)
        {
            //This is the left button.
            //euro = dollar / koers.
            if (Convert.ToDouble(TextBoxRight.Text) > 0)
            {
                double Result2 = Convert.ToDouble(TextBoxRight.Text) / Convert.ToDouble(NumericUpDown.Value);
                TextBoxLeft.Text = Result2.ToString();
            }
            else
            {
                MessageBox.Show("Error");
            }
            
        }

        private void Button2_Click(object sender, EventArgs e)
        {
            //This is the right button.
            //dollar = euro * koers.
            if (Convert.ToDouble(TextBoxLeft.Text) > 0){
                double Result = Convert.ToDouble(TextBoxLeft.Text) * Convert.ToDouble(NumericUpDown.Value);
                TextBoxRight.Text = Result.ToString();
            }
            else
            {
                MessageBox.Show("Error");
            }
            
        }

        private void TextBoxLeft_TextChanged(object sender, EventArgs e)
        {
            //This is the Left textbox.

        }

        private void TextBoxRight_TextChanged(object sender, EventArgs e)
        {
            //This is the Right textbox.

        }

        private void NumericUpDown_ValueChanged(object sender, EventArgs e)
        {
            //This is the NumericUpDown box.
            //Changes in properties.
            
        }
    }
}
