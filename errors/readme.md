# Error Pages

These are error pages which can be applied via your blog if you so wish.

## GitHub Pages

Using error pages with GitHub is very easy.

  1. If you're using **GitHub pages with git** then this will be done automatically and so you have nothing to worry about.
  2. If you're using **GitHub pages web only** then you should have done this during your manual setup and so you have nothing to worry about.

Unfortunately GitHub does not support any error pages other than 404 so they will have been left out.

## Website

If you're using Wren with a website (either stand-alone or alongside) then you will have to manually then In [Apache](https://en.wikipedia.org/wiki/Apache_HTTP_Server) for example this is done by enabling and using the ```.htaccess``` file, an example of which is shown below.

```
ErrorDocument 400 /errors/400.html
ErrorDocument 403 /errors/403.html
ErrorDocument 404 /errors/404.html
ErrorDocument 500 /errors/500.html
```

As of now Wren does not handle your ```.htaccess``` so you will have to do this seperately. This may change in future versions, especially if users request it.