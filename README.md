# BibleWebsite
*Your ultimate Bible website for detailed commentaries, full chapters, and multiple translations to enhance your study.*

## Description
This Bible web application allows users to read and explore different translations of the Bible, view specific books and chapters, and access related commentaries. The application is built using Flask, a Python web framework, and integrates content scraped from external websites.

## Features
Homepage: Displays a list of all available Bible books.
Bible Reader: Allows users to read Bible chapters from different translations.
Commentary Section: Provides commentary for specific Bible chapters.
Responsive Design: The user interface is designed to be responsive and user-friendly.

## Technologies Used
- Python: Programming language for server-side logic.
- Flask: Web framework for building the application.
- BeautifulSoup: Library used for web scraping and parsing HTML content.
- HTML/CSS: For structuring and styling web pages.
- JavaScript: For additional interactivity and functionality.

## Project Structure
server.py: Contains the main application logic, including route handling and any other server-side code necessary for the application.

static/: Holds all static assets for your application, organized by type:

css/style.css: A stylesheet used to style the web application.

image/blogo.png: A logo image used in the application.

javascript/app.js: JavaScript file for adding interactive functionality to the web application.

data_details.json: A JSON file containing data details, such as translations and book information.

templates/: Contains all HTML templates used to render different pages of your application:

home.html: Template for the homepage.

bible.html: Template for displaying Bible chapters for reading.

commentary.html: Template for displaying Bible commentary.

## Usage
Navigate to the homepage to view the list of available Bible books.
Click on any book to view its chapters in a specified translation.
Switch between translations using the navigation menu.
Access commentaries for each chapter to gain insights and understanding.

## Note
The application scrapes content from external websites, such as Bible.com and Enduring Word, to retrieve Bible verses and commentary. 
Ensure that your internet connection is active to access and display the scraped content.

## Acknowledgements
The application uses Bible.com for Bible verse content.
Commentary content is sourced from Enduring Word.
Front-end icons are provided by Font Awesome.

