namespace KillerApp_Quiz
{
    partial class High_Score
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
            this.buttonHome = new System.Windows.Forms.Button();
            this.label6 = new System.Windows.Forms.Label();
            this.labelScore = new System.Windows.Forms.Label();
            this.HighScore = new System.Windows.Forms.ListBox();
            this.SuspendLayout();
            // 
            // buttonHome
            // 
            this.buttonHome.Font = new System.Drawing.Font("Arial Black", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.buttonHome.Location = new System.Drawing.Point(299, 377);
            this.buttonHome.Name = "buttonHome";
            this.buttonHome.Size = new System.Drawing.Size(220, 61);
            this.buttonHome.TabIndex = 0;
            this.buttonHome.Text = "Homepage";
            this.buttonHome.UseVisualStyleBackColor = true;
            this.buttonHome.Click += new System.EventHandler(this.ButtonHome_Click);
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Font = new System.Drawing.Font("Arial Black", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label6.Location = new System.Drawing.Point(299, 99);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(220, 42);
            this.label6.TabIndex = 2;
            this.label6.Text = "Jouw Score:";
            // 
            // labelScore
            // 
            this.labelScore.AutoSize = true;
            this.labelScore.Font = new System.Drawing.Font("Microsoft Sans Serif", 25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelScore.Location = new System.Drawing.Point(377, 181);
            this.labelScore.Name = "labelScore";
            this.labelScore.Size = new System.Drawing.Size(129, 48);
            this.labelScore.TabIndex = 3;
            this.labelScore.Text = "Score";
            // 
            // HighScore
            // 
            this.HighScore.FormattingEnabled = true;
            this.HighScore.ItemHeight = 16;
            this.HighScore.Location = new System.Drawing.Point(13, 13);
            this.HighScore.Name = "HighScore";
            this.HighScore.Size = new System.Drawing.Size(212, 420);
            this.HighScore.TabIndex = 5;
            this.HighScore.SelectedIndexChanged += new System.EventHandler(this.HighScore_SelectedIndexChanged);
            // 
            // High_Score
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.HighScore);
            this.Controls.Add(this.labelScore);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.buttonHome);
            this.Name = "High_Score";
            this.Text = "High_Score";
            this.Load += new System.EventHandler(this.High_Score_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button buttonHome;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label labelScore;
        private System.Windows.Forms.ListBox HighScore;
    }
}