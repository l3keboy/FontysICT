﻿namespace KillerApp_Quiz
{
    partial class Question_1
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
            this.txtBoxAwnser1 = new System.Windows.Forms.TextBox();
            this.buttonAwnserChangedQ1 = new System.Windows.Forms.Button();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // buttonNext
            // 
            this.buttonNext.Font = new System.Drawing.Font("Arial Black", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.buttonNext.Location = new System.Drawing.Point(669, 392);
            this.buttonNext.Name = "buttonNext";
            this.buttonNext.Size = new System.Drawing.Size(119, 46);
            this.buttonNext.TabIndex = 0;
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
            this.label1.Size = new System.Drawing.Size(265, 42);
            this.label1.TabIndex = 1;
            this.label1.Text = "Wat is 34 + 90?";
            // 
            // txtBoxAwnser1
            // 
            this.txtBoxAwnser1.Location = new System.Drawing.Point(13, 77);
            this.txtBoxAwnser1.Name = "txtBoxAwnser1";
            this.txtBoxAwnser1.Size = new System.Drawing.Size(265, 22);
            this.txtBoxAwnser1.TabIndex = 2;
            // 
            // buttonAwnserChangedQ1
            // 
            this.buttonAwnserChangedQ1.Font = new System.Drawing.Font("Arial Black", 7.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.buttonAwnserChangedQ1.Location = new System.Drawing.Point(12, 392);
            this.buttonAwnserChangedQ1.Name = "buttonAwnserChangedQ1";
            this.buttonAwnserChangedQ1.Size = new System.Drawing.Size(278, 46);
            this.buttonAwnserChangedQ1.TabIndex = 3;
            this.buttonAwnserChangedQ1.Text = "Use this if awnser is changed";
            this.buttonAwnserChangedQ1.UseVisualStyleBackColor = true;
            this.buttonAwnserChangedQ1.Click += new System.EventHandler(this.Button1_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.ErrorImage = global::KillerApp_Quiz.Properties.Resources.Optellen;
            this.pictureBox1.Image = global::KillerApp_Quiz.Properties.Resources.Optellen;
            this.pictureBox1.Location = new System.Drawing.Point(439, 13);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(349, 287);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox1.TabIndex = 4;
            this.pictureBox1.TabStop = false;
            // 
            // Question_1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.buttonAwnserChangedQ1);
            this.Controls.Add(this.txtBoxAwnser1);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.buttonNext);
            this.Name = "Question_1";
            this.Text = "Question_1";
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button buttonNext;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtBoxAwnser1;
        private System.Windows.Forms.Button buttonAwnserChangedQ1;
        private System.Windows.Forms.PictureBox pictureBox1;
    }
}