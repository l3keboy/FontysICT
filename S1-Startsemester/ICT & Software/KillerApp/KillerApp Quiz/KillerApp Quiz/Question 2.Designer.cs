namespace KillerApp_Quiz
{
    partial class Question_2
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
            this.label1 = new System.Windows.Forms.Label();
            this.txtBoxAwnser2 = new System.Windows.Forms.TextBox();
            this.buttonAwnserChangedQ2 = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // buttonNext
            // 
            this.buttonNext.Font = new System.Drawing.Font("Arial Black", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.buttonNext.Location = new System.Drawing.Point(669, 392);
            this.buttonNext.Name = "buttonNext";
            this.buttonNext.Size = new System.Drawing.Size(119, 46);
            this.buttonNext.TabIndex = 1;
            this.buttonNext.Text = "Next";
            this.buttonNext.UseVisualStyleBackColor = true;
            this.buttonNext.Click += new System.EventHandler(this.ButtonNext_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Arial Black", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(13, 13);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(677, 84);
            this.label1.TabIndex = 2;
            this.label1.Text = "Wat krijg je als je de kleuren rood en wit\r\nmet elkaar mengt?";
            // 
            // txtBoxAwnser2
            // 
            this.txtBoxAwnser2.Location = new System.Drawing.Point(13, 101);
            this.txtBoxAwnser2.Name = "txtBoxAwnser2";
            this.txtBoxAwnser2.Size = new System.Drawing.Size(320, 22);
            this.txtBoxAwnser2.TabIndex = 3;
            // 
            // buttonAwnserChangedQ2
            // 
            this.buttonAwnserChangedQ2.Font = new System.Drawing.Font("Arial Black", 7.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.buttonAwnserChangedQ2.Location = new System.Drawing.Point(12, 392);
            this.buttonAwnserChangedQ2.Name = "buttonAwnserChangedQ2";
            this.buttonAwnserChangedQ2.Size = new System.Drawing.Size(278, 46);
            this.buttonAwnserChangedQ2.TabIndex = 4;
            this.buttonAwnserChangedQ2.Text = "Use this if awnser is changed";
            this.buttonAwnserChangedQ2.UseVisualStyleBackColor = true;
            this.buttonAwnserChangedQ2.Click += new System.EventHandler(this.ButtonAwnserChangedQ2_Click);
            // 
            // Question_2
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.buttonAwnserChangedQ2);
            this.Controls.Add(this.txtBoxAwnser2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.buttonNext);
            this.Name = "Question_2";
            this.Text = "Question_2";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button buttonNext;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtBoxAwnser2;
        private System.Windows.Forms.Button buttonAwnserChangedQ2;
    }
}