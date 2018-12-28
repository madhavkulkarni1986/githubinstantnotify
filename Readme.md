Readme.md
---------

Author: Madhava Kulkarni
Email : madhav.kulkarni1986@gmail.com

Purpose or Idea of this script:
   In a large project with many developers using Github to collaborate, code is always written parallely by each other. This is realized only during the process of Push to Github. If you have delayed a push for 1-2 days, then you are way behind in the commit. You realise if you knew about others commit-push as soon as it was done, you could have pulled the changes and be up to date with the changes. 
   With this in mind, and not worrying about the solutions that exists, I started creating the script. It is small and simple.

Script:
   gitinstanotify.py - Github instant notification. A single Python script.

Modules:
   flask
   json
   sys
   request
   ntfy

Description:
   Since this is a flask application, you can deploy it into Cloud and get the URL to add it into Github webhook. Github sends the message to this webhook when there is an event, which you have subscribed to
   (Currently, this script works for only "push" events, as this was my intention).

Script tested with:
   - Python 3
   - ngrok - for creating webhook
   - Windows 10 host

Configuration:
   [ I have used ngrok to create a webhook and hence you will see the "port" variable. You can change this as per your cloud provider's configuration]

   -  If you have deployed the script in cloud, copy the URL and configure it in Github.
      Goto https://github.com/<your account>/<repository>/settings/hooks/ --> Add webhook --> Paste the URL in the text box under "Payload URL", set "Content type" to "application/json" from the dropdown. Select "Just the push event" radio button. Check "Active" and click on "Add webhook"
   -  On your windows machine enable Notifications and Action center to see the messages.

 Change log:
 - v1.0 --> First verison