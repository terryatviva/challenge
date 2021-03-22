
++++++++++++++++++++++++++++++++++++++ SERVER ++++++++++++++++++++++++++++++++++++++++++++
=> befre proceeding you should have python installed in your system and virtual environment
=> In this simple application, I recommend using virtual environment to avoid conflict with some installed app in your system.

=> open a terminal and locate the directory of the app
=> after activating your environment

=> NOTE: be sure that you are on the "server" directory on this application directory
=> install all the backend/server dependecy of the application using the command "npm install -r requirements.txt" (without the quotes)

=> you can run the development server using the code "flask run" (without the quotes)

++++++++++++++++++++++++++++++++++++++ CLIENT ++++++++++++++++++++++++++++++++++++++++++++
=> before proceeding again you should have nodejs installed in your system
=>  open another terminal and locate again the app directory
=? NOTE : be sure that you are on the "client" directory of this application directory
=> install all the dependecies using "npm install" (without the quotes), by doing this all the packages define on package.json will be installed

=> you can now run the react application using "npm start" (without the quotes)


=> After running both flask and react, open your browser and type the url below
====> http://localhost:3000/admin/feedbacks to show the table list of the feedbacks
====> http://localhost:3000/userfeedback to show the feedback form
