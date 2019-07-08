## QUOTES BLOG

## CREATED BY

 William Mango  07/07/19

## Description

Quotes blog is a web application where  a writer can post the quote and see the blogs.and can subscribes to get the latest updates on quotes posted by other.we have comments from readers and blog writers can determine whether to delete the comments or not. writers can also delete blog posts at their discretion.After the writer has posted a new blog post, subscribers will receive an email notification with a link to the blog post
users can also random quotes by reloading or clicking on the random button

## user stories

-   users can to view the blog posts on the site
-   users can comment on blog posts
-   users can view the most recent posts
-   users get an email alert when a new post is made by joining a subscription.
-   users can see random quotes on the site
-   a writer, I would like to sign in to the blog.
-   a writer, I would also like to create a blog from the application.
-   a writer, I would like to delete comments that I find insulting or degrading.
-   a writer, I would like to update or delete blogs I have created.

## features

-   The home page presents users with all available navigation to various routes/linked pages.
-   The system flow is simple.
    ## BDD
    | Behavior            | Input                   | Outcome                            |
    \| --------------------\|-------------------------\| -----------------------------------\|
    | display random quote| reloaad/click random    | rrandom quotes                     |
    | add  a q  quote     | fill oute the quote form| new quote posted                   |  
    | view blog           | click on heroku link    | random and recent quotes           |
    |comment on a quote   |fill out comments  form  |fill out the comment form           |
    |delete a quote&commen|click delete             |comment/quote deleted               |

## Setup/Installation Requirements

Cloning
In your terminal:

-   git clone (<https://github.com/mangowilliam/quotesblog>
-   cd quotesblog
    Creating the virtual environment

-   python3 -m pip install --user virtualenv ( on a Mac)
-   python3 -m virtualenv env
-   source env/bin/activate

    Installing Flask and other Modules

While in the virtalenvironment install all the requirements by running $ pip install -r requirements.txt
Setting up the quotes base url

To run the application, in your terminal:

  $ chmod a+x start.sh
  $ ./start.sh

## Known Bugs

No known bugs

## Technologies Used

-   Python 3.6
-   Flask Framework
-   HTML, CSS and Bootstrap
-   JavaScript
-   Git
-   SQLALCHEMY

## Support and contact details

contact williammango2015@gmail.com for any kind of support.

## Live Link

**[click here](https://github.com/mangowilliam/quotesblog)**

### License

**[MIT](https://opensource.org/licenses/MIT)**
Copyright (c) 2019 **manowilliam**
