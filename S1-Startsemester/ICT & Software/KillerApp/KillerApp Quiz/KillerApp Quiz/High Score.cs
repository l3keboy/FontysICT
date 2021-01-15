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
using System.IO;

namespace KillerApp_Quiz
{
    public partial class High_Score : Form
    {
        Thread th;

        public High_Score()
        {
            InitializeComponent();
            int eindscore = 0;
            if (Awnser_Overview.next == "yes")
            {
                if (Question_1.AwnserQ1 == "124")
                {
                    eindscore += 1;
                }

                if (Question_2.AwnserQ2 == "Roze")
                {
                    eindscore += 1;
                }

                if (Question_3.AwnserQ3 == "357")
                {
                    eindscore += 3;
                }

                if (Question_4.AwnserQ4 == "Leclerc")
                {
                    eindscore += 2;
                }

                if (Question_5.AwnserQ5 == "Onjuist")
                {
                    eindscore += 1;
                }

                labelScore.Text = Convert.ToString(eindscore);

                string fileLocation = @"C:\Users\luke\Documents\Junk\High Score killerapp.txt";
                string Name = Convert.ToString(Awnser_Overview.yourName);
                string Score = Convert.ToString(eindscore);

                List<string> lines = new List<String>();

                foreach (string line in File.ReadAllLines(fileLocation))
                {
                    HighScore.Items.Add(line);
                    lines.Add(line);

                }

                lines.Add(Name + " " + Score);
                File.WriteAllLines(fileLocation, lines);
                Awnser_Overview.next = "";
            }
            else
            {
                string fileLocation = @"C:\Users\luke\Documents\Junk\High Score killerapp.txt";
                foreach (string line in File.ReadAllLines(fileLocation))
                {
                    HighScore.Items.Add(line);
                }
            }
        }

        private void ButtonHome_Click(object sender, EventArgs e)
        {
            this.Close();
            th = new Thread(opennewform);
            th.SetApartmentState(ApartmentState.STA);
            th.Start();
        }

        private void opennewform(object obj)
        {
            Application.Run(new Form1());
        }

        private void High_Score_Load(object sender, EventArgs e)
        {

        }

        private void HighScore_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
    }
}
