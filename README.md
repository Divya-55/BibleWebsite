![home page](https://github.com/user-attachments/assets/fa6beee6-6324-45c6-a69b-80b6534dd8c0)# BibleWebsite
*Your ultimate Bible website for detailed commentaries, full chapters, and multiple translations to enhance your study.*

## Description
This Bible web application allows users to read and explore different translations of the Bible, view specific books and chapters, and access related commentaries. The application is built using Flask, a Python web framework, and integrates content scraped from external websites.

## Features
- **Homepage:** Displays a list of all available Bible books.
- **Bible Reader:** Allows users to read Bible chapters from different translations.
- **Commentary Section:** Provides commentary for specific Bible chapters.
- **Responsive Design:** The user interface is designed to be responsive and user-friendly.

## Screenshots

### Homepage
![home page](https://github.com/user-attachments/assets/b4f205fd-7d82-4550-a1fb-8c71a2b7ab87)

![home page displaying all books name](https://github.com/user-attachments/assets/7c94e91c-97a1-4549-9d19-5966edcab947)
*Homepage displaying available Bible books.*

### Homepage Footer
![home page footer](https://github.com/user-attachments/assets/3efd2b19-eca3-47fc-b3e5-619f7fe46d06)


### Bible Read Page
![bible read page](https://github.com/user-attachments/assets/f81165f2-e193-4dee-a4cf-c6a3d9a6c40f)


### Change Book
![change book](https://github.com/user-attachments/assets/5ea3d718-7b17-4dc2-a0c9-ea76ace811f6)


### Change Translation
![Change Translation](screenshots/change_translation.png)

### Bible Read Page Footer
![Bible Read Page Footer](screenshots/bible_read_page_footer.png)

### Read Bible Along with Commentary
![Read Bible with Commentary](screenshots/read_bible_with_commentary.png)

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
  ``` bash
  git clone https://github.com/your-username/BibleWebsite.git
  cd BibleWebsite
  ```
  
  2. **Create a virtual environment:** This step is optional but recommended to manage dependencies seperately from other projects.
  ``` bash
  python3 -m venv venv
  source venv/bin/activate   # On Windows, use 'venv\Scripts\activate'
  ```
  
  3. **Install dependencies:** Install all the neccessary python using the ```requirements.txt``` file.              
  ```bash
  pip install -r requirements.txt
  ```
  
  4. **Run the Flask app:** Start the flask developement server to run the applicaion
  ```bash
  flask run
  ```

  6. **Navigate to the app:** Open your web browser and visit http://127.0.0.1:5000 to view the application.


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

