import sys

def clean_url(url):
    """
    Description: Cleans URL by removing suffix
    """
    if "?" in url:
        return url[:url.index("?")]
    else:
        return url
    
def main():
    raw_url = sys.argv[1]
    url = clean_url(raw_url)
    print(url)

if __name__ == '__main__':
    main()