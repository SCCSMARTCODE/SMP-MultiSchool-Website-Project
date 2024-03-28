"""
This module contains static messages for gmail notification...
"""


def message(content, name):
    if content == 'Welcome School':
        return """ <!DOCTYPE html>
            <html lang="en">
            <head>
              <meta charset="UTF-8">
              <meta name="viewport" content="width=device-width, initial-scale=1.0">
              <title>Welcome to Our School Platform</title>
              <style>
                body {
                  font-family: Arial, sans-serif;
                  margin: 0;
                  padding: 0;
                }
                .container {
                  max-width: 600px;
                  margin: 20px auto;
                  padding: 20px;
                  border-top: 5px solid #003cff;
                  /* border-radius: 2px 2px 0 0; */
                  background-color: #ffffff;
                  box-shadow: 1px 1px 2px rgba(104, 104, 204, 0.363), 0px 1px 2px rgba(104, 104, 204, 0.363);
                }
                h1 {
                  color: #003cff;
                  text-decoration: underline;
                  font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
                  text-align: center;
                }
                p {
                  /* color: #666; */
                  font-family: cursive;
                  font-weight: 700;
                  text-indent: 15px;
                }
                .message{
                  display: inline-block;
                  background-color: #007bff;
                  color: #fff;
                  padding: 10px 20px;
                  text-decoration: none;
                  border-radius: 5px;
                }
            
                .cta-btn{
                  /* display: inline-block; */
                  background-color: #ffffff;
                  color: #0004ff;
                  padding: 10px 20px;
                  text-decoration: none;
                  border-radius: 5px;
                  text-align: center;
                  margin-top: 15vh;
                }
              </style>
            </head>""" + f"""
            <body>
              <div class="container">
                <h1>Welcome to SMP MultiSchool Website!</h1>
                <div class="message">
                  <p>Thank you {name} for registering with us. Your account has been created successfully.</p>
                  <p>Please note that your account will need to be verified and activated before you can log in.</p>
                  <p>An email will be sent to you once your account has been verified and activated.</p>
                  <p>If you have any questions or need assistance, feel free to contact us.</p>
                  <p class="cta-btn">Best regards,<br>SMP Platform Team</p>
                </div>
              </div>
            </body>
            </html>

        """

    elif content == 'Welcome Student':
        return """ <!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Welcome to Our School Platform</title>
            <style>
            body {
              font-family: Arial, sans-serif;
              margin: 0;
              padding: 0;
            }
            .container {
              max-width: 600px;
              margin: 20px auto;
              padding: 20px;
              border-top: 5px solid #003cff;
              /* border-radius: 2px 2px 0 0; */
              background-color: #ffffff;
              box-shadow: 1px 1px 2px rgba(104, 104, 204, 0.363), 0px 1px 2px rgba(104, 104, 204, 0.363);
            }
            h1 {
              color: #003cff;
              text-decoration: underline;
              font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
              text-align: center;
            }
            p {
              /* color: #666; */
              font-family: cursive;
              font-weight: 700;
              text-indent: 15px;
            }
            .message{
              display: inline-block;
              background-color: #007bff;
              color: #fff;
              padding: 10px 20px;
              text-decoration: none;
              border-radius: 5px;
            }
            
            .cta-btn{
              /* display: inline-block; */
              background-color: #ffffff;
              color: #0004ff;
              padding: 10px 20px;
              text-decoration: none;
              border-radius: 5px;
              text-align: center;
              margin-top: 15vh;
            }
            </style>
            </head>""" + f"""
            <body>
            <div class="container">
            <h1>Welcome to SMP MultiSchool Website!</h1>
            <div class="message">
              <p>Thank you {name} for joining our school community. Your student account has been created successfully.</p>
              <p>Please note that your account verification and activation will be handled by the school you registered under.</p>
              <p>An email notification will be sent to you once your account has been verified and activated by your school.</p>
              <p>If you have any questions or need assistance, feel free to contact your school administration.</p>
              <p class="cta-btn">Best regards,<br>SMP Platform Team</p>
            </div>
            </div>
            </body>
            </html>

        """

    elif content == 'active student':
        return """
            <!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Welcome to Our School Platform</title>
            <style>
            body {
              font-family: Arial, sans-serif;
              margin: 0;
              padding: 0;
            }
            .container {
              max-width: 600px;
              margin: 20px auto;
              padding: 20px;
              border-top: 5px solid #003cff;
              /* border-radius: 2px 2px 0 0; */
              background-color: #ffffff;
              box-shadow: 1px 1px 2px rgba(104, 104, 204, 0.363), 0px 1px 2px rgba(104, 104, 204, 0.363);
            }
            h1 {
              color: #003cff;
              text-decoration: underline;
              font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
              text-align: center;
            }
            p {
              /* color: #666; */
              font-family: cursive;
              font-weight: 700;
              text-indent: 15px;
            }
            .message{
              display: inline-block;
              background-color: #007bff;
              color: #fff;
              padding: 10px 20px;
              text-decoration: none;
              border-radius: 5px;
            }
            
            .cta-btn{
              /* display: inline-block; */
              background-color: #ffffff;
              color: #0004ff;
              padding: 10px 20px;
              text-decoration: none;
              border-radius: 5px;
              text-align: center;
              margin-top: 15vh;
            }
            </style>
            </head>""" + f"""
            <body>
            <div class="container">
            <h1>Your Account is Now Active!</h1>
            
            <div class="message">
                    <p>{name}, Your student account has been successfully verified and activated.
                    <br><br> You can now log in to our school platform and access all features.</p>
                    <p>If you have any questions or need assistance, feel free to contact your school administration.</p>
               <p class="cta-btn">Best regards,<br>SMP Platform Team</p>
            </div>
            </div>
            </body>
            </html>

        """

    elif content == 'inactive student':
        return """<!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Welcome to Our School Platform</title>
            <style>
            body {
              font-family: Arial, sans-serif;
              margin: 0;
              padding: 0;
            }
            .container {
              max-width: 600px;
              margin: 20px auto;
              padding: 20px;
              border-top: 5px solid #003cff;
              /* border-radius: 2px 2px 0 0; */
              background-color: #ffffff;
              box-shadow: 1px 1px 2px rgba(104, 104, 204, 0.363), 0px 1px 2px rgba(104, 104, 204, 0.363);
            }
            h1 {
              color: #003cff;
              text-decoration: underline;
              font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
              text-align: center;
            }
            p {
              /* color: #666; */
              font-family: cursive;
              font-weight: 700;
              text-indent: 15px;
            }
            .message{
              display: inline-block;
              background-color: #007bff;
              color: #fff;
              padding: 10px 20px;
              text-decoration: none;
              border-radius: 5px;
            }
            
            .cta-btn{
              /* display: inline-block; */
              background-color: #ffffff;
              color: #0004ff;
              padding: 10px 20px;
              text-decoration: none;
              border-radius: 5px;
              text-align: center;
              margin-top: 15vh;
            }
            </style>
            </head>
            <body> """ + f"""
            <div class="container">
            <h1>Your Account is Currently Inactive</h1>
            
            <div class="message">
              
              <p>{name}, Your student account is currently inactive. This may be due to pending verification or activation.</p>
              <p>Please contact your school administration for further assistance to activate your account.</p>
              <p>Once your account is activated, you will receive a confirmation email.</p>
              <p class="cta-btn">Best regards,<br>SMP Platform Team</p>
            </div>
            </div>
            </body>
            </html>

    """

    elif content == 'active school':
        return """ <!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Welcome to Our School Platform</title>
            <style>
            body {
              font-family: Arial, sans-serif;
              margin: 0;
              padding: 0;
            }
            .container {
              max-width: 600px;
              margin: 20px auto;
              padding: 20px;
              border-top: 5px solid #003cff;
              /* border-radius: 2px 2px 0 0; */
              background-color: #ffffff;
              box-shadow: 1px 1px 2px rgba(104, 104, 204, 0.363), 0px 1px 2px rgba(104, 104, 204, 0.363);
            }
            h1 {
              color: #003cff;
              text-decoration: underline;
              font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
              text-align: center;
            }
            p {
              /* color: #666; */
              font-family: cursive;
              font-weight: 700;
              text-indent: 15px;
            }
            .message{
              display: inline-block;
              background-color: #007bff;
              color: #fff;
              padding: 10px 20px;
              text-decoration: none;
              border-radius: 5px;
            }
            
            .cta-btn{
              /* display: inline-block; */
              background-color: #ffffff;
              color: #0004ff;
              padding: 10px 20px;
              text-decoration: none;
              border-radius: 5px;
              text-align: center;
              margin-top: 15vh;
            }
            </style>
            </head>
            <body>""" + f"""
            <div class="container">
            <h1>Your School Account is Now Active!</h1>
            
            <div class="message">
              
              <p>{name}, Your school account has been successfully verified and activated.</p>
              <p>You can now log in to our platform and manage your school profile, classes, and students.</p>
              <p>If you have any questions or need assistance, feel free to contact our support team.</p>
             
              <p class="cta-btn">Best regards,<br>SMP Platform Team</p>
            </div>
            </div>
            </body>
            </html>

        """

    elif content == 'inactive school':
        return """ 
            <!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Welcome to Our School Platform</title>
            <style>
            body {
              font-family: Arial, sans-serif;
              margin: 0;
              padding: 0;
            }
            .container {
              max-width: 600px;
              margin: 20px auto;
              padding: 20px;
              border-top: 5px solid #003cff;
              background-color: #ffffff;
              box-shadow: 1px 1px 2px rgba(104, 104, 204, 0.363), 0px 1px 2px rgba(104, 104, 204, 0.363);
            }
            h1 {
              color: #003cff;
              text-decoration: underline;
              font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
              text-align: center;
            }
            p {
              font-family: cursive;
              font-weight: 700;
              text-indent: 15px;
            }
            .message{
              display: inline-block;
              background-color: #007bff;
              color: #fff;
              padding: 10px 20px;
              text-decoration: none;
              border-radius: 5px;
            }
            
            .cta-btn{
              background-color: #ffffff;
              color: #0004ff;
              padding: 10px 20px;
              text-decoration: none;
              border-radius: 5px;
              text-align: center;
              margin-top: 15vh;
            }
            </style>
            </head>""" + f"""
            <body>
            <div class="container">
            <h1>Your School Account is Currently Inactive</h1>
            
            <div class="message">
              <p>{name}, Your school account is currently inactive. This may be due to pending verification or activation.</p>
              <p>Please contact our support team for further assistance to activate your account.</p>
              <p>Once your account is activated, you will receive a confirmation email.</p>
                        
              <p class="cta-btn">Best regards,<br>SMP Platform Team</p>
            </div>
            </div>
            </body>
            </html>
        """
    else:
        return None
