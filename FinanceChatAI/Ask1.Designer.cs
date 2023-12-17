namespace FinanceChatAI
{
    partial class Ask1
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Ask1));
            dateTimePicker1 = new DateTimePicker();
            label1 = new Label();
            title_textBox = new TextBox();
            label2 = new Label();
            add_button = new Button();
            groupBox1 = new GroupBox();
            label8 = new Label();
            label7 = new Label();
            start_button = new Button();
            label6 = new Label();
            label5 = new Label();
            label4 = new Label();
            pictureBox1_ask = new PictureBox();
            title_listBox = new ListBox();
            label3 = new Label();
            ans_textBox = new TextBox();
            re_button = new Button();
            pictureBox1 = new PictureBox();
            groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)pictureBox1_ask).BeginInit();
            ((System.ComponentModel.ISupportInitialize)pictureBox1).BeginInit();
            SuspendLayout();
            // 
            // dateTimePicker1
            // 
            dateTimePicker1.Location = new Point(130, 12);
            dateTimePicker1.Name = "dateTimePicker1";
            dateTimePicker1.Size = new Size(250, 27);
            dateTimePicker1.TabIndex = 0;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("Microsoft JhengHei UI", 12F, FontStyle.Bold, GraphicsUnit.Point);
            label1.Location = new Point(12, 14);
            label1.Name = "label1";
            label1.Size = new Size(112, 25);
            label1.TabIndex = 1;
            label1.Text = "請選擇日期";
            // 
            // title_textBox
            // 
            title_textBox.Location = new Point(6, 63);
            title_textBox.Multiline = true;
            title_textBox.Name = "title_textBox";
            title_textBox.ScrollBars = ScrollBars.Both;
            title_textBox.Size = new Size(368, 76);
            title_textBox.TabIndex = 2;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Font = new Font("Microsoft JhengHei UI", 12F, FontStyle.Bold, GraphicsUnit.Point);
            label2.Location = new Point(6, 23);
            label2.Name = "label2";
            label2.Size = new Size(132, 25);
            label2.TabIndex = 3;
            label2.Text = "新增新聞標題";
            // 
            // add_button
            // 
            add_button.Font = new Font("Microsoft JhengHei UI", 12F, FontStyle.Bold, GraphicsUnit.Point);
            add_button.Location = new Point(176, 18);
            add_button.Name = "add_button";
            add_button.Size = new Size(106, 34);
            add_button.TabIndex = 4;
            add_button.Text = "新增";
            add_button.UseVisualStyleBackColor = true;
            add_button.Click += add_button_Click;
            // 
            // groupBox1
            // 
            groupBox1.Controls.Add(pictureBox1);
            groupBox1.Controls.Add(label8);
            groupBox1.Controls.Add(label7);
            groupBox1.Controls.Add(label2);
            groupBox1.Controls.Add(start_button);
            groupBox1.Controls.Add(label6);
            groupBox1.Controls.Add(add_button);
            groupBox1.Controls.Add(label5);
            groupBox1.Controls.Add(title_textBox);
            groupBox1.Controls.Add(label4);
            groupBox1.Controls.Add(pictureBox1_ask);
            groupBox1.Location = new Point(12, 58);
            groupBox1.Name = "groupBox1";
            groupBox1.Size = new Size(382, 302);
            groupBox1.TabIndex = 5;
            groupBox1.TabStop = false;
            // 
            // label8
            // 
            label8.AutoSize = true;
            label8.Font = new Font("Microsoft JhengHei UI", 25.8000011F, FontStyle.Bold, GraphicsUnit.Point);
            label8.ForeColor = Color.Red;
            label8.Location = new Point(218, 136);
            label8.Name = "label8";
            label8.Size = new Size(64, 56);
            label8.TabIndex = 15;
            label8.Text = "%";
            // 
            // label7
            // 
            label7.AutoSize = true;
            label7.Font = new Font("Microsoft JhengHei UI", 13.8F, FontStyle.Bold, GraphicsUnit.Point);
            label7.Location = new Point(61, 63);
            label7.Name = "label7";
            label7.Size = new Size(201, 29);
            label7.TabIndex = 14;
            label7.Text = "BingChat回應中...";
            // 
            // start_button
            // 
            start_button.Font = new Font("Microsoft JhengHei UI", 12F, FontStyle.Bold, GraphicsUnit.Point);
            start_button.Location = new Point(138, 214);
            start_button.Name = "start_button";
            start_button.Size = new Size(80, 52);
            start_button.TabIndex = 7;
            start_button.Text = "開始";
            start_button.UseVisualStyleBackColor = true;
            start_button.Click += start_button_Click;
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Font = new Font("Microsoft JhengHei UI", 24F, FontStyle.Bold, GraphicsUnit.Point);
            label6.ForeColor = Color.Red;
            label6.Location = new Point(65, 142);
            label6.Name = "label6";
            label6.Size = new Size(139, 50);
            label6.TabIndex = 13;
            label6.Text = "label6";
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Font = new Font("Microsoft JhengHei UI", 12F, FontStyle.Bold, GraphicsUnit.Point);
            label5.Location = new Point(61, 76);
            label5.Name = "label5";
            label5.Size = new Size(157, 25);
            label5.TabIndex = 12;
            label5.Text = "預測股票指數為:";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Font = new Font("Microsoft JhengHei UI", 12F, FontStyle.Bold, GraphicsUnit.Point);
            label4.Location = new Point(65, 35);
            label4.Name = "label4";
            label4.Size = new Size(132, 25);
            label4.TabIndex = 11;
            label4.Text = "您的平均新聞";
            // 
            // pictureBox1_ask
            // 
            pictureBox1_ask.Image = (Image)resources.GetObject("pictureBox1_ask.Image");
            pictureBox1_ask.Location = new Point(6, 14);
            pictureBox1_ask.Name = "pictureBox1_ask";
            pictureBox1_ask.Size = new Size(368, 194);
            pictureBox1_ask.TabIndex = 13;
            pictureBox1_ask.TabStop = false;
            // 
            // title_listBox
            // 
            title_listBox.Font = new Font("Microsoft JhengHei UI", 13.8F, FontStyle.Bold, GraphicsUnit.Point);
            title_listBox.FormattingEnabled = true;
            title_listBox.ItemHeight = 29;
            title_listBox.Location = new Point(413, 8);
            title_listBox.MultiColumn = true;
            title_listBox.Name = "title_listBox";
            title_listBox.RightToLeft = RightToLeft.No;
            title_listBox.ScrollAlwaysVisible = true;
            title_listBox.Size = new Size(923, 352);
            title_listBox.TabIndex = 6;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Font = new Font("Microsoft JhengHei UI", 12F, FontStyle.Bold, GraphicsUnit.Point);
            label3.Location = new Point(34, 227);
            label3.Name = "label3";
            label3.Size = new Size(330, 25);
            label3.TabIndex = 8;
            label3.Text = "標題已全部新增完成請按\"開始\"分析";
            // 
            // ans_textBox
            // 
            ans_textBox.Location = new Point(456, 12);
            ans_textBox.Multiline = true;
            ans_textBox.Name = "ans_textBox";
            ans_textBox.ScrollBars = ScrollBars.Both;
            ans_textBox.Size = new Size(831, 363);
            ans_textBox.TabIndex = 9;
            // 
            // re_button
            // 
            re_button.Font = new Font("Microsoft JhengHei UI", 12F, FontStyle.Bold, GraphicsUnit.Point);
            re_button.ForeColor = Color.Red;
            re_button.Location = new Point(130, 272);
            re_button.Name = "re_button";
            re_button.Size = new Size(120, 52);
            re_button.TabIndex = 10;
            re_button.Text = "重新開始";
            re_button.UseVisualStyleBackColor = true;
            re_button.Click += re_button_Click;
            // 
            // pictureBox1
            // 
            pictureBox1.Location = new Point(304, 142);
            pictureBox1.Name = "pictureBox1";
            pictureBox1.Size = new Size(64, 56);
            pictureBox1.TabIndex = 16;
            pictureBox1.TabStop = false;
            // 
            // Ask1
            // 
            AutoScaleDimensions = new SizeF(9F, 19F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = Color.White;
            ClientSize = new Size(1348, 372);
            Controls.Add(re_button);
            Controls.Add(title_listBox);
            Controls.Add(ans_textBox);
            Controls.Add(label3);
            Controls.Add(groupBox1);
            Controls.Add(label1);
            Controls.Add(dateTimePicker1);
            Name = "Ask1";
            Text = "Ask1";
            groupBox1.ResumeLayout(false);
            groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)pictureBox1_ask).EndInit();
            ((System.ComponentModel.ISupportInitialize)pictureBox1).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private DateTimePicker dateTimePicker1;
        private Label label1;
        private TextBox title_textBox;
        private Label label2;
        private Button add_button;
        private GroupBox groupBox1;
        private ListBox title_listBox;
        private Button start_button;
        private Label label3;
        private TextBox ans_textBox;
        private Button re_button;
        private Label label4;
        private Label label5;
        private Label label6;
        private Label label7;
        private PictureBox pictureBox1_ask;
        private Label label8;
        private PictureBox pictureBox1;
    }
}