namespace FinanceChatAI
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            panel1 = new Panel();
            welcome_label2 = new Label();
            btn_Research = new Button();
            btn_Forecast = new Button();
            btn_Ask = new Button();
            pictureBox1 = new PictureBox();
            title_label1 = new Label();
            pictureBox2 = new PictureBox();
            panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)pictureBox1).BeginInit();
            ((System.ComponentModel.ISupportInitialize)pictureBox2).BeginInit();
            SuspendLayout();
            // 
            // panel1
            // 
            panel1.Controls.Add(welcome_label2);
            panel1.Location = new Point(277, 157);
            panel1.Name = "panel1";
            panel1.Size = new Size(1366, 385);
            panel1.TabIndex = 1;
            // 
            // welcome_label2
            // 
            welcome_label2.AutoSize = true;
            welcome_label2.Font = new Font("Microsoft JhengHei UI", 36F, FontStyle.Bold, GraphicsUnit.Point);
            welcome_label2.Location = new Point(117, 171);
            welcome_label2.Name = "welcome_label2";
            welcome_label2.Size = new Size(1254, 77);
            welcome_label2.TabIndex = 0;
            welcome_label2.Text = "WELCOME !請點選按鈕執行您想執行的操作!";
            // 
            // btn_Research
            // 
            btn_Research.BackColor = Color.FromArgb(255, 255, 128);
            btn_Research.BackgroundImage = (Image)resources.GetObject("btn_Research.BackgroundImage");
            btn_Research.Location = new Point(1, 157);
            btn_Research.Name = "btn_Research";
            btn_Research.Size = new Size(252, 75);
            btn_Research.TabIndex = 2;
            btn_Research.UseVisualStyleBackColor = false;
            btn_Research.Click += btn_Research_Click;
            // 
            // btn_Forecast
            // 
            btn_Forecast.BackColor = Color.FromArgb(255, 255, 128);
            btn_Forecast.BackgroundImage = (Image)resources.GetObject("btn_Forecast.BackgroundImage");
            btn_Forecast.Location = new Point(1, 290);
            btn_Forecast.Name = "btn_Forecast";
            btn_Forecast.Size = new Size(252, 75);
            btn_Forecast.TabIndex = 3;
            btn_Forecast.UseVisualStyleBackColor = false;
            btn_Forecast.Click += btn_Forecast_Click;
            // 
            // btn_Ask
            // 
            btn_Ask.BackColor = Color.FromArgb(255, 255, 128);
            btn_Ask.BackgroundImage = (Image)resources.GetObject("btn_Ask.BackgroundImage");
            btn_Ask.Location = new Point(1, 445);
            btn_Ask.Name = "btn_Ask";
            btn_Ask.Size = new Size(252, 75);
            btn_Ask.TabIndex = 4;
            btn_Ask.UseVisualStyleBackColor = false;
            btn_Ask.Click += btn_Ask_Click;
            // 
            // pictureBox1
            // 
            pictureBox1.Image = (Image)resources.GetObject("pictureBox1.Image");
            pictureBox1.Location = new Point(461, -1);
            pictureBox1.Name = "pictureBox1";
            pictureBox1.Size = new Size(603, 114);
            pictureBox1.TabIndex = 5;
            pictureBox1.TabStop = false;
            // 
            // title_label1
            // 
            title_label1.AutoSize = true;
            title_label1.Font = new Font("Microsoft JhengHei UI", 25.8000011F, FontStyle.Bold, GraphicsUnit.Point);
            title_label1.ForeColor = Color.White;
            title_label1.Image = (Image)resources.GetObject("title_label1.Image");
            title_label1.Location = new Point(1445, 67);
            title_label1.Name = "title_label1";
            title_label1.Size = new Size(107, 56);
            title_label1.TabIndex = 6;
            title_label1.Text = "title";
            // 
            // pictureBox2
            // 
            pictureBox2.Image = (Image)resources.GetObject("pictureBox2.Image");
            pictureBox2.Location = new Point(48, 30);
            pictureBox2.Name = "pictureBox2";
            pictureBox2.Size = new Size(183, 121);
            pictureBox2.TabIndex = 7;
            pictureBox2.TabStop = false;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(9F, 19F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = Color.White;
            BackgroundImage = (Image)resources.GetObject("$this.BackgroundImage");
            ClientSize = new Size(1731, 698);
            Controls.Add(pictureBox2);
            Controls.Add(title_label1);
            Controls.Add(pictureBox1);
            Controls.Add(btn_Ask);
            Controls.Add(btn_Forecast);
            Controls.Add(btn_Research);
            Controls.Add(panel1);
            Name = "Form1";
            Text = "Form1";
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)pictureBox1).EndInit();
            ((System.ComponentModel.ISupportInitialize)pictureBox2).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion
        private Panel panel1;
        private Button btn_Research;
        private Button btn_Forecast;
        private Button btn_Ask;
        private Label welcome_label2;
        private PictureBox pictureBox1;
        private Label title_label1;
        private PictureBox pictureBox2;
    }
}