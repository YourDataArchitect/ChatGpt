<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🤖 ChatGPT Automation Bot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            padding: 20px;
            max-width: 800px;
            margin: auto;
        }
        h1, h2, h3 {
            color: #343a40;
        }
        .header {
            text-align: center;
            padding-bottom: 20px;
            border-bottom: 2px solid #ccc;
        }
        .section {
            background-color: #fff;
            padding: 20px;
            margin: 15px 0;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        code {
            background-color: #eaeaea;
            padding: 2px 5px;
            border-radius: 4px;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            font-size: 0.9em;
            color: #666;
        }
        a {
            color: #0066cc;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🤖 ChatGPT Automation Bot</h1>
        <p>A Python-based automated bot for seamless interaction with ChatGPT.</p>
    </div>

    <div class="section">
        <h2>🌟 Features</h2>
        <ul>
            <li>Automated browser interaction using Selenium and Undetected Chromedriver.</li>
            <li>Secure login and token verification.</li>
            <li>Collects prompts and ChatGPT responses into an organized CSV file.</li>
            <li>Randomized User-Agent to prevent bot detection.</li>
        </ul>
    </div>

    <div class="section">
        <h2>⚙️ Installation & Usage</h2>
        <ol>
            <li>Clone the repository:
                <pre><code>git clone https://github.com/yourusername/chatgpt-bot.git</code></pre>
            </li>
            <li>Install dependencies:
                <pre><code>pip install selenium pandas undetected-chromedriver</code></pre>
            </li>
            <li>Run the script:
                <pre><code>python chatgpt_bot.py</code></pre>
            </li>
        </ol>
    </div>

    <div class="section">
        <h2>🚧 Requirements</h2>
        <ul>
            <li>Python 3.8 or higher</li>
            <li>Google Chrome browser</li>
            <li>Chromedriver (included)</li>
        </ul>
    </div>

    <div class="section">
        <h2>📝 Output</h2>
        <p>Interactions are saved in <code>out_put.csv</code>, clearly documenting all ChatGPT responses.</p>
    </div>

    <div class="footer">
        <p>Made with ❤️ by <a href="https://github.com/yourusername">Your Name</a></p>
    </div>

</body>
</html>
