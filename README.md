# PostsComments-DjangoRest

API provides list of news with functionality to upvote and comment on them. Similar platform to [HackerNews](https://news.ycombinator.com/).

## Functionality

- Containes CRUD API to manage news posts. The post has the next fields: title, link, creation date, amount of upvotes, author-name
- Posts has CRUD API to manage comments on them. The comment has the next fields: author-name, content, creation date
- There is an endpoint to upvote the post
- Recurring job running once a day to reset post upvotes count

## Intstoctuns to get started
- Clone the repo
- Go to the folder posts_cmnts (cd posts_cmnts)
- Start the docker containers by "(sudo) docker-compose up"

## Postmant collection
https://www.getpostman.com/collections/66e807bca44dad4de72f
