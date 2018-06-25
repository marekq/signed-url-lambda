signed-url-lambda
=================
Generate signed URL's for all objects stored in an S3 bucket. The results are sent using SES to an email address you can define which makes it easy to share the URL's securely over email.

Installation
------------
Ensure you have validated the from e-mail address through the SES console. Copy the Lambda code to a Python 3.6 function or use the attached SAM template and enter the validated e-mail address in the "fromemail" field.

Contact
-------
In case of questions or bugs, please raise an issue or reach out to @marekq!
