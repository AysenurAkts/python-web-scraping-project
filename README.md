# python-web-scraping-project

A Spyder project that scrapes markastok web pages using Python to create a dataset.

All metrics are saved in the local excel file and google sheets.

The project consists of two parts:

  •Part 1: Scraped required metrics from product pages
  
  •Part 2: This data was written into Google Sheets
  
  •Part 2: Sorting and Sending data with an Email 
  
 a. URL of the Report: https://docs.google.com/spreadsheets/d/1YP0YAw0Mkz8rifU88-lLrQWr6dZPuUYprMhCDTQSIz8/edit?usp=sharing
 
 b. Used tech-stack ( library/framework etc.): 
 
    • PYTHON
    
    • BEAUTIFUL SOUP
    
    • PANDAS
    
    • PYGSHEETS
    
 c. What were the problems I faced during the project development phase?
 
At first when scraping the metrics from the website, I couldn't get the metrics separately. Then I was able to scrape metrics based on class names. I was overwriting the data when saving these metrics to the Excel file. Then I used the mods in file saves. Thus, I did not lose the data in the file.
    
 d. What did I learn in this project?
 
I learned to scrape necessary metrics from a website. BeautifulSoup, Selenium, Scrapy libraries can be used for these processes. I chose to do the operations using BeautifulSoup. As I am new to web scraping, I chose this library as BeatifulSoup is easier to learn and develop. Also BeautifulSoup has extensive documentation for me to learn. There is good community support for solving problems that arise when working with this library. In the second stage, I learned to write the data to Google Sheets using Api. I went through the documentation for the api usage. I learned how to do the necessary operations for these api's.

1. If I’d have 10.000 urls that I should visit, then it takes hours to finish. What can we make to fasten this process?
We can use Scrapy or Selenium libraries for these processes. Thus, we can make faster transactions through the website. We can also delete Urls that do not point to products inside the Urls. We can make faster transactions by only processing on product URLs.

2. What can we make or use to automate this process to run once a day?
Windows Task Scheduler is a default Windows Application for managing tasks in response to an event-based or time-based trigger. With this application we can automate our processes.

3. What is API and how does it work?
API stands for Application Programming Interface. An API is a software intermediary that allows two applications to talk to each other.  In other words, an API is the messenger that delivers your request to the provider that you’re requesting it from and then delivers the response back to you. APIs work by sharing data and information between applications, systems, and devices—making it possible for these things to talk with each other.
