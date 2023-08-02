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
                // Makes sure that the user inputed values for each numerical field.
                if (tb_KaDecimal.Text.Length == 0 || tb_KaPower.Text.Length == 0 || tb_MOfSolution.Text.Length == 0)
                {
                    throw new Exception();
                }

                // Appends user data to newly created variables.
                double KaDecimal = Convert.ToDouble(tb_KaDecimal.Text);
                double KaPower = Convert.ToDouble(tb_KaPower.Text);
                double MOfSolution = Convert.ToDouble(tb_MOfSolution.Text);

                // Performs apprpriate math with values given to attain (value of X, pH, and ionization). 
                double X = Math.Sqrt(KaDecimal * Math.Pow(10, KaPower) * MOfSolution);
                double pH = -Math.Log10(X);
                double ionization = X / MOfSolution * 100;

                // Retrives the solution name. If no name is given the default is set to "unknown".
                string solutionName = "unknown";
                if (tb_SolutionName.Text.Length > 0) {solutionName = tb_SolutionName.Text;}

                // Displays the calculations performed.
                MessageBox.Show("The value of X is: " + string.Format("{0:N8}", X) +
                            "\n\nThe pH is: " + string.Format("{0:N2}", pH) +
                            "\n\n% ionization: " + string.Format("{0:N2}%", ionization)
                            , "Solution for " + solutionName);
            }
            catch
            {
                // Prompts the user to check their inputs.
                MessageBox.Show("Please make sure all fields have valid numerical values!", "Error!");
            }
        }
    }
}