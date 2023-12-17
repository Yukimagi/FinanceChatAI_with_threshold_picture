using BingChat;//需下載 dotnet add package --prerelease BingChat
using System;
using System.IO;
using System.Text;
using CsvHelper;//需下載 dotnet add package CsvHelper
using System.Net;
using System.Diagnostics;
using System.Text.RegularExpressions;
using CsvHelper.Configuration;
using System.Globalization;
using System.Threading;
using System.IO.Pipes;
namespace FinanceChatAI
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            title_label1.Visible = false;
        }
        //表單切換
        //https://lillylovecode.medium.com/c-%E5%AD%90%E6%AF%8D%E8%A1%A8%E5%96%AE-windows-form-app-e38e1610fba6
        private Form activeForm = null;
        private void openChildForm(Form childForm)
        {
            if (activeForm != null) activeForm.Close();
            activeForm = childForm;
            childForm.TopLevel = false;
            childForm.FormBorderStyle = FormBorderStyle.None;
            childForm.Dock = DockStyle.Fill;
            panel1.Controls.Add(childForm);
            panel1.Tag = childForm;
            childForm.BringToFront();
            childForm.Show();
        }

        private void btn_Research_Click(object sender, EventArgs e)
        {

            title_label1.Visible = false;
            welcome_label2.Visible = false;
            openChildForm(new Research1());
            title_label1.Text = "Research";
            title_label1.Visible = true;
        }

        private void btn_Forecast_Click(object sender, EventArgs e)
        {

            title_label1.Visible = false;
            welcome_label2.Visible = false;
            openChildForm(new Forecast1());
            title_label1.Text = "Forecast";
            title_label1.Visible = true;
        }

        private void btn_Ask_Click(object sender, EventArgs e)
        {

            title_label1.Visible = false;
            welcome_label2.Visible = false;
            openChildForm(new Ask1());
            title_label1.Text = "Ask";
            title_label1.Visible = true;
        }
    }
}