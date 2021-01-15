namespace KillerApp_Quiz
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.buttonNext = new System.Windows.Forms.Button();
            this.labelName1 = new System.Windows.Forms.Label();
            this.buttonHS1 = new System.Windows.Forms.Button();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // buttonNext
            // 
            this.buttonNext.BackColor = System.Drawing.Color.Transparent;
            this.buttonNext.Font = new System.Drawing.Font("Arial Black", 20F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.buttonNext.Location = new System.Drawing.Point(254, 348);
            this.buttonNext.Name = "buttonNext";
            this.buttonNext.Size = new System.Drawing.Size(310, 90);
            this.buttonNext.TabIndex = 0;
            this.buttonNext.Text = "Next";
            this.buttonNext.UseVisualStyleBackColor = false;
            this.buttonNext.Click += new System.EventHandler(this.ButtonNext_Click);
            // 
            // labelName1
            // 
            this.labelName1.AutoSize = true;
            this.labelName1.BackColor = System.Drawing.Color.Cyan;
            this.labelName1.Font = new System.Drawing.Font("Arial Black", 20F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelName1.Location = new System.Drawing.Point(298, 9);
            this.labelName1.Name = "labelName1";
            this.labelName1.Size = new System.Drawing.Size(222, 48);
            this.labelName1.TabIndex = 1;
            this.labelName1.Text = "Welkom bij";
            this.labelName1.Click += new System.EventHandler(this.LabelName1_Click);
            // 
            // buttonHS1
            // 
            this.buttonHS1.BackColor = System.Drawing.Color.Transparent;
            this.buttonHS1.Location = new System.Drawing.Point(354, 314);
            this.buttonHS1.Name = "buttonHS1";
            this.buttonHS1.Size = new System.Drawing.Size(110, 28);
            this.buttonHS1.TabIndex = 3;
            this.buttonHS1.Text = "High Score";
            this.buttonHS1.UseVisualStyleBackColor = false;
            this.buttonHS1.Click += new System.EventHandler(this.ButtonHS1_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.pictureBox1.Image = global::KillerApp_Quiz.Properties.Resources.Quiz;
            this.pictureBox1.Location = new System.Drawing.Point(2, 0);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(797, 448);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox1.TabIndex = 4;
            this.pictureBox1.TabStop = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.buttonNext);
            this.Controls.Add(this.buttonHS1);
            this.Controls.Add(this.labelName1);
            this.Controls.Add(this.pictureBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button buttonNext;
        private System.Windows.Forms.Label labelName1;
        private System.Windows.Forms.Button buttonHS1;
        private System.Windows.Forms.PictureBox pictureBox1;
    }
}

