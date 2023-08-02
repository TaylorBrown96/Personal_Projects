using System;
using System.Windows.Forms;

namespace WinUI
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btn_Calculate_Click(object sender, EventArgs e)
        {
            try
            {
                
                    
                double KaDecimal = Convert.ToDouble(tb_KaDecimal.Text);
                double KaPower = Convert.ToDouble(tb_KaPower.Text);
                double MOfSolution = Convert.ToDouble(tb_MOfSolution.Text);
                double x = Math.Sqrt(KaDecimal * Math.Pow(10, KaPower) * MOfSolution);

                double pH = -Math.Log10(x);
                double ionization = x / MOfSolution * 100;

                MessageBox.Show("The value of x is: " + string.Format("{0:N8}", x) +
                            "\n\nThe pH is: " + string.Format("{0:N2}", pH) +
                            "\n\n% ionization: " + string.Format("{0:N2}%", ionization)
                            , "Solution for " + tb_SolutionName.Text);
            }
            catch
            {
                MessageBox.Show("Please enter valid numerical values!", "Error!");
            }
        }
    }
}