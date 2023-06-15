<h1 align="center">Review Detective</h1>

<p align="center">
  <img src="https://github.com/your-username/review-detective/blob/main/logo.png" alt="Review Detective Logo">
</p>

<p align="center">
  <strong>Review Detective</strong> is a web application that analyzes product reviews to determine if a product is good to buy or not. It utilizes sentiment analysis to provide insights into the overall sentiment of the reviews.
</p>

<h2>Table of Contents</h2>

<ul>
  <li><a href="#overview">Overview</a></li>
  <li><a href="#installation">Installation</a></li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#dependencies">Dependencies</a></li>
  <li><a href="#contributing">Contributing</a></li>
  <li><a href="#license">License</a></li>
</ul>

<h2 id="overview">Overview</h2>

<p>
  The Review Detective web application allows users to input the URL of a product and receive an analysis of the reviews for that product. The application scrapes reviews from the provided Amazon product link, performs sentiment analysis on the reviews, and presents the overall sentiment as a result. The sentiment analysis helps users make informed decisions about purchasing products based on the general sentiment of the reviews.
</p>

<h2 id="installation">Installation</h2>

<ol>
  <li>Clone the repository:</li>
</ol>

<pre><code>git clone https://github.com/your-username/review-detective.git
</code></pre>

<ol start="2">
  <li>Navigate to the project directory:</li>
</ol>

<pre><code>cd review-detective
</code></pre>

<ol start="3">
  <li>Create a virtual environment:</li>
</ol>

<pre><code>python -m venv venv
</code></pre>

<ol start="4">
  <li>Activate the virtual environment:</li>
</ol>

<ul>
  <li>On Windows:</li>
</ul>

<pre><code>venv\Scripts\activate
</code></pre>

<ul>
  <li>On macOS/Linux:</li>
</ul>

<pre><code>source venv/bin/activate
</code></pre>

<ol start="5">
  <li>Install the required dependencies:</li>
</ol>

<pre><code>pip install -r requirements.txt
</code></pre>

<h2 id="usage">Usage</h2>

<ol>
  <li>Run the Flask application:</li>
</ol>

<pre><code>flask run
</code></pre>

<ol start="2">
  <li>Open a web browser and navigate to <code>http://localhost:5000</code> to access the Review Detective web application.</li>
  <li>Enter the URL of a product in the provided input field and click the "Analyze" button.</li>
  <li>The application will scrape reviews from the provided Amazon product link, perform sentiment analysis on the reviews, and display the overall sentiment of the reviews.</li>
</ol>

<h2 id="dependencies">Dependencies</h2>

<p>
  The Review Detective application has the following dependencies:
</p>

<ul>
  <li>Flask: A lightweight web framework for Python.</li>
  <li>BeautifulSoup: A library for web scraping and parsing HTML.</li>
  <li>Selenium: A tool for automating web browser interactions.</li>
  <li>Transformers: A library for natural language processing (NLP) using pre-trained models.</li>
</ul>

<p>
  These dependencies are listed in the <code>requirements.txt</code> file and can be installed using <code>pip</code> (see the <a href="#installation">Installation</a> section).
</p>

<h2 id="contributing">Contributing</h2>

<p>
  Contributions to the Review Detective project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
</p>

<ol>
  <li>Fork the repository.</li>
  <li>Create a new branch for your feature or bug fix:</li>
</ol>

<pre><code>git checkout -b feature-name
</code></pre>

<ol start="3">
  <li>Make your changes and commit them:</li>
</ol>

<pre><code>git commit -m "Add feature-name"
</code></pre>

<ol start="4">
  <li>Push your changes to your forked repository:</li>
</ol>

<pre><code>git push origin feature-name
</code></pre>

<ol start="5">
  <li>Open a pull request on the main repository.</li>
</ol>

<h2 id="license">License</h2>

<p>
  Review Detective is licensed under the <a href="LICENSE">MIT License</a>.
</p>
