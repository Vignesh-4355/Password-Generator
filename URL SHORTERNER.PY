import pyshorterner

def shorten_url(long_url):
    try:
        shortener = pyshorteners.Shortener()
        return shortener.tinyurl.short(long_url)
    except Exception as e:
        return f"Error: {e}"

def expand_url(short_url):
    try:
        shortener = pyshorteners.Shortener()
        return shortener.tinyurl.expand(short_url)
    except Exception as e:
        return f"Error: {e}"

def main():
    while True:
        print("\nURL Shortener")
        print("1. Shorten URL")
        print("2. Expand URL")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            url = input("Enter the URL to shorten: ")
            print(f"Shortened URL: {shorten_url(url)}")
        elif choice == "2":
            url = input("Enter the shortened URL to expand: ")
            print(f"Original URL: {expand_url(url)}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
