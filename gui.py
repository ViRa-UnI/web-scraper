# gui.py

```python
import tkinter as tk

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Website Source Code Scraper")
        self.window.geometry("800x600")

        self.label = tk.Label(self.window, text="Enter the URL of the website:")
        self.label.pack()

        self.entry = tk.Entry(self.window)
        self.entry.pack()

        self.button = tk.Button(self.window, text="Scrape", command=self.scrape_website)
        self.button.pack()

        self.window.mainloop()

    def scrape_website(self):
        url = self.entry.get()
        # Add your code here to scrape the website source code

if __name__ == "__main__":
    gui = GUI()
```

This code generates a basic GUI using the `tkinter` library. It creates a window with a label, an entry field for the user to enter the URL of the website, and a button to initiate the scraping process. The `scrape_website` method is called when the button is clicked, and it retrieves the URL entered by the user. You can add your own code inside the `scrape_website` method to implement the website source code scraping functionality.