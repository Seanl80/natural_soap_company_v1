# Natural Soap Company

[Link to Natural Soap Co. live site](https://natural-soap-company-v1-33f8559d9f2f.herokuapp.com/)

This is my Milestone 4 project based around a fictional company.
The Natural Soap Company is a newly formed company with the aim of selling soaps free from harmful chemicals to customers of all ages who think like us on how soap should be made. It's website has been created using a postgreSQL database. It's made using lanuages like JavaScript and Python. Bootstrap has been used for a structured layout and Stripe used for payments.

## Developer goals

As a Developer, I would like:
- to build a website which is easy to navigate through and use.
- to make the user able to have their own profile for when they use the website.
- to allow users the ability to create, display, edit and delete reviews.
- develop a database structure which will allow for previous orders, wishlists, delivery info to be stored securely.
- for superusers to be able to create, display, edit and delete products to sell.

## User stories

As a user of this website, I want:
- to browse products easily without the need to sign in.
- to add items to my cart to see how much everything I wanted would cost.
- to be able to read reviews on the products before I buy them.
- to feel that your website is secure.
- the sign up process to be easy to understand.
- acknowledgement that I have made an account with you.
- the buying process to be quick and straight forward.
- acknowledgement that I have made a purchase from you.
- to be able to view my past orders.
- to be able to ammend my details if needed.
- to be able to make a list of items I would like to buy in the future.


---

## Design choices

- The basic colour range for this website are with the following colours :-
- ![#ffffff](https://placehold.co/15x15/ffffff/ffffff.png) `#ffffff`
- ![#000000](https://placehold.co/15x15/000000/000000.png) `#000000`
- ![#6c757d](https://placehold.co/15x15/6c757d/6c757d.png) `#6c757d`
- ![#ff007b](https://placehold.co/15x15/ff007b/ff007b.png) `#ff007b`
- ![#01013e](https://placehold.co/15x15/01013e/01013e.png) `#01013e`



I felt these were a vibrant contrast to my beige background picture.
Originally I had my home page background picture displayed throughout the website but, especially with the pages that had images, I felt this clashed with my content so decided to go for a dark plain colour so I could let my content stand out more cleanly. 
I felt the rounded edges of the buttons and lowercase within the buttons felt more relaxed like the products.


---

## Wireframes

[Wireframes](https://github.com/Seanl80/natural_soap_company_v1/blob/main/docs/wireframes/All-wireframes.pdf)

Here are the original wireframes:
I have made the nine main pages of the site.
- Home page consists of an explanation of the site with navigation and shop now button. There will be icons in the navbar to login/register and a basket total.
- The Products page will consist of rectangler cards showing the different products with their images and prices.
- The Product details page will show a larger image and a more in depth description with a review section below.
- The Wishlist page will show rectangular cards again with image and price with buttons to remove from wishlist or go to product details page.
- The Basket page will contain a large image, product info and clear pricing and a total. There is buttons to make a choice whether to buy and go to checkout or to continue shopping.
- The Checkout page will be a similar layout to the basket page but will ask for customer details and a permission check to store this info.
- The Checkout success page will consist of an order confirmation the order was successful stating what was bought.
- The Register page will be the base for all form pages with content being centered with white input boxes clearly labelled.
- The Sign in page will be the base for my sign out page to keep things consistent again with clearly labelled white input boxes.


---

## Technologies used

- For this website I have chosen to use HTML, CSS and JavaScript.
- I have also used Python and Postgresql.
- I have also included Bootstrap, Font Awesome and Stripe.
- Gitpod was used as my IDE.
- GitHub was used to store my code.
- Heroku was used to deploy the website.

---


## Testing Developer Goals

As a Developer, I would like:
- to build a website which is easy to navigate through and use.
- to make the user able to have their own profile for when they use the website.
- to allow users the ability to create, display, edit and delete reviews.
- develop a database structure which will allow for previous orders, wishlists, delivery info to be stored securely.
- for superusers to be able to create, display, edit and delete products to sell.

## Testing User Stories

As a user of this website, I want:
- to browse products easily without the need to sign in.
- to add items to my cart to see how much everything I wanted would cost.
- to be able to read reviews on the products before I buy them.
- to feel that your website is secure.
- the sign up process to be easy to understand.
- acknowledgement that I have made an account with you.
- the buying process to be quick and straight forward.
- acknowledgement that I have made a purchase from you.
- to be able to view my past orders.
- to be able to ammend my details if needed.
- to be able to make a list of items I would like to buy in the future.

---

## Testing

I have used these validators to check the validity of my code.

- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/)

- [W3C Markup Validation](https://validator.w3.org/)

- [JShint JavaScript Validation](https://jshint.com/)  
    

- [CI Python Linter Validation](https://pep8ci.herokuapp.com/)  
    

These are the lighthouse performance results.  



---

## Bugs



## Deployment

This project was developed using the [Gitpod IDE](https://https://gitpod.io/). Then developments and changes were commited and pushed to GitHub.


To clone this project into Gitpod you will need:

1. A GitHub account. [Create a GitHub account here](https://www.github.com).
2. Use the Chrome browser.

Then follow these steps:

1. Install the Gitpod Browser Extensons for Chrome.
2. After installation restart the browser.
3. Log into Gitpod with your Gitpod account.
4. Navigate to the Project GitHub repository.
5. Click the green "Gitpod" button in the top right of the repository.
6. This will trigger a new gitpod workspace to be created from the code in github where you can work locally.

To deploy this page from Heroku, the following steps were taken:

1. Create a Heroku Account and log in. Click 'New' -> 'Create new app'.
2. Enter a name for your project and select your region.
3. Click 'Create app'.
4. Navigate to PostgreSQL from Code Institute and enter your email.
5. Update your project with the URL sent to your email.
6. Make sure to have dj_database_url and psycopg2 installed.
7. Login to the Heroku CLI - heroku login -i
8. Run migrations on Heroku Postgres - python3 manage.py migrate
9. Create a superuser - python3 manage.py createsuperuser
10. Install gunicorn - pip3 install gunicorn
11. Create a requirements.txt file - pip3 freeze > requirements.txt
12. Create a Procfile.
13. Disable Heroku from collecting static files
14. Add the hostname to project settings.py file
14. Commit and push the changes to GitHub.
15. Go to 'Heroku Settings', click 'Reveal Config Vars'.
16. The following variables were added:
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- DATABASE_URL
- EMAIL_HOST_PASS
- EMAIL_HOST_USER
- SECRET_KEY
- STRIPE_PUBLIC_KEY
- STRIPE_SECRET_KEY
- STRIPE_WH_SECRET
- USE_AWS
17. Click on the 'Deploy' tab.
18. Click 'Connect to GitHub'.
19. Find your repo and click 'Connect'
20. Click 'Enable Automatic Deploys'
21. Up to date version of App is now deployed by pushing to GitHub
22. Click 'Open App'. 

---

## Credits

### Code

The Code Institiue student template was used to create this project.

This project has used code from the Boutique Ado walkthrough as the basic structure then embellished.


### Media

- For my images I used [Pixabay](https://www.pixabay.com/).
- For my favicon image I used [Icon Archive](https://www.iconarchive.com/).
- To show my website on different screens I used [Am I responsive](https://ui.dev/amiresponsive/) to create them.
- For my wireframes I used [Balsamiq](https://balsamiq.com/).