using BingChat;
using CsvHelper.Configuration;
using CsvHelper;
using Microsoft.VisualBasic;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace FinanceChatAI
{
    public partial class Ask1 : Form
    {
        private List<string> newsTitles = new List<string>();
        public Ask1()
        {
            InitializeComponent();
            pictureBox1.Visible = false;
            label4.Visible = false;
            label5.Visible = false;
            label6.Visible = false;
            label7.Visible = false;
            label8.Visible = false;
            pictureBox1_ask.Visible = false;
            re_button.Enabled = false;
            re_button.Visible = false;
            start_button.Enabled = true;
            start_button.Visible = true;
            ans_textBox.Visible = false;
            ans_textBox.Text = "";
            newsTitles.Clear();
            title_listBox.Items.Clear();
            MessageBox.Show("請記得貼上您的www.bing.com的cookie path於bing_cookies_myaccount.json");
            try
            {
                // 檢查文件夾是否已存在，如果不存在則創建它
                if (!Directory.Exists("ask"))
                {
                    Directory.CreateDirectory("ask");
                    Console.WriteLine("資料夾建立成功！");
                }
                else
                {
                    Console.WriteLine("資料夾已存在。");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"資料夾建立時發生錯誤：{ex.Message}");
            }
        }

        private void add_button_Click(object sender, EventArgs e)
        {
            string inputTitle = title_textBox.Text.Trim();
            if (!string.IsNullOrEmpty(inputTitle))
            {
                newsTitles.Add(inputTitle);
                title_listBox.Items.Add(inputTitle);
                title_textBox.Clear();
            }
        }
        string keyword = "台積電";
        string date;
        private void start_button_Click(object sender, EventArgs e)
        {
            DateTime selectedDateTime = dateTimePicker1.Value;

            // 获取日期
            DateTime selectedDate = selectedDateTime.Date;
            date = selectedDate.ToString("yyyy-MM-dd");
            ans_textBox.Text = date;
            keyword = Interaction.InputBox("輸入查詢的股票(ex: 台積電)", "確定", "台積電", 50, 50);//50,50視窗座標位置
            DialogResult result = MessageBox.Show("Bing chat聊天會耗時很久\n如果已有資料(預設是有的)請按否\n不要重跑!\n請問是否繼續?", "注意", MessageBoxButtons.YesNo, MessageBoxIcon.Warning);
            if (result == DialogResult.Yes)
            {
                InitializeAsync(); // 用異步初始化方法
                start_button.Enabled = false;
                start_button.Visible = false;

            }
            else
            {
                conclusion();
            }
        }


        private async void InitializeAsync()
        {
            ans_textBox.Visible = true;
            start_button.Enabled = false;
            start_button.Visible = false;
            label1.Visible = false;
            dateTimePicker1.Visible = false;
            label2.Visible = false;
            add_button.Visible = false;
            title_textBox.Visible = false;
            label3.Visible = false;
            start_button.Visible = false;
            title_listBox.Visible = false;
            label7.Visible = true;
            pictureBox1_ask.Visible = true;

            // 指定 CSV 檔案路徑
            string ans_path = "ask/ans_ask.csv";

            using (StreamWriter writer = new StreamWriter(ans_path, false, Encoding.UTF8)) // 使用 UTF-8 編碼
            {
                writer.WriteLine("date,title, Y/N");
            }

            // 定義資料類別以匹配 CSV 檔案中的結構


            //-------------主要修改區--------------------------------------------------------
            int i = 0;
            //string[] t = { "年底確定來不及！台積電中科2奈米廠用地延至明年交地" , "慘？市場傳三度調降財測 台積電急重訊澄清" };
            string[] answer = new string[newsTitles.Count];
            foreach (var record in newsTitles)
            {
                string keyword2 = keyword;
                string pythonScriptPath = "BingChat.py";
                //請找自己的python.exe路徑貼上
                string pythonInterpreter = "C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python311\\python.exe";
                //請寫入你的bingchat.json路徑，注意格式(python注重)
                //D:\Downloads\FinanceChatAI - 複製\FinanceChatAI\bin\Debug\net6.0-windows
                //string cookiepath = "D:/Downloads/FinanceChatAI - 複製/FinanceChatAI/bin/Debug/net6.0-windows/bingchat.json";
                string cookiepath = "bingchat.json";

                var message = "請您拿" + date + "當下5日內" + keyword2 + "的均線漲跌進行分析為漲還是跌，接著對以下新聞標題與其5日均線之漲跌經過綜合分析，並請考慮到當沖要獲利的話，必須價差超過股價的 0.435％才能獲利，那麼這個標題對公司隔日股票當沖是好(會賺錢)還是壞(不會賺錢)，接著請注意回答重點是:如果隔日股票會漲(會賺錢)請只回答#yes，而如果隔日股票會跌(不會賺錢)則只回答#no，如果不確定則只回答#unknown，請盡可能的不要回答#unknown，然後於下一行用簡短的句子進行詳細說明， 而以下為要分析的新聞標題:" + record;
                ans_textBox.AppendText(message + Environment.NewLine + Environment.NewLine);

                ProcessStartInfo psi = new ProcessStartInfo();
                psi.FileName = pythonInterpreter;
                psi.Arguments = $"{pythonScriptPath} \"{cookiepath}\" \"{message}\""; //傳參數給python   
                psi.UseShellExecute = false;
                psi.RedirectStandardOutput = true; // 捕獲輸出
                psi.CreateNoWindow = true;


                using (Process process = new Process())
                {
                    process.StartInfo = psi;
                    process.Start();


                    process.WaitForExit();

                    if (process.ExitCode == 0)
                    {
                        answer[i] = process.StandardOutput.ReadToEnd();//讀所有python輸出
                        ans_textBox.AppendText($"Answer: {answer[i]}" + Environment.NewLine + Environment.NewLine);
                        //Console.WriteLine($"Answer:\n {answer[i]}");

                        string pattern = @"(#unknown|#no|#yes)";

                        MatchCollection matches = Regex.Matches(answer[i], pattern);

                        foreach (Match match in matches)
                        {
                            string keywordText = match.Value;
                            // 寫入 CSV 資料行
                            using (StreamWriter writer = new StreamWriter(ans_path, true, Encoding.UTF8)) // 第二個參數為 true，表示追加模式 // 需要更動的地方
                            {
                                writer.WriteLine(date + "," + record + "," + keywordText);
                            }
                        }

                        i++;
                    }
                    else
                    {
                        Console.WriteLine("Python script execution failed.");
                    }
                }

            }
            //-------------主要修改區--------------------------------------------------------

            // Create an instance of StreamWriter to write text to a file.
            // The using statement also closes the StreamWriter.
            using (StreamWriter sw = new StreamWriter("ask/output_ask.TXT"))   //小寫TXT     
            {
                i = 0;
                foreach (var record in newsTitles)
                {
                    // Add some text to the file.
                    sw.WriteLine(date);
                    sw.WriteLine(record);
                    sw.WriteLine(answer[i]);
                    // Arbitrary objects can also be written to the file.
                    //sw.Write("The date is: ");
                    //sw.WriteLine(DateTime.Now);
                    i++;
                }
            }

            conclusion();
        }

        private Image ResizeImage(Image sourceImage, Size newSize)
        {
            // 调整图像大小
            Bitmap resizedImage = new Bitmap(newSize.Width, newSize.Height);
            using (Graphics g = Graphics.FromImage(resizedImage))
            {
                g.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.HighQualityBicubic;
                g.DrawImage(sourceImage, 0, 0, newSize.Width, newSize.Height);
            }
            return resizedImage;
        }

        void conclusion()
        {
            ans_textBox.Visible = true;
            start_button.Enabled = false;
            start_button.Visible = false;
            label1.Visible = false;
            dateTimePicker1.Visible = false;
            label2.Visible = false;
            add_button.Visible = false;
            title_textBox.Visible = false;
            label3.Visible = false;
            start_button.Visible = false;
            title_listBox.Visible = false;
            label7.Visible = true;
            pictureBox1_ask.Visible = true;
            //此處的py檔有修改(應該會放在.exe同層)，如果您的資料夾沒有我提供的py檔，請向使用者索取
            string stockSymbol = Interaction.InputBox("請輸入股票代號(ex:2330)", "確定", "2330", 50, 50);//50,50視窗座標位置
            string pythonScriptPath = "Conclusion_ask.py";
            string pythonInterpreter = "C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python311\\python.exe";

            ProcessStartInfo psi = new ProcessStartInfo();
            psi.FileName = pythonInterpreter;
            psi.Arguments = $"{pythonScriptPath} \"{stockSymbol}\""; // 傳遞股票代號作為參數
            psi.UseShellExecute = false;
            psi.RedirectStandardOutput = true; // 捕獲輸出
            psi.CreateNoWindow = true;
            label7.Visible = false;
            pictureBox1_ask.Visible = false;
            label4.Visible = true;
            label5.Visible = true;
            label6.Visible = true;
            using (Process process = new Process())
            {
                process.StartInfo = psi;
                process.Start();

                // 捕獲 Python 腳本的輸出
                string output = process.StandardOutput.ReadToEnd();
                process.WaitForExit();

                // 從輸出中解析平均結論值
                string averageConclusionText = "平均結論值：";
                //string imgfile = "股市指標圖";
                //int index = output.IndexOf(averageConclusionText);
                //int index2 = output.IndexOf(imgfile);
                string pattern = @"(?<=平均結論值：)\d+";
                Match match = Regex.Match(output, pattern);
                if (match.Success)
                {
                    string averageValue = match.Value;
                    //Console.WriteLine("Average Value: " + averageValue);

                    string imagePath = "";
                    //Console.WriteLine("Remaining Text: " + remainingText);
                    label6.Text = (averageValue);
                    if (int.Parse(averageValue) > 50)
                    {
                        imagePath = "股市指標圖/正正.png";
                    }
                    else if (int.Parse(averageValue) < 50 & int.Parse(averageValue)>0)
                    {
                        imagePath = "股市指標圖/正.png";
                    }
                    else if (int.Parse(averageValue) == 0)
                    {
                        imagePath = "股市指標圖/普通.png";
                    }
                    else if (int.Parse(averageValue) < 0 & int.Parse(averageValue) > -50)
                    {
                        imagePath = "股市指標圖/負.png";
                    }
                    else if (int.Parse(averageValue) < -50)
                    {
                        imagePath = "股市指標圖/負負.png";
                    }
                    Image image = Image.FromFile(imagePath);
                    pictureBox1.Image = ResizeImage(image, pictureBox1.Size);
                    pictureBox1.Visible = true;
                    label8.Visible = true;
                }
                else
                {
                    Console.WriteLine("No match found.");
                }
            }
            re_button.Visible = true;
            re_button.Enabled = true;
        }

        private void re_button_Click(object sender, EventArgs e)
        {

            start_button.Enabled = true;
            start_button.Visible = true;
            label1.Visible = true;
            dateTimePicker1.Visible = true;
            label2.Visible = true;
            add_button.Visible = true;
            title_textBox.Visible = true;
            label3.Visible = true;
            start_button.Visible = true;
            title_listBox.Visible = true;

            label4.Visible = false;
            label5.Visible = false;
            label6.Visible = false;
            label7.Visible = false;
            label8.Visible = false;
            pictureBox1_ask.Visible = false;
            re_button.Enabled = false;
            re_button.Visible = false;
            start_button.Enabled = true;
            start_button.Visible = true;
            ans_textBox.Visible = false;
            MessageBox.Show("請記得貼上您的www.bing.com的cookie path於bing_cookies_myaccount.json");
            try
            {
                // 檢查文件夾是否已存在，如果不存在則創建它
                if (!Directory.Exists("ask"))
                {
                    Directory.CreateDirectory("ask");
                    Console.WriteLine("資料夾建立成功！");
                }
                else
                {
                    Console.WriteLine("資料夾已存在。");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"資料夾建立時發生錯誤：{ex.Message}");
            }
            ans_textBox.Text = "";
            newsTitles.Clear();
            title_listBox.Items.Clear();
        }
    }
}
