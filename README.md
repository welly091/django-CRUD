# Lab: 29 - Django with Style

## Feature Tasks and Requirements
- Building upon previous lab, add some styles using the framework [TailwindCSS](https://tailwindcss.com/).

![lab29](https://i.imgur.com/WAp8vmu.jpg)

------
# Lab:28 - Django-CRUD 
### Date 8/24/2022

Once you start the App, go to http://127.0.0.1:8000/ to see the snacks list.
![Demo image](https://i.imgur.com/d1aXCKz.jpg)
- **Snacks List** is the main page. You can access to the link at the left-top corner.
- **Create a new snack** can create a new snack item into the list.
- Click each snack element to **update** or to **delete** the selected snack element.

## Feature Tasks and Requirements
- Create snacks_crud_project Django project
- Create snacks app
- Create Snack model
- Create SnackListView that extends appropriate generic view
  - associated url path is an empty string
- Create SnackDetailView that extends appropriate generic view
  - associated url path is <int:pk>/
- Create SnackCreateView that extends appropriate generic view
  - associated url path is create/
- Create SnackUpdateView that extends appropriate generic view
  - associated url path is <int:pk>/update/
- Create SnackDeleteView that extends appropriate generic view
  - associated url path is <int:pk>/delete/
- Add urls to support all views, with appropriate names
- Add templates to support all views
- Add navigation links in appropriate locations to access all pages
  
## Stretch Goals
- [ ] add multiple models
- [x] use an alternate test runner
- [x] add more advanced fields to models, e.g. created time stamp
- [x] add styling

