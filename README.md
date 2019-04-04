# SmoothieDB

SmoothieDB is a database of smoothie recipes by a lover of smoothies and for all lovers of smoothies.

A smoothie is a thick and creamy beverage made from pureed raw fruit, vegetables, and sometimes dairy products (e.g. milk, yogurt, ice-cream or cottage cheese), typically using a blender. Smoothies may be made using other ingredients, such as water, crushed ice, fruit juice, sweeteners (e.g. honey, sugar, stevia, or syrup), whey powder, plant milk, nuts, nut butter, seeds, tea, chocolate, herbal supplements, or nutritional supplements. A smoothie containing dairy products is similar to a milkshake, though the latter typically contains less fruit and often uses ice cream or frozen yogurt. 

SmoothieDB a simple beautiful App that allows users to look up recipes that include their search-term (i.e. main ingredient or taste). Users can alos upload their own favourite smoothie recipes to the database, thus growing the App and sharing their favourites with others.

<hr/>

## UX

#### User Stories
 
- I love smoothies - the taste, the health benefits and the ease that they can be whipped up in no time at all. I love trying new recipes, but sometimes they're hard to come by, and if you do find recipes online, you'e bombarded with click-bait and other distractions. I'd like a one-stop-shop for smoothie recipes.

- Anne is a primary school teacher who is trying to encourage the introduction of more fruits and vegatables to her pupils diet. She is looking for a App that is colourful, child-friendly and user-friendly for the kids to use.

- Tom works at home and eats on the go, but sometimes just opens the fridge/press and reaches for the wrong things. With an App like SmoothieDB he has healthy recipes at his fingertips and can get an quick meal in no time at all.

#### Design Considerations

The design of SmoothieDB instantly greets users with fun colour and eye catching simple icons that spell out recipe contents.

#### Responsive Design

The App is designed to work on all devices.

Proposed layout -

![Mobile Layout](/documentation/mobile-plan.png)

![Desktop Layout](documentation/desktop-plan.png)


## Features

##### Navigation
- Simple one page App. Navigation by way of HTML anchor links to various points on the page.

![Navigation](/documentation/Barrys-Strava-2018-Navigation.png)

##### Reset / Reload Page

- Bespoke button to "reloadPage" hovers and animates at top right of browser window on all devices. Animation will be enough for users to know it’s there, but not so much that it is an annoyance.

##### Crossfilter

- Crossfilter Javascript library in installed connecting and rendering data to various D3 charts.

##### Possible feature to implement

- Another feature that could be implemented is connecting HTML elements to the crossfilter functionality. It would be good if clicking images of gear/bikes would trigger the data charts to behave the same as clicking on a crossfilter elements themselves.  I did research this to no avail. I think bespoke functions could be written further along in my learning.

<hr/>

## Technologies Used

- [CSS](https://bootswatch.com/)

This App is constructed in HTML using a simple bootstrap framework boilerplate template called "United" from Bootswatch.com

Default CSS is used throughout and further styled with the file - /assets/css/style.css


- [Javascript](https://www.javascript.com/)
    - The App uses Crossfilter, D3, DC and Queue pre-installed **Javascript** libraries.
    - Bespoke functions are written in the file - /assets/js/barry.strava.js


- [JQuery](https://jquery.com)
    - The project uses **JQuery** to enable hamburger dropdown menu on smaller mobile devices.

<hr/>

## Testing

##### User Stories addressed

- The App addresses the needs/wants of submitted user stories by showing that Strava data can be easily downloaded, and displayed in a neat intuitive manner while also allowing users to feature their own bikes/gear and add their own text/photos, etc.

##### Design

- The responsiveness of the App was tested in MAC OSX Safari, Firefox and Chrome browser windows at varying sizes and displays as intended/desired.

- The responsiveness of the App was tested in iPhone6 Chrome and Safari Apps and displays as intended/desired.

- Also tested on a random selection of phones, tablets and desktop browsers using https://www.browserstack.com/
extension in Firefox.

- The D3 charts are not responsive, as expected, nor do the guidelines of the project require them to be.

##### Code

- HTML code checked with validator.W3.org returns
    - Document checking completed. No errors or warnings to show.

- CSS code checked with validator.W3.org returns one error
    - Property **r** (radius of SVG circle) doesn't exist - This is related to pin pointing one specific data point and styling with bespoke CSS. Property **r** may not exist, but it does work.

- Javascript checked through JSHint.com returns no errors

##### Bug

- A bug that encountered was with the Bootswatch template I used, where the hamburger menu button collapse feature did not work as desired. On click the menu opened, but closed straight away.

- The issue was resolved with - `.navbar-collapse.collapse.in{display: block!important;}`

- CREDIT: https://stackoverflow.com/questions/25878450/bootstrap-collapsed-navbar-buggy-open

- An anomally in data encountered was where I had done three separate activities in one day, and the average speed was grouped, thus displaying an unachievable average speed for a bicycle (c. 70kmph). Activity Lines 19 & 20 were removed to rectify.

<hr/>

## Deployment

The App is deployed to GithubPages for review

https://barra1212.github.io/college-project-dashboard-strava/

<hr/>

## Credits

#### Content
- The dataset is made from my own 2018 Strava activities an downloaded directly as CSV from my [VeloViewer](https://www.veloviewer.com/) profile.

- The CSV dataset was converted to a JSON file via [csvjson.com](https://www.csvjson.com/csv2json) but I chose to use CSV

#### Media
- The text and images content are all my own.

- The video is an MP4 review of my 2018 activities generated by [Strava](https://www.strava.com/)

#### Acknowledgements

- I received inspiration from my own Strava experiences.

- I received Javascript support from Niel @ Code Institute and highlight same specifically in barry.strava.js