namespace WinUI
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
            this.tb_KaDecimal = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.tb_KaPower = new System.Windows.Forms.TextBox();
            this.tb_MOfSolution = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.btn_Calculate = new System.Windows.Forms.Button();
            this.label3 = new System.Windows.Forms.Label();
            this.tb_SolutionName = new System.Windows.Forms.TextBox();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // tb_KaDecimal
            // 
            this.tb_KaDecimal.Location = new System.Drawing.Point(11, 36);
            this.tb_KaDecimal.Name = "tb_KaDecimal";
            this.tb_KaDecimal.Size = new System.Drawing.Size(47, 20);
            this.tb_KaDecimal.TabIndex = 1;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(66, 42);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(29, 13);
            this.label1.TabIndex = 1;
            this.label1.Text = "X 10";
            // 
            // tb_KaPower
            // 
            this.tb_KaPower.Location = new System.Drawing.Point(92, 19);
            this.tb_KaPower.Name = "tb_KaPower";
            this.tb_KaPower.Size = new System.Drawing.Size(28, 20);
            this.tb_KaPower.TabIndex = 2;
            // 
            // tb_MOfSolution
            // 
            this.tb_MOfSolution.Location = new System.Drawing.Point(16, 34);
            this.tb_MOfSolution.Name = "tb_MOfSolution";
            this.tb_MOfSolution.Size = new System.Drawing.Size(76, 20);
            this.tb_MOfSolution.TabIndex = 3;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(99, 41);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(16, 13);
            this.label2.TabIndex = 4;
            this.label2.Text = "M";
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.tb_KaPower);
            this.groupBox1.Controls.Add(this.tb_KaDecimal);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Location = new System.Drawing.Point(32, 43);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(126, 86);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Ka of the solution";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.tb_MOfSolution);
            this.groupBox2.Controls.Add(this.label2);
            this.groupBox2.Location = new System.Drawing.Point(175, 43);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(126, 86);
            this.groupBox2.TabIndex = 3;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "M of the solution";
            // 
            // btn_Calculate
            // 
            this.btn_Calculate.Location = new System.Drawing.Point(119, 135);
            this.btn_Calculate.Name = "btn_Calculate";
            this.btn_Calculate.Size = new System.Drawing.Size(95, 23);
            this.btn_Calculate.TabIndex = 4;
            this.btn_Calculate.Text = "Calculate";
            this.btn_Calculate.UseVisualStyleBackColor = true;
            this.btn_Calculate.Click += new System.EventHandler(this.btn_Calculate_Click);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(36, 13);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(89, 13);
            this.label3.TabIndex = 5;
            this.label3.Text = "Name of solution:";
            // 
            // tb_SolutionName
            // 
            this.tb_SolutionName.Location = new System.Drawing.Point(131, 10);
            this.tb_SolutionName.Name = "tb_SolutionName";
            this.tb_SolutionName.Size = new System.Drawing.Size(162, 20);
            this.tb_SolutionName.TabIndex = 0;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ButtonHighlight;
            this.ClientSize = new System.Drawing.Size(343, 169);
            this.Controls.Add(this.tb_SolutionName);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.btn_Calculate);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Ka to pH";
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox tb_KaDecimal;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox tb_KaPower;
        private System.Windows.Forms.TextBox tb_MOfSolution;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Button btn_Calculate;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox tb_SolutionName;
    }
}

