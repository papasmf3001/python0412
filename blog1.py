import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

search_keyword = "맥불어"

# Create a new Excel workbook and worksheet
workbook = Workbook()
worksheet = workbook.active

# Set the column headers for the worksheet
worksheet["A1"] = "Blog Title"
worksheet["B1"] = "Blog Address"

row_number = 2 # start from row 2 to leave the first row for headers

for page in range(1, 101):
    url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start={page * 10 - 9}"

    # Send an HTTP request to the blog URL and get the response
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the blog post title and address using the CSS selectors
    blog_links = soup.select(".sh_blog_top dt a")
    for link in blog_links:
        blog_title = link.get_text()
        blog_address = link["href"]

        # Write the results to the worksheet
        worksheet[f"A{row_number}"] = blog_title
        worksheet[f"B{row_number}"] = blog_address
        row_number += 1

# Save the workbook to a file
workbook.save(filename="c:/work/search results.xlsx")
