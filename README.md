# Manager App

### Overview

This web app is to help improve the communication between managers and employees for a better work flow and
performance in retail stores. The app has 3 main navigation tabs. One for Notification,
second one for scheduling and third one for grill timer. The notification will have 4 sub tabs. The
first one is for
Urgent messages, second one for General messages, third one for completed Tasks/messages, fourth one
for Daily Tasks.
In the app a user/employee will be able to signup and login to leave a note or post a message. Check
his/her schedule. And use a mobile device (tablet) to control the time food stays on a grill. Also managers can
notify a person in charge about anything new even though they are away from work place (post a note or message from
their mobile device).

### Features

- User login : User must be logged in to post a note, edit or delete a note
- Create a note: Any user logged in must be able to create a note
- Badges: To notify if there is a new note or message
- Edit and delete: A user can edit or delete his/her note but not able to modify others
- Mark completed: A logged in user can mark a note as completed
- Schedule: A user can access the schedule of the given week, but admins only can create or modify
  schedule tables
- Email a schedule: Admins can email schedules to other users
- Grill controller: A user can start a timer for a new food displayed on the Grill

### Technologies

- Python
- Flask
- MySQL
- SQLAlchemy
- Jinja2 templates
- Javascript

### Running the application

docker build . -t manapp

docker run --rm --publish 5000:5000 manapp

### Snapshots

#### Login Page

![alt text](https://raw.githubusercontent.com/adonayab/python_proj1_manager_app/master/project_snapshots/1_login.png)

#### Register Page

![alt text](https://raw.githubusercontent.com/adonayab/python_proj1_manager_app/master/project_snapshots/2_register.png)

#### Admin Home

![alt text](https://raw.githubusercontent.com/adonayab/python_proj1_manager_app/master/project_snapshots/2_admin.png)

#### Deleting a User

![alt text](https://raw.githubusercontent.com/adonayab/python_proj1_manager_app/master/project_snapshots/2_deleteComfirm.png)

#### The Messages Home Page

![alt text](https://raw.githubusercontent.com/adonayab/python_proj1_manager_app/master/project_snapshots/3_msgHome.png)

#### Creating a New Note

![alt text](https://raw.githubusercontent.com/adonayab/python_proj1_manager_app/master/project_snapshots/4_newNote.png)

#### Editing an existing Note

![alt text](https://raw.githubusercontent.com/adonayab/python_proj1_manager_app/master/project_snapshots/4_editNote.png)

#### Options for a single Note (Edit or Delete the Note)

![alt text](https://raw.githubusercontent.com/adonayab/python_proj1_manager_app/master/project_snapshots/4_noteOptions.png)

#### Filtering Completed Notes

![alt text](https://raw.githubusercontent.com/adonayab/python_proj1_manager_app/master/project_snapshots/5_completed.png)

#### Daily Tasks

![alt text](https://raw.githubusercontent.com/adonayab/python_proj1_manager_app/master/project_snapshots/6_dailyTask.png)

#### Adding a Task

![alt text](https://raw.githubusercontent.com/adonayab/python_proj1_manager_app/master/project_snapshots/7_addTask.png)

#### Searching for Notes Feature

![alt text](https://raw.githubusercontent.com/adonayab/python_proj1_manager_app/master/project_snapshots/8_search.png)

#### Scheduling Home Page

![alt text](https://raw.githubusercontent.com/adonayab/python_proj1_manager_app/master/project_snapshots/9_scheduleHome.png)

#### Viewing a Schedule

![alt text](https://raw.githubusercontent.com/adonayab/python_proj1_manager_app/master/project_snapshots/10_viewSchedule.png)

#### Creating a Schedule

![alt text](https://raw.githubusercontent.com/adonayab/python_proj1_manager_app/master/project_snapshots/11_createSchedule.png)

#### Adding users to the Schedule

![alt text](https://raw.githubusercontent.com/adonayab/python_proj1_manager_app/master/project_snapshots/12_addSchedule.png)

#### Editing a User Schedule

![alt text](https://raw.githubusercontent.com/adonayab/python_proj1_manager_app/master/project_snapshots/13_editSchedule.png)

#### The Grill Home Page

![alt text](https://raw.githubusercontent.com/adonayab/python_proj1_manager_app/master/project_snapshots/14_grillHome.png)

#### Timers for different types of food items

![alt text](https://raw.githubusercontent.com/adonayab/python_proj1_manager_app/master/project_snapshots/15_grillCountDown.png)
