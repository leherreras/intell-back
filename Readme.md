If you want run the project you need have installed Docker and docker-compose

For run the project with docker-compose please run the next commands
`docker-compose -f docker/docker-compose.yml up -d`

You initial data to test the service is
`"username": "intell",
"password": "12345",
"first_name": "Intell",
"last_name": "Next"`

Get all users
`curl -XGET http://127.0.0.1:5000/user/`

Create one user
`curl -XPOST -d username=luis -d password=12345 -d first_name=luis -d last_name=herrera http://127.0.0.1:5000/user/`

GET specific user
`curl -XGET http://127.0.0.1:5000/user/luis`

Login user
`curl -XPOST -d username=luis -d password=12345 http://127.0.0.1:5000/login/`

Get Books
`curl -XGET http://127.0.0.1:5000/book/`

Create Book
`curl -XPOST -d title=title1 -d publication_date="1899-01-01T00:00:00" http://127.0.0.1:5000/book/`

Get Book
`curl -XGET http://127.0.0.1:5000/book/title1`

Get Comments
`curl -XGET http://127.0.0.1:5000/book/comment/`

Create Comment
`curl -XPOST -d text=test_test -d id_book=1 -d id_user=1 http://127.0.0.1:5000/book/comment/`
