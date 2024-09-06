# BibleWebsite
*Your ultimate Bible website for detailed commentaries, full chapters, and multiple translations to enhance your study.*

## Description
This Bible web application allows users to read and explore different translations of the Bible, view specific books and chapters, and access related commentaries. The application is built using Flask, a Python web framework, and integrates content scraped from external websites.

## Features
- **Homepage:** Displays a list of all available Bible books.
- **Bible Reader:** Allows users to read Bible chapters from different translations.
- **Commentary Section:** Provides commentary for specific Bible chapters.
- **Responsive Design:** The user interface is designed to be responsive and user-friendly.

## Technologies Used
- **Python:** Programming language for server-side logic.
- **Flask:** Web framework for building the application.
- **BeautifulSoup:** Library used for web scraping and parsing HTML content.
- **HTML/CSS:** For structuring and styling web pages.
- **JavaScript:** For additional interactivity and functionality.

## Project Structure
- **server.py:** Contains the main application logic, including route handling and any other server-side code necessary for the application.

- **static/:** Holds all static assets for your application, organized by type:

    - **css/style.css:** A stylesheet used to style the web application.

    - **image/blogo.png:** A logo image used in the application.

    - **javascript/app.js:** JavaScript file for adding interactive functionality to the web application.

    - **data_details.json:** A JSON file containing data details, such as translations and book information.

- **templates/:** Contains all HTML templates used to render different pages of your application:

    - **home.html:** Template for the homepage.

    - **bible.html:** Template for displaying Bible chapters for reading.

    - **commentary.html:** Template for displaying Bible commentary.
- **requrements.txt:** Lists all Python libraries and versions required for the project.

## Prerequisites
  - Python 3.8+
  - Pip (Python package installer)
  - An active internet connection (for scraping content from Bible.com and Enduring Word)
  - Install all necessary Python libraries using the ```requirements.txt``` file to ensure the application functions correctly.
    
## Installation
- ### Step-by-Step Installation
  1. **Clone the repository**:
         ```
         git clone https://github.com/your-username/BibleWebsite.git
         cd BibleWebsite
         ```
  2. **Create a virtual environment:** This step is optional but recommended to manage dependencies seperately from other projects.
         ```
         python3 -m venv venv
         source venv/bin/activate   # On Windows, use 'venv\Scripts\activate'
         ```
  3. **Install dependencies:** Install all the neccessary python using the                           ```requirements.txt``` file.
         ```pip install -r requirements.txt```
  4. **Run the Flask app:** Start the flask developement server to run the applicaion
         ```flask run```
  5. **Navigate to the app:** Open your web browser and visit http://127.0.0.1:5000 to view the application.

## Usage
- Navigate to the homepage to view the list of available Bible books.
- Click on any book to view its chapters in a specified translation.
- Switch between translations using the navigation menu.
- Access commentaries for each chapter to gain insights and understanding.

## Note
- This app scrapes content from external websites like Bible.com and Enduring Word.
- Make sure your internet connection is active to fetch and display the content.
  
## Acknowledgements
- Bible Verses: Bible.com.
- Commentary: Enduring Word.
- Icons: Font Awesome.

