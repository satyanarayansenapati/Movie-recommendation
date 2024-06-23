# Movie recommendation system

Data : The data that needs to be uploaded should have following format :

`
movie title :{x['movie_title']}\nmovie info :{x['movie_info']}\ngenres :{x['genres']}\ndirectors :{x['directors']}\nactors :{x['actors']}\nrelease date :{x['original_release_date']}\nrating :{x['audience_rating']}
`

 It is recommended to keep the number of actors to less than or equal to 5.


 The project uses Vector Database.

 ## USE :

 __input__ : _a movie name_

 __output__ : _3 movies (that exists in the database) that are similar to the provided movie name_