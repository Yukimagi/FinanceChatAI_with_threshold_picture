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
using static System.Windows.Forms.VisualStyles.VisualStyleElement;
using System.Linq;

namespace FinanceChatAI
{
    public partial class Forecast1 : Form
    {
        public Forecast1()
        {
            InitializeComponent();
            pictureBox4.Visible = false;
            button1.Visible = false;
            pictureBox2.Visible = true;
            pictureBox1.Visible = true;
            Forecast_label2.Visible = true;
            Forecast_label9.Visible = true;
            btn_check.Visible = true;
            btn_check.Enabled = true;
            Forecast_comboBox1.Visible = true;
            Forecast_comboBox1.Enabled = true;
            pictureBox3.Visible = false;
            Forecast_label3.Visible = false;
            Forecast_label4.Visible = false;
            Forecast_label5.Visible = false;
            Forecast_label6.Visible = false;
            Forecast_label7_point.Visible = false;
            Forecast_label8.Visible = false;
            MessageBox.Show("請記得貼上您的www.bing.com的cookie path於bing_cookies_myaccount.json");
            try
            {
                // 檢查文件夾是否已存在，如果不存在則創建它
                if (!Directory.Exists("forecast"))
                {
                    Directory.CreateDirectory("forecast");
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
        string keyword = "台積電";
        void filter()
        {
            //此處的py檔有修改(應該會放在.exe同層)，如果您的資料夾沒有我提供的py檔，請向使用者索取
            keyword = Interaction.InputBox("輸入查詢的股票(ex: 台積電)", "確定", "台積電", 50, 50);//50,50視窗座標位置
            string pythonScriptPath = "news_filter_now.py";
            string pythonInterpreter = "C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python311\\python.exe";

            ProcessStartInfo psi = new ProcessStartInfo();
            psi.FileName = pythonInterpreter;
            psi.Arguments = $"{pythonScriptPath} \"{keyword}\""; // 傳遞關鍵字作為參數
            psi.UseShellExecute = false;
            psi.CreateNoWindow = true;

            using (Process process = new Process())
            {
                process.StartInfo = psi;
                process.Start();
                process.WaitForExit();
            }
        }

        int daysToKeep = 0;
        private void btn_check_Click(object sender, EventArgs e)
        {
            Forecast_label3.Visible = false;
            Forecast_label4.Visible = false;
            Forecast_label5.Visible = false;
            Forecast_label6.Visible = false;
            Forecast_label7_point.Visible = false;
            Forecast_label8.Visible = false;

            DialogResult result = MessageBox.Show("Bing chat聊天會耗時很久\n如果已有資料(預設是有的)請按否\n不要重跑!\n請問是否繼續?", "注意", MessageBoxButtons.YesNo, MessageBoxIcon.Warning);
            if (result == DialogResult.Yes)
            {
                daysToKeep = Forecast_comboBox1.SelectedIndex + 1;
                //Forecast_textBox1.Text = daysToKeep.ToString();
                pictureBox3.Visible = true;
                Forecast_label4.Visible = true;

                DialogResult result2 = MessageBox.Show("請問是否要開始爬資料\n如果已有資料(預設是有的)請按否\n不要重跑!\n請問是否繼續?", "注意", MessageBoxButtons.YesNo, MessageBoxIcon.Warning);
                if (result2 == DialogResult.Yes)
                {
                    // 設定 Python 檔案的路徑
                    string pythonScriptPath = "catch_news_now.py";

                    // 設定 Python 執行器的路徑(自己去搜尋自己電腦的python.exe的路徑)
                    string pythonInterpreter = "C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python311\\python.exe";

                    // 建立 ProcessStartInfo 物件來設定執行參數
                    ProcessStartInfo psi = new ProcessStartInfo();
                    psi.FileName = pythonInterpreter;
                    psi.Arguments = pythonScriptPath;
                    psi.UseShellExecute = false;
                    psi.CreateNoWindow = true;

                    // 執行 Python 腳本
                    using (Process process = new Process())
                    {
                        process.StartInfo = psi;
                        process.Start();
                        process.WaitForExit();
                    }
                    filter();

                }
                InitializeAsync(); // 用異步初始化方法
            }
        }

        private async void InitializeAsync()
        {
            pictureBox2.Visible = false;
            //pictureBox1.Visible = false;
            Forecast_label2.Visible = false;
            Forecast_label9.Visible = false;
            btn_check.Visible = false;
            btn_check.Enabled = false;
            Forecast_comboBox1.Visible = false;
            Forecast_comboBox1.Enabled = false;

            pictureBox3.Visible = false;
            Forecast_label4.Visible = false;

            Forecast_label3.Visible = true;
            // 指定 CSV 檔案路徑
            string news_path = "forecast/news_now_filter.csv";
            string ans_path = "forecast/ans_forcast.csv";

            using (StreamWriter writer = new StreamWriter(ans_path, false, Encoding.UTF8)) // 使用 UTF-8 編碼
            {
                writer.WriteLine("date,title, Y/N");
            }

            // 定義資料類別以匹配 CSV 檔案中的結構
            int num = 0;
            int num2 = 0;

            var record0 = new List<Dictionary<string, string>>();
            var records = new List<Dictionary<string, string>>();
            var dates = new HashSet<string>(); // 使用 HashSet 来存储不重复的日期
            // 讀取 2330_2022.csv(or每個月) 檔案
            using (var reader = new StreamReader(news_path))
            using (var csv = new CsvReader(reader, new CsvConfiguration(CultureInfo.InvariantCulture)))
            {
                csv.Read();
                csv.ReadHeader();

                while (csv.Read())
                {
                    var record = new Dictionary<string, string>();
                    foreach (var header in csv.HeaderRecord)
                    {
                        record[header] = csv.GetField(header);
                    }

                    string date = record["date"];
                    if (!dates.Contains(date))
                    {
                        dates.Add(date); // 添加新的日期
                        if (dates.Count > daysToKeep)
                        {
                            break; // 如果日期数量超过了 daysToKeep，跳出循环
                        }
                    }

                    record0.Add(record);

                }
            }

            foreach (var date in dates)
            {
                foreach (var record in record0)
                {
                    if (record["date"] == date)
                    {
                        Forecast_textBox1.AppendText("\n" + $"Date: {record["date"]}, Title: {record["title"]}" + Environment.NewLine + Environment.NewLine);
                        records.Add(record);
                        num2++;
                    }
                }
            }
            //-------------主要修改區--------------------------------------------------------
            int i = 0;
            string[] answer = new string[num2];
            foreach (var record in records)
            {
                string keyword2 = keyword;
                string pythonScriptPath = "BingChat.py";
                //請找自己的python.exe路徑貼上
                string pythonInterpreter = "C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python311\\python.exe";
                //請寫入你的bingchat.json路徑，注意格式(python注重)
                //D:\Downloads\FinanceChatAI - 複製\FinanceChatAI\bin\Debug\net6.0-windows
                //string cookiepath = "D:/Downloads/FinanceChatAI - 複製/FinanceChatAI/bin/Debug/net6.0-windows/bingchat.json";
                string cookiepath = "bingchat.json";

                var message = "請您拿" + record["date"] + "當下5日內" + keyword2 + "的均線漲跌進行分析為漲還是跌，接著對以下新聞標題與其5日均線之漲跌經過綜合分析，並請考慮到當沖要獲利的話，必須價差超過股價的 0.435％才能獲利，那麼這個標題對公司隔日股票當沖是好(會賺錢)還是壞(不會賺錢)，接著請注意回答重點是:如果隔日股票會漲(會賺錢)請只回答#yes，而如果隔日股票會跌(不會賺錢)則只回答#no，如果不確定則只回答#unknown，請盡可能的不要回答#unknown，然後於下一行用簡短的句子進行詳細說明， 而以下為要分析的新聞標題:" + record["title"];
                Forecast_textBox1.AppendText(message + Environment.NewLine + Environment.NewLine);

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
                        Forecast_textBox1.AppendText(message + Environment.NewLine + Environment.NewLine);

                        Forecast_textBox1.AppendText($"Answer: {answer[i]}" + Environment.NewLine + Environment.NewLine);
                        //Console.WriteLine($"Answer:\n {answer[i]}");

                        string pattern = @"(#unknown|#no|#yes)";

                        MatchCollection matches = Regex.Matches(answer[i], pattern);

                        foreach (Match match in matches)
                        {
                            string keywordText = match.Value;
                            // 寫入 CSV 資料行
                            using (StreamWriter writer = new StreamWriter(ans_path, true, Encoding.UTF8)) // 第二個參數為 true，表示追加模式 // 需要更動的地方
                            {
                                writer.WriteLine(record["date"] + "," + record["title"] + "," + keywordText);
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
            using (StreamWriter sw = new StreamWriter("forecast/output_forcast.TXT"))   //小寫TXT     
            {
                i = 0;
                foreach (var record in records)
                {
                    // Add some text to the file.
                    sw.WriteLine(record["date"]);
                    sw.WriteLine(record["title"]);
                    sw.WriteLine(answer[i]);
                    // Arbitrary objects can also be written to the file.
                    //sw.Write("The date is: ");
                    //sw.WriteLine(DateTime.Now);
                    i++;
                }
            }
            Forecast_label3.Visible = false;
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
            Forecast_label5.Visible = true;
            Forecast_label6.Visible = true;
            //此處的py檔有修改(應該會放在.exe同層)，如果您的資料夾沒有我提供的py檔，請向使用者索取
            string stockSymbol = Interaction.InputBox("請輸入股票代號(ex:2330)", "確定", "2330", 50, 50);//50,50視窗座標位置
            string pythonScriptPath = "Conclusion_Forecast.py";
            string pythonInterpreter = "C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python311\\python.exe";

            ProcessStartInfo psi = new ProcessStartInfo();
            psi.FileName = pythonInterpreter;
            psi.Arguments = $"{pythonScriptPath} \"{stockSymbol}\""; // 傳遞股票代號作為參數
            psi.UseShellExecute = false;
            psi.RedirectStandardOutput = true; // 捕獲輸出
            psi.CreateNoWindow = true;

            using (Process process = new Process())
            {
                process.StartInfo = psi;
                process.Start();

                // 捕獲 Python 腳本的輸出
                string output = process.StandardOutput.ReadToEnd();
                process.WaitForExit();

                // 從輸出中解析平均結論值
                string averageConclusionText = "平均結論值：";

                int index = output.IndexOf(averageConclusionText);
                if (index != -1)
                {
                    string averageValue = output.Substring(index + averageConclusionText.Length);
                    Forecast_label7_point.Text = (averageValue);
                    Forecast_label7_point.Visible = true;
                    Forecast_label8.Visible = true;
                    string imagePath = "";
                    /*
                    if (int.Parse(averageValue) > 50)
                    {
                        imagePath = "股市指標圖/正正.png";
                    }
                    else if (int.Parse(averageValue) < 50 & int.Parse(averageValue) > 0)
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
                    pictureBox4.Image = ResizeImage(image, pictureBox1.Size);
                    pictureBox4.Visible = true;
                    */
                }
            }
            button1.Visible = true;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            button1.Visible = false;
            pictureBox2.Visible = true;
            pictureBox1.Visible = true;
            Forecast_label2.Visible = true;
            Forecast_label9.Visible = true;
            btn_check.Visible = true;
            btn_check.Enabled = true;
            Forecast_comboBox1.Visible = true;
            Forecast_comboBox1.Enabled = true;
            pictureBox3.Visible = false;
            Forecast_label3.Visible = false;
            Forecast_label4.Visible = false;
            Forecast_label5.Visible = false;
            Forecast_label6.Visible = false;
            Forecast_label7_point.Visible = false;
            Forecast_label8.Visible = false;
            MessageBox.Show("請記得貼上您的www.bing.com的cookie path於bing_cookies_myaccount.json");
            try
            {
                // 檢查文件夾是否已存在，如果不存在則創建它
                if (!Directory.Exists("forecast"))
                {
                    Directory.CreateDirectory("forecast");
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
    }
}
