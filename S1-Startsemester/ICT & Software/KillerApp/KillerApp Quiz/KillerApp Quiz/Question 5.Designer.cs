namespace KillerApp_Quiz
{
    partial class Question_5
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
            this.radioButtonJuist = new System.Windows.Forms.RadioButton();
            this.radioButtonOnjuist = new System.Windows.Forms.RadioButton();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.label2 = new System.Windows.Forms.Label();
            this.buttonAwnserChangedQ5 = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
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
            this.label1.Size = new System.Drawing.Size(493, 42);
            this.label1.TabIndex = 2;
            this.label1.Text = "Is de stelling juist of onjuist?";
            // 
            // radioButtonJuist
            // 
            this.radioButtonJuist.AutoSize = true;
            this.radioButtonJuist.Location = new System.Drawing.Point(6, 46);
            this.radioButtonJuist.Name = "radioButtonJuist";
            this.radioButtonJuist.Size = new System.Drawing.Size(58, 21);
            this.radioButtonJuist.TabIndex = 3;
            this.radioButtonJuist.TabStop = true;
            this.radioButtonJuist.Text = "Juist";
            this.radioButtonJuist.UseVisualStyleBackColor = true;
            // 
            // radioButtonOnjuist
            // 
            this.radioButtonOnjuist.AutoSize = true;
            this.radioButtonOnjuist.Location = new System.Drawing.Point(6, 73);
            this.radioButtonOnjuist.Name = "radioButtonOnjuist";
            this.radioButtonOnjuist.Size = new System.Drawing.Size(73, 21);
            this.radioButtonOnjuist.TabIndex = 4;
            this.radioButtonOnjuist.TabStop = true;
            this.radioButtonOnjuist.Text = "Onjuist";
            this.radioButtonOnjuist.UseVisualStyleBackColor = true;
            this.radioButtonOnjuist.CheckedChanged += new System.EventHandler(this.RadioButton2_CheckedChanged);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.radioButtonOnjuist);
            this.groupBox1.Controls.Add(this.radioButtonJuist);
            this.groupBox1.Location = new System.Drawing.Point(20, 92);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(200, 100);
            this.groupBox1.TabIndex = 5;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Juist of Onjuist?";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Arial", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.World, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(16, 55);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(451, 22);
            this.label2.TabIndex = 6;
            this.label2.Text = "Het lichaam van een man bestaat voor 64% uit water.";
            // 
            // buttonAwnserChangedQ5
            // 
            this.buttonAwnserChangedQ5.Font = new System.Drawing.Font("Arial Black", 7.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.buttonAwnserChangedQ5.Location = new System.Drawing.Point(12, 392);
            this.buttonAwnserChangedQ5.Name = "buttonAwnserChangedQ5";
            this.buttonAwnserChangedQ5.Size = new System.Drawing.Size(278, 46);
            this.buttonAwnserChangedQ5.TabIndex = 5;
            this.buttonAwnserChangedQ5.Text = "Use this if awnser is changed";
            this.buttonAwnserChangedQ5.UseVisualStyleBackColor = true;
            this.buttonAwnserChangedQ5.Click += new System.EventHandler(this.ButtonAwnserChangedQ5_Click);
            // 
            // Question_5
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.buttonAwnserChangedQ5);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.buttonNext);
            this.Name = "Question_5";
            this.Text = "Question_5";
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button buttonNext;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.RadioButton radioButtonJuist;
        private System.Windows.Forms.RadioButton radioButtonOnjuist;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button buttonAwnserChangedQ5;
    }
}