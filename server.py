import json
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template
import lxml

with open("static/data_details.json") as data_file:
    data = json.load(data_file)
# Extracting keys from "books_details" dictionary
book_names = list(data["books_details"].keys())


app = Flask(__name__)
@app.route("/")
def get_home():
    return render_template("home.html", all_books=book_names)


@app.route("/bible/<translation>/<book_name>/<chapter_num>")
def get_bible_book(translation,  book_name, chapter_num):
    response = requests.get(f"https://www.bible.com/bible/{data["translations_codes"][translation]}"
                            f"/{data["books_details"][book_name]["code"]}.{chapter_num}")
    response.raise_for_status()  # Raise an HTTPError for bad responses
    bible_webpage = response.text
    soup = BeautifulSoup(bible_webpage, "lxml")
    bible_info = soup.find_all(name="span", class_="ChapterContent_verse__57FIw")

    return render_template("bible.html", book=book_name, chapter=chapter_num, translation=translation,
                           all_books=book_names, number_of_chapters=data["books_details"][book_name]["chapters"],
                           content=bible_info)



@app.route("/bible_commentary/<translation>/<book_name>/<chapter_num>")
def get_commentary(translation, book_name, chapter_num):
    response1 = requests.get(f"https://www.bible.com/bible/{data["translations_codes"][translation]}"
                            f"/{data["books_details"][book_name]["code"]}.{chapter_num}")
    response1.raise_for_status()  # Raise an HTTPError for bad responses
    bible_webpage = response1.text
    soup = BeautifulSoup(bible_webpage, "lxml")
    bible_info = soup.find_all(name="span", class_="ChapterContent_verse__57FIw")

    response2 = requests.get(f"https://enduringword.com/bible-commentary/{book_name.lower()}-{chapter_num}/")
    response2.raise_for_status()  # Raise an HTTPError for bad responses
    bible_webpage = response2.text
    soup = BeautifulSoup(bible_webpage, "lxml")
    commentary_info = soup.select(selector=".av_textblock_section av-b79tk-cae54786a9c77a674c5eff51df1b2afb "
                                           ".avia_textblock h3,h4,p")
    commentary = []
    for i in range(len(commentary_info) - 25):
        commentary.append(commentary_info[i])

    return render_template("commentary.html", book=book_name, chapter=chapter_num, translation=translation,
                           all_books=book_names, number_of_chapters=data["books_details"][book_name]["chapters"],
                           content=bible_info, commentary_content=commentary)



if __name__ == "__main__":
    app.run(debug=True)
