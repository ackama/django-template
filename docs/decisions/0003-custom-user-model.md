# 0003 Use Custom User Model

- Date: 2024-04-10
- Author(s): [Chen Zhang][chen]
- Status: `Active`

## Decision

Instead of using Django built-in User model, We will use a custom User model which
is based on the Django built-in AbstractUser model and provides all the same features
by default.

## Context

Django comes with a built-in User model which provides basic authentication and 
authorisation features. This model includes fields like username, email, password,
and essential methods for user management. However, there're some limitations of
the default User model.

The built-in User model is designed so users can login via username and password,
and won’t be able to login with email and password. Also, we're unable to add new
fields to the default user model.

[The official Django documentation][document] highly recommends using a custom user
model when start a Django project, because it’s hard to switch a user model out for
another once the project is deployed and being used by real users.

## Implications

This custom User model might not be perfect for all use cases,  but by making a custom
user model part of the template project we can insure it is as easy as possible to
change and evolve that model later one. Something that is a lot more difficult should
we stick with the built in one.

In some cases, users might lost access to their email address before they update their
email address on the website or APP, and if the project uses email as primary user identifier
it will be difficult for them to get their accounts back.

<!-- Links -->
[chen]: mailto:chen.zhang@ackama.com
[document]: https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
