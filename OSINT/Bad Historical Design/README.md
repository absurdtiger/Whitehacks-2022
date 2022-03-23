# Bad Historical Design

When we click on the link, we see an empty website with not much information. However, we can see that the link to the webpage is `lewischan0601.github.io`.

When we search for lewischan0601, we see 1 repository which contains the HTML of the webpage.

When we check the commit history of the repo, we notice a commit with the description: `Purge repo due to accidental inclusion of API key`.

This prompts us to use Wayback Machine on the website to see what it contained before the repo was purged. When we do, we see one capture of the site on 12 Jan 2022, which contains the flag.

Flag:

	WH2022{4r3_y0u_sur3_y0ur_s3cr3t_1s_s4f3_?}
