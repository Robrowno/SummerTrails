<h1 align="center"><strong>🌞🚵 SummerTrails 🏄🏖️</strong>
</h1>

<h4 align="center">A Summer-Traveller's App!</h2>

<p align="center">
<img height="300px" width="300px" src="./static/assets/images/globe.png">
</p>
<p align="center">"Snap your world, pin your path, share your journey - we're redefining exploring!"</p>

## Deployment

The project is deployed and can be accessed by [clicking here!](https://summertrails-heroku-dd7388a15196.herokuapp.com/).

If you'd like to see the original repository, that can be found by following [this link](https://github.com/Robrowno/SummerTrails)

&nbsp;

## Criteria
In this section, we will briefly discuss how our team addressed the applicable criteria:

- ✨ Project is 100% Mobile First
- ✨ Project uses browser location or device camera
- ✨ Project aligns well to the Hackathon Theme
- ✨ Clear use of Github Projects or other agile tool
- ✨ Presentation Quality - Present as if you are pitching it to client


&nbsp;

## Intro

SummerTrails is a location-service app for users to share photos and pin them to their geo-location on a mapbox map for other users to see in real time.

Users can share where they have been over the summer and the many sights they have seen with other like-minded users.



&nbsp;

## Goal

The goal of this project is to connect people around the world during the summer where people are statistically most likely to travel and take holiday.

A [2014 census](https://aytm.com/post/vacations-survey) by Ask Your Target Market found that 59% of respondants said that they book their holidays in the Summer and 46% said they aim for the month of July.

We want to see users sharing cool views from different places on their travels, whether it be from a road trip to the countryside or a flight to a new destination.

Users will be able to see what others are up to and sharing and can also see recommended travel destinations around the world.

## UX Design Choices

- *Secure Login Page*: Users will be greeted with a login page to ensure that every person accessing the site must be logged in to post. This design choice helps regulate the content by ensuring that only registered users can create posts in the app. By requiring login credentials, we can maintain a safer and more controlled environment for posting.
- *Accessible Post Button*: To adhere to established mental maps and provide a user-friendly experience, we will make the post functionality easily accessible. A single red button will be placed at the bottom of the index page, ensuring that users can quickly locate and access the option to create a post. This design choice promotes ease of use and enhances app accessibility by offering clearly identifiable options.
- *Simple Post Form*: Upon clicking the post button, users will be presented with a straightforward form. This form will allow them to add a title, description, and picture to their current location on the globe. By keeping the form simple and focused, we can streamline the posting process and make it more intuitive for users to share their content.

- *Modal for Image Display*: The images added by the user will be displayed using a modal. By clicking on the marker created on the map, users can access the modal, which will showcase a list of the images associated with the post (up to a maximum of 3 images). Additionally, the modal will include the post's title and description. This design choice allows users to view the images and associated information in a focused and immersive manner.
- *Clear Close Button and Like Button*: Below each displayed image in the modal, a clear close button will be provided for users to easily close the modal and return to the map view. Additionally, a heart icon will serve as a like button. When clicked, the heart button will change color to red, indicating a successful like action. This visual feedback provides users with a clear indication of their interaction with the image.
- *Extra Menu for Reporting*: On the top left corner of the image display within the modal, an additional menu will be represented by three white dots. Clicking on these dots will open a menu with various options, including the ability to report an image in case of inappropriate content. This design choice ensures that users have a clear and accessible way to report any content that violates community guidelines or standards.

## Wireframes, ideas and planning

**Day 1:** We spent a lot of time on the first day discussing ideas based on the criteria set out by C.I.
Some great ideas off the bat included adding weather forecasts bases on your location, creating events for other users in your vicinity and search/fitering events/activities based on interests that authenticated users could save to a user profile.

The project was mapped out and followed on Github Projects.
A link to the project board can be found here: https://github.com/users/Robrowno/projects/6

We immediately knew we wanted to use the Mapbox API, and A first wireframe draft saw us modelling an app that was not too disimilar to the ROADS app by Porsche. An app where users can use their location to find interested local destinations, road trip ideas and meet up with other users who can share their own custom road trip routes.

![First draft wireframe](./static/assets/readme-images/initial-wireframe.png)

**Day 2:** On day two, we refined our scope and realised we needed to streamline our focus on getting the frontend right before looking to different features. We went back to the drawing board and came up with an idea of having the map take up the entire screen space - globe front and centre! 

Wireframes were redrafted as a result and so we developed a new plan that looked something like this:

![New Wireframe](./static/assets/readme-images/updated-wireframe.png)

With some hard-coded data we even mapped out how pinned users would appear on the map when they upload an image from their lcoation:

![Mobile Render (Day 2)](./static/assets/readme-images/day2-progress-mobile.png)

![Laptop Render (Day 2)](./static/assets/readme-images/day2-progress-laptop.png)



**Day 3:** 

Converted project to Django 4.2.2

We experienced some teething issues when installing Django, where we were using the incorrect file structure for using Django 4.2 - once that was resolved we could run the `python3 manage.py runserver` and `python3 manage.py migrate` commands.

We also changed the html template structure to suit Django, and began setting up a Django REST API. Some functionality we needed was started/completed - namely most of the authentication.

We also successully made our first migrations and started work on other pages that would be required for the application. We paired the application up with an ElephantSQL PostgreSQL RBDMS and successfully made our first deployment to Heroku.



**Day 4**

Big progress - we made big strides on the backend thanks to Niclas's great work in this area, and we also succesfully implemented login/signup/logout functionality as well as the creation and editing of a User Profile section. 

We spent a lot of time then implementing cloudinary and fixing other small bugs which would allow us to work towards polishing the work we'd put into this so far and make another final push for the 5th and final day.



**Day 5**

Some great strides again - We fixed some more bugs, implemented more styling updates/changes and bug fixes and began the final touches required for the hackathon project submission.

A geolocation API was being explored as well as what we had implemented so far.

The README.md had to finished, all project details added to the C.I Hackathon app and a 3-minute-max video for presentation in the afternoon.


Nearing the end of the submission deadline, we had a project that now looked like this:
![Project Screenshot](./static/assets/readme-images/current-look.png)

---

&nbsp;

## Tech

The following technology has been used for this application:

- Markup Languages: **HTML5**, **CSS3**
- Styling frameworks: **Bootstrap v5.2**
- Programming Languages: **Javascript**, **Python v3.9.6**
- Frameworks: **Django v4.2.2**, **Django REST Framework**
- Agile/Project-mapping: **Github Projects**, **Github Issues**
- Cloud Delivery Networks: **Cloudinary**
- RDBMS: **PostgreSQL**
- Database Hosting Service: **ElephantSQL**
- Wireframes: **Balsamiq**
- IDE: **VS Code**, **CodeAnywhere**
- Version Control: **Git**


### Testing 

- The project has been tested in Google Chrome on the following systems:

    - MacOS/Unix
    - Windows
    - iOS

- It has been tested on the following mobile screens:
    - iPhone X
    - iPhone 12 Pro
    - Samsung Galaxy S8+
    - Pixel 5
    

&nbsp;

## Future Implementations/Ideas

- **Travel Diary:** Implement some sort of chronological tracker for users to map out their travels .
- **Comment & Like:** User ability to comment and like on other's uploads and view comments and likes on their own posts.
- **Social Media integration:** Upload to other socials or share their other social accounts on their profile.
- **Advanced Search Filters:** Search based on profile interests, location and more!
- **Location-based Recommendations from the app:** Recommendations based on your active location.
- **Weather forecast based on location:** A weather forecast page which can use another API to retrieve current and forecasted weather predictions.
- **Achievement Badges:** (Post 100 photos, 200 photos, 500 photos, 1000 photos), (Visit 2 new countries, 5 new countries, 10 new countries), (Interact with: 2 posts, 5 posts, 10 posts, 20 posts, 50 posts) - collect badges for all of these!
- **Photo Album creation:** Compile your images and sort them in to albums to reminice about your travels over time.
- **Auto-deleting of pins after 'x' hours:** We will need to implement a means of clearing pins on the map that have been there longer than a specified period of time. This will ensure content is new and put less strain on the DB - **Perhaps 24 or 48hrs.**


&nbsp;

## Bugs/Issues

- We tried to set up a temporary fix for not pushing up our mapbox API early on, however, we had no success with this. We tried to `npm install dotenv` and set up a config.js file for storing out API key but we were not able to successfully import it into the index.js file.

- We had an canvas overflow issue from the nav bar which we solved by inspecting in the console and adding a z-index of 1 to one of the classes properties.

- We had some issues in installing requirements on different machines locally, especially between those of use using VS Code and CodeAnywhere. It seemed the solution a lot of the time was to start a new virtual environment and delete and re-install the packages using `pip3 install -r requirements.txt` and then `pip3 freeze > requirements.txt`

- We struggled to implement cloudinary to begin with and once we had done so, we noticed that uploaded photos were not converted to the cloudinary urls in the database.
Niclas found the solution for this, which was to set use_url=True in this segment of the serializers.py PhotoImageSerializer class: `image = serializers.ImageField(use_url=True)`

- We found you'd get a 404 error when logged out and clicked on the photo upload icon in the mobile nav - this has now been rectified to redirect to the sign up form as you need to be logged in to make posts.


**!NOTE:** If you spot any bugs on the site that we might not be aware of, please get in touch with one of us on Linkedin to inform us and we'll address it as soon as we can!



-----

&nbsp;

## Meet the Team

| Callum Dennis | Jhoan Trujillo | Christian Brown | Niclas Tanskanen | Chinonso Olejeme |
| :---: | :---: | :---: | :---: | :---: |
| ![Callum Dennis](https://ca.slack-edge.com/T0L30B202-U03SRDH32SF-af021d3d5f5a-512) | ![Jhoan Trujillo](https://ca.slack-edge.com/T0L30B202-U058Y63AY9F-a234b1fddb8d-512) | ![Christian Brown](https://ca.slack-edge.com/T0L30B202-U030WF45NKV-1720b6f59b47-512) | ![Niclas Tanskanen](https://ca.slack-edge.com/T0L30B202-U03M22KFF46-11a1d1b943cd-512) | ![Chinonso Olejeme](https://ca.slack-edge.com/T0L30B202-U01S0DB71H8-6119c0e594c3-512) |
| Full-Stack | Front-End | SCRUM Master | Back-End | Front-End |
| [Callum Dennis's LinkedIn](https://www.linkedin.com/in/callum-dennis-ireland/) | [Jhoan Trujillo's LinkedIn](https://www.linkedin.com/in/jhoan-trujillo-92b03517b/) | [ Christian Brown's LinkedIn](https://www.linkedin.com/in/christian-brown-ba7741171/) | [Niclas Tanskanen's LinkedIn](https://www.linkedin.com/in/niclastanskanen/) | [Chinonso Olejeme's LinkedIn](https://www.linkedin.com/in/olejeme/) |


-----

&nbsp;

## Credits
We would like to give credit to the following individuals, organizations, and resources that have contributed to the project or provided inspiration:

- Colour palettes were taken from the trending section on the [Coolers](https://coolors.co/palette/000000-14213d-fca311-e5e5e5-ffffff) site

- The Map was able to be generated using the Mapbox API: [Mapbox API](https://docs.mapbox.com/mapbox-gl-js/example/custom-marker-icons/)

- The user interface was pre-designed and sketched using [Balsamiq](https://balsamiq.com) wireframing tool




-----

![Summer of Code Banner](https://res.cloudinary.com/djdefbnij/image/upload/v1688114955/Summer_2_owummy.png)

-----