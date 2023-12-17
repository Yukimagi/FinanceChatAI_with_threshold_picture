using BingChat;
using CsvHelper.Configuration;
using CsvHelper;
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
using Microsoft.VisualBasic;//1.到“專案” → “加入參考(visualbasic” → “參考管理員”
                            //2.並最後using就可使用input box

namespace FinanceChatAI
{
    public partial class Research1 : Form
    {
        public Research1()
        {
            InitializeComponent();
            MessageBox.Show("請記得貼上您的www.bing.com的cookie path於bing_cookies_myaccount.json");
            //InitializeAsync(); // 用異步初始化方法
            MessageBox.Show("請注意是否有為自己的電腦裝好需要的python import檔~");
        }

        private void btn_NewsCatch_Click(object sender, EventArgs e)
        {
            DialogResult result = MessageBox.Show("爬整年資料會耗時很久\n如果已有資料(預設是有的)請按否\n不要重跑!\n請問是否繼續?", "注意", MessageBoxButtons.YesNo, MessageBoxIcon.Warning);
            if (result == DialogResult.Yes)
            {
                // 設定 Python 檔案的路徑
                string pythonScriptPath = "news_catch.py";

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
                MessageBox.Show("爬蟲新聞成功");
            }
        }

        private void btn_NewsFilter_Click(object sender, EventArgs e)
        {
            // 獲取輸入用戶的關鍵字和股票代號
            string keyword = Interaction.InputBox("輸入查詢的股票的台灣代稱(ex: 台積電)", "確定", "台積電", 50, 50);
            string stockCode = Interaction.InputBox("輸入股票代碼(ex: 2330)", "確定", "2330", 50, 50);


            string folderPath = keyword + "過濾新聞"; // 指定要创建的文件夹路径

            try
            {
                // 檢查文件夾是否已存在，如果不存在則創建它
                if (!Directory.Exists(folderPath))
                {
                    Directory.CreateDirectory(folderPath);
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

            string pythonScriptPath = "news_filter.py";
            string pythonInterpreter = "C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python311\\python.exe";

            ProcessStartInfo psi = new ProcessStartInfo();
            psi.FileName = pythonInterpreter;
            psi.Arguments = $"{pythonScriptPath} \"{keyword}\" \"{stockCode}\""; // 将关键字和股票代号作为参数传递
            psi.UseShellExecute = false;
            psi.CreateNoWindow = true;

            using (Process process = new Process())
            {
                process.StartInfo = psi;
                process.Start();
                process.WaitForExit();
            }
            MessageBox.Show("新聞過濾成功");

        }

        private void btn_IntradayReturn_Click(object sender, EventArgs e)
        {

            try
            {
                // 檢查文件夾是否已存在，如果不存在則創建它
                if (!Directory.Exists("Intraday return"))
                {
                    Directory.CreateDirectory("Intraday return");
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

            //此處的py檔有修改(應該會放在.exe同層)，如果您的資料夾沒有我提供的py檔，請向使用者索取
            string stockSymbol = Interaction.InputBox("輸入查詢的股票檔案(ex:2330.TW)\n詳情可搜尋yahoo finance", "確定", "2330.TW", 50, 50);//50,50視窗座標位置
            string pythonScriptPath = "Intraday_return.py";
            string pythonInterpreter = "C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python311\\python.exe";

            ProcessStartInfo psi = new ProcessStartInfo();
            psi.FileName = pythonInterpreter;
            psi.Arguments = $"{pythonScriptPath} \"{stockSymbol}\""; // 傳遞關鍵字作為參數
            psi.UseShellExecute = false;
            psi.CreateNoWindow = true;

            using (Process process = new Process())
            {
                process.StartInfo = psi;
                process.Start();
                process.WaitForExit();
            }
            MessageBox.Show("Intraday return成功");
        }
        string month = "1";
        string stock = "2330";
        string keyword2 = "台積電";

        void check()
        {
            if (0 < Convert.ToInt32(month) && Convert.ToInt32(month) < 13)
            {
                keyword2 = Interaction.InputBox("輸入查詢的股票的台灣代稱(ex: 台積電)", "確定", "台積電", 50, 50);
                stock = Interaction.InputBox("輸入股票代碼(ex: 2330)", "確定", "2330", 50, 50);
                DialogResult result = MessageBox.Show("請問是要查詢2023年" + month + "月的嗎\n如果是請按是\n如果是2022年請按否", "注意", MessageBoxButtons.YesNo, MessageBoxIcon.Warning);
                if (result == DialogResult.Yes)
                {
                    month = "23_" + month;
                }
                InitializeAsync(); // 用異步初始化方法
            }
            else
            {
                DialogResult result = MessageBox.Show("月份輸入錯誤，請重新輸入，或按取消已結束此動作", "注意", MessageBoxButtons.YesNo, MessageBoxIcon.Warning);
                if (result == DialogResult.Yes)
                {
                    check();
                }
            }
        }
        private void btn_BingChat_Click(object sender, EventArgs e)
        {
            DialogResult result = MessageBox.Show("Bing chat聊天會耗時很久\n如果已有資料(預設是有的)請按否\n不要重跑!\n請問是否繼續?", "注意", MessageBoxButtons.YesNo, MessageBoxIcon.Warning);
            if (result == DialogResult.Yes)
            {
                month = Interaction.InputBox("請輸入月份(ex:1)", "確定", "1", 50, 50);//50,50視窗座標位置
                check();
            }
        }
        private async void InitializeAsync()
        {
            // 指定 CSV 檔案路徑

            int path = 10;

            int j = 0;

            try
            {
                // 檢查文件夾是否已存在，如果不存在則創建它
                if (!Directory.Exists(stock + "ans"))
                {
                    Directory.CreateDirectory(stock + "ans");
                    textBox1.Text = ("資料夾建立成功！" + Environment.NewLine);
                }
                else
                {
                    textBox1.Text = ("資料夾已存在。" + Environment.NewLine);
                }
            }
            catch (Exception ex)
            {
                textBox1.Text = ($"資料夾建立時發生錯誤：{ex.Message}" + Environment.NewLine);
            }

            // 寫入 CSV 標題行
            using (StreamWriter writer = new StreamWriter(stock + "ans" + "/" + stock + "ans_" + month + ".csv", false, Encoding.UTF8)) // 使用 UTF-8 編碼
            {
                writer.WriteLine("date,title, Y/N");
            }


            // 定義資料類別以匹配 CSV 檔案中的結構
            int num = 0;
            var records = new List<Dictionary<string, string>>();
            // 讀取 2330_2022.csv(or每個月) 檔案
            using (var reader = new StreamReader(keyword2 + "過濾新聞" + "/" + stock + "_" + month + ".csv"))
            using (var csv = new CsvReader(reader, new CsvConfiguration(CultureInfo.InvariantCulture)))
            {
                csv.Read(); // 讀取第一行作為欄位標題
                csv.ReadHeader(); // 將第一行設定為欄位標題

                // 將 news_1.csv 檔案中的資料讀取為字典列表
                //var records = new List<Dictionary<string, string>>();
                while (csv.Read())
                {
                    var record = new Dictionary<string, string>();
                    foreach (var header in csv.HeaderRecord)
                    {
                        record[header] = csv.GetField(header);
                    }
                    records.Add(record);
                    num++;
                }

                // 處理字典列表中的資料
                foreach (var record in records)
                {
                    textBox1.AppendText($"Date: {record["date"]}, Title: {record["title"]}\n" + Environment.NewLine);
                }
            }
            //-------------主要修改區--------------------------------------------------------
            int i = 0;
            string[] answer = new string[num];
            foreach (var record in records)
            {
                //string keyword2 = keyword;
                string pythonScriptPath = "BingChat.py";
                //請找自己的python.exe路徑貼上
                string pythonInterpreter = "C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python311\\python.exe";
                //請寫入你的bingchat.json路徑，注意格式(python注重)
                //D:\Downloads\FinanceChatAI - 複製\FinanceChatAI\bin\Debug\net6.0-windows
                //string cookiepath = "D:/Downloads/FinanceChatAI - 複製/FinanceChatAI/bin/Debug/net6.0-windows/bingchat.json";
                string cookiepath = "bingchat.json";

                var message = "請您拿" + record["date"] + "當下5日內" + keyword2 + "的均線漲跌進行分析為漲還是跌，接著對以下新聞標題與其5日均線之漲跌經過綜合分析，並請考慮到當沖要獲利的話，必須價差超過股價的 0.435％才能獲利，那麼這個標題對公司隔日股票當沖是好(會賺錢)還是壞(不會賺錢)，接著請注意回答重點是:如果隔日股票會漲(會賺錢)請只回答#yes，而如果隔日股票會跌(不會賺錢)則只回答#no，如果不確定則只回答#unknown，請盡可能的不要回答#unknown，然後於下一行用簡短的句子進行詳細說明， 而以下為要分析的新聞標題:" + record["title"];


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
                        textBox1.AppendText($"answer: {answer[i]}\n" + Environment.NewLine + Environment.NewLine);
                        //Console.WriteLine($"Answer:\n {answer[i]}");

                        string pattern = @"(#unknown|#no|#yes)";

                        MatchCollection matches = Regex.Matches(answer[i], pattern);

                        foreach (Match match in matches)
                        {
                            string keywordText = match.Value;
                            // 寫入 CSV 資料行
                            using (StreamWriter writer = new StreamWriter(stock + "ans" + "/" + stock + "ans_" + month + ".csv", true, Encoding.UTF8)) // 第二個參數為 true，表示追加模式 // 需要更動的地方
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
            using (StreamWriter sw = new StreamWriter(stock + "ans" + "/" + "output_" + stock + "ans_" + month + ".TXT"))   //小寫TXT     
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
            MessageBox.Show("Bing Chat回答完成!" + Environment.NewLine);
        }

        private void btn_Conclusion_Click(object sender, EventArgs e)
        {
            //此處的py檔有修改(應該會放在.exe同層)，如果您的資料夾沒有我提供的py檔，請向使用者索取
            string stockSymbol = Interaction.InputBox("請輸入股票代號(ex:2330)", "確定", "2330", 50, 50);//50,50視窗座標位置

            try
            {
                // 檢查文件夾是否已存在，如果不存在則創建它
                if (!Directory.Exists(stockSymbol + "_conclusion"))
                {
                    Directory.CreateDirectory(stockSymbol + "_conclusion");
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

            string pythonScriptPath = "Conclusion.py";
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

                string averageConclusionText2 = "總獲利期望值：";
                int index2 = output.IndexOf(averageConclusionText2);
                if (index2 != -1)
                {
                    string profitValue = output.Substring(index2 + averageConclusionText2.Length);
                    MessageBox.Show($"總獲利期望值：{profitValue}元");
                }
            }
            MessageBox.Show("結論已產生!");
        }
    }
}
