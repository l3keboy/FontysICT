namespace EuroDrollarConverter
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
            this.ButtonLeft = new System.Windows.Forms.Button();
            this.ButtonRight = new System.Windows.Forms.Button();
            this.TextBoxLeft = new System.Windows.Forms.TextBox();
            this.TextBoxRight = new System.Windows.Forms.TextBox();
            this.NumericUpDown = new System.Windows.Forms.NumericUpDown();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.NumericUpDown)).BeginInit();
            this.SuspendLayout();
            // 
            // ButtonLeft
            // 
            this.ButtonLeft.Location = new System.Drawing.Point(299, 124);
            this.ButtonLeft.Name = "ButtonLeft";
            this.ButtonLeft.Size = new System.Drawing.Size(60, 56);
            this.ButtonLeft.TabIndex = 0;
            this.ButtonLeft.Text = "<";
            this.ButtonLeft.UseVisualStyleBackColor = true;
            this.ButtonLeft.Click += new System.EventHandler(this.ButtonLeft_Click);
            // 
            // ButtonRight
            // 
            this.ButtonRight.Location = new System.Drawing.Point(365, 124);
            this.ButtonRight.Name = "ButtonRight";
            this.ButtonRight.Size = new System.Drawing.Size(60, 56);
            this.ButtonRight.TabIndex = 1;
            this.ButtonRight.Text = ">";
            this.ButtonRight.UseVisualStyleBackColor = true;
            this.ButtonRight.Click += new System.EventHandler(this.Button2_Click);
            // 
            // TextBoxLeft
            // 
            this.TextBoxLeft.Location = new System.Drawing.Point(193, 142);
            this.TextBoxLeft.Name = "TextBoxLeft";
            this.TextBoxLeft.Size = new System.Drawing.Size(100, 22);
            this.TextBoxLeft.TabIndex = 2;
            this.TextBoxLeft.TextChanged += new System.EventHandler(this.TextBoxLeft_TextChanged);
            // 
            // TextBoxRight
            // 
            this.TextBoxRight.Location = new System.Drawing.Point(432, 142);
            this.TextBoxRight.Name = "TextBoxRight";
            this.TextBoxRight.Size = new System.Drawing.Size(100, 22);
            this.TextBoxRight.TabIndex = 3;
            this.TextBoxRight.TextChanged += new System.EventHandler(this.TextBoxRight_TextChanged);
            // 
            // NumericUpDown
            // 
            this.NumericUpDown.DecimalPlaces = 2;
            this.NumericUpDown.Increment = new decimal(new int[] {
            1,
            0,
            0,
            131072});
            this.NumericUpDown.Location = new System.Drawing.Point(365, 212);
            this.NumericUpDown.Name = "NumericUpDown";
            this.NumericUpDown.Size = new System.Drawing.Size(99, 22);
            this.NumericUpDown.TabIndex = 4;
            this.NumericUpDown.Value = new decimal(new int[] {
            200,
            0,
            0,
            131072});
            this.NumericUpDown.ValueChanged += new System.EventHandler(this.NumericUpDown_ValueChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(257, 214);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(102, 17);
            this.label1.TabIndex = 5;
            this.label1.Text = "Koers: €1,- = $";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(49, 89);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(130, 142);
            this.label2.TabIndex = 6;
            this.label2.Text = "€";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label3.Location = new System.Drawing.Point(538, 92);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(130, 142);
            this.label3.TabIndex = 7;
            this.label3.Text = "$";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.NumericUpDown);
            this.Controls.Add(this.TextBoxRight);
            this.Controls.Add(this.TextBoxLeft);
            this.Controls.Add(this.ButtonRight);
            this.Controls.Add(this.ButtonLeft);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.NumericUpDown)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button ButtonLeft;
        private System.Windows.Forms.Button ButtonRight;
        private System.Windows.Forms.TextBox TextBoxLeft;
        private System.Windows.Forms.TextBox TextBoxRight;
        private System.Windows.Forms.NumericUpDown NumericUpDown;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
    }
}

