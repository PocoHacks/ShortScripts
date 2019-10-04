if __name__ == '__main__':
    import urllib.request
    import re

    URL = "https://httpbin.org/ip" # Constant that contains the URL

    with urllib.request.urlopen(URL) as webRequest:
        result = webRequest.read().decode("utf-8") # Get the result to the request and decode it
        ipRegex = "\d\d?\d?\.\d\d?\d?\.\d\d?\d?\.\d\d?\d?" # Regex that matches any IP
        print("Your IP address is:", re.findall(ipRegex, result)[0])