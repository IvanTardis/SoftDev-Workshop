**how-to :: bootstrap**

**Overview**

Bootstrap is a front-end framework to more easily customize and stylize your web apps. It includes prebuilt components that can be easily integrated into your application.


**Estimated Time Cost: YMMV**


**Prerequisites:**

- Have Bootstrap documentation open (https://getbootstrap.com/docs)
- Not much! Some basic html will help, but it’s not necessary


1. Create an html file (e.g. index. html)
2. Write the basic html file setup - something like this:
<!DOCTYPE html>
<!--
	heading here
-->

<html>

	<head>
    	<title> hello </title>
	</head>

	<body>
	</body>

</html>

3. Link CDN (content delivery network) for Bootstrap. You can find the link on Bootsrap’s website (https://getbootstrap.com/). Scroll down past “Install via package manager” and you’ll find “Include via CDN” with two copy-paste links. Copy the first link and paste it within the head of your html.

<!DOCTYPE html>
<html>

	<head>
    	<title> hello </title>
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
	</head>

	<body>
	</body>

</html>

4. Explore the Bootstrap website to see what features you’d like to include in your web app. Simply copy and paste the code into your html file, and adjust the content as needed.
