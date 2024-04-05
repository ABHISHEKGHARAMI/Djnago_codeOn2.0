# Djnago_codeOn2.0
This is the Django learning repo with rapid development .


Here goes the content for the site .

1. first we create the model using the oops class and __str__ , meta() class
2. We register the model to the admin file
3. We add the app to the settings of the projects.
4. Adding the datefield to the model
5. Migration of the database to the the db.squlite
6. Adding the choice fill for status for the charfield.
7. then migration database.
8. Superuser creation
9. Using the object relation mapper (ORM) creating the queryset .
10. Using the Query set in view we declare the function for the url.
11. Adding get_object_or_404 from django.http 
12. create a custom urls.py in django to create the route.
13. Adding the blog app to the mysite project url.
14. Accessing the Django.admin and create a post 
15. using a decorater custom admin added which is going to be helpfull for the post when added or updated.
16. Using the Django.auth.models from there User added for the many to one relation author foreign key object.
17. Finally a post is created.
18. Creating the templates for the site to show
   the structure is-
       templates
         ---->blog
               ---->base.html
                 this will be the main rendering part and have a sidebar to  it.
                 which will inherit the list and detail
               ----> post
                    ----> list.html
                    ----> detail.html
19. Successfully added the published .
Going to the 2nd chapter.

20. Adding the cannonical route for the url
  ---> it workslike we import the reverse method from the django.urls then make function for the 
       get_absoluet_url()  in the models
      then it added in the list.html
21. Adding the seo friendly route for the site.
     ways to do it is 
        1. Added the slug field unique by adding the unique='publish' no slug can be added to the database as a same slug name on the same data
        2. changing the url for that like -
          <int:year>/<int:month>/<int:day><post:slug>
        3. Now we change the post_detail
        4. in models.py have to change the get_absolute_url() have to add year,month,day,slug as parameter.

22. Adding the Paginator for the site.
    Have to add django.core.paginator import Paginator then according to that have to add page number
    and then add a paginator html file with checking the if else based upon the posts.