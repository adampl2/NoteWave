# NoteWave - Testing

![multi screen img]()

[View deployed site here]()

- - -

## CONTENTS

* [`Automated Testing`](#automated-testing)
  * [`W3C Validator`](#w3c-validator)
  * [`JavaScript Validator`](#javascript-validator)
  * [`Lighthouse`](#lighthouse)
* [`Manual Testing`](#manual-testing)
  * [`User Stories`](#user-stories)
  * [`Full Testing`](#full-testing)

Testing progressed at every stage of this project. This ensured that most issues were fixed before the website was finished. Chrome DevTools were utilised when building the website to help with troubleshooting as the website transformed.

## Automated Testing

Since this is a Flask application, there are errors, however, they are only referring to syntax that is used within the Flask application and therefore, are not relevant.

### W3C Validator

The [W3C validator](https://validator.w3.org/) was used to validate the HTML and CSS pages.

* HTML Validation

* base.html
  * ![base.html](docs/testing-base.jpg)

* edit_note.html
  * ![edit_note.html](docs/testing-edit.jpg)

* home.html
  * ![home.html](docs/testing-home.jpg)

* login.html
  * ![login.html](docs/testing-login.jpg)

* sign_up.html
  * ![sign_up.html](docs/testing-signup.jpg)

* 404.html
  * ![404.html](docs/testing-404.jpg)

* CSS Validation
  * ![CSS](docs/testing-css.jpg)

- - -

### JavaScript Validator

[jshint](https://jshint.com/) was used to validate all JavaScript code on this page.

* script.js Validation

  * [`script.js`](docs/testing-js.jpg) - The JSHint comments are inaccurate as they are reporting an undefined variable as a jQuery function and an unused variable as being used. Therefore, the comments should be reviewed and revised to provide more accurate information.

- - -

### Python Testing

[]

- - -

### Lighthouse

### Desktop

![Desktop](docs/lighthouse-desktop.jpg)

### Mobile

![Mobile](docs/lighthouse-mobile.jpg)

- - -

## Manual Testing

### User Stories

`Client Goals`

| Goals | How are they achieved? |
| :--- | :--- |
| First-time user: As a first time user, I want to easily create a new account on the note app, so I can start creating, viewing, editing, and deleting notes. I also want to be able to quickly and intuitively navigate through the note app, so I can easily find the features I need to use and efficiently manage my notes. | I have created prominent "Sign Up" button and a simple sign-up form. The app's clean and organized interface, with a clear menu and search function, made it easy to navigate. The app was made responsive through optimized design techniques for different devices. |
| I want the site to be responsive to my device. | I have developed the site with responsiveness in mind. |
| Frequent user: As a frequent user, I want to be able to easily access my notes from my previous sessions so that I can quickly pick up where I left off and continue my work. I also want to be able to edit, delete, and create new notes when I wish to do so. | I have created clear buttons for editing, deleting, and creating new notes. |

- - -

### Full Testing

I have fully tested the website using Google Chrome and Mozilla Firefox on desktop (HP Pavilion Convertible 14 inch) and mobile (Samsung Note9).

It was ensured that through the testing process content was responsive using the Google Developer Tools.

Further testing was performed by friends & family. No issues reported.

`Home Page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Home button | Should refresh the page | Button clicked | Home page reloads | Pass |
| Logout button | User logged out | Clicked on button | User is redirected to login | Pass |
| Title input | Should allow the user to enter title | Wrote title | Title written | Pass |
| Note textarea | Should allow the user to enter note contents | Wrote contents | Note written | Pass |
| Add Note button | Should create note and display it above | Clicked on button | Note added accordingly | Pass |
| Edit button | Should redirect the user to the edit page  | Clicked on button | User redirected to the edit page | Pass |
| Delete button | Should show modal  | Clicked on button | Modal appeared | Pass |
| Facebook link | Should redirect to facebook.com  | Clicked on link | User redirected | Pass |
| Twitter link | Should redirect to twitter.com  | Clicked on link | User redirected | Pass |
| GitHub link | Should redirect to github.com  | Clicked on link | User redirected | Pass |
| LinkedIn link | Should redirect to linkedin.com  | Clicked on link | User redirected | Pass |
| copyright link | Should redirect to github.com  | Clicked on link | User redirected | Pass |
| alert `x` button | Should close alert message  | Clicked on button | Alert closed | Pass |

`Home page - Modal`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| `x` button | Should hide the modal  | Clicked on button | Modal hidden | Pass |
| Cancel button | Should hide the modal  | Clicked on button | Modal hidden | Pass |
| Delete button | Should delete the note  | Clicked on button | Note deleted | Pass |

`Edit note page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Title input | User should be able to enter title | Title entered | Title input filled | Pass |
| Note body | User should be able to enter note field | Note body typed | Note body is filled | Pass |
| Save Changes button | Should save the note with changes made by user | Button clicked | Note updated | Pass |

`Login page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Login button | Should refresh page | Button clicked | Page reloads | Pass |
| Sign Up button | User redirected to Sign up page | Button clicked | User redirected | Pass |
| Email/password fields | Should let user enter email/password | Input entered | Fields are filled with text/*s | Pass |
| Login button | Should login the user | Button clicked | User logged in | Pass |

`Sign Up page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Login button | Should redirect user to login page | Button clicked | User redirected | Pass |
| Sign Up button | Should reload page | Button clicked | Page reloads | Pass |
| Email/username/password fields | Should let user enter email/username/password | Input entered | Fields are filled with text/*s | Pass |
| Register button | User redirected to their home page | Button clicked | User account created | Pass
