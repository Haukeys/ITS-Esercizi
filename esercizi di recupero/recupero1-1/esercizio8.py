#Progettare un sistema di videonoleggio


class Movie:

    def __init__(self,movie_id:str, title:str, director:str,is_rented:bool=False)->None: #valeur par deflaut false car il n est pas alouer de base
        self.movie_id=movie_id
        self.title=title
        self.director=director
        self.is_rented=is_rented



    def rent(self)->None:

        if not self.is_rented:
            self.is_rented=True
        
        else:
            print(f"Il film '{self.title}' è già noleggiato.")



    def return_movie(self)->None:

        if self.is_rented:
            self.is_rented=False
        
        else:
            print(f"Il film '{self.title}' non è stato noleggiato da questo cliente.")

class Custumer:
    
    def __init__(self, custumer_id:str, name:str, rented_movies:list[Movie] =[])->None: #valeur par defaut de la liste inizialiser car de base elle est techniquement vide

        self.custumer_id =custumer_id
        self.name = name
        self.rented_movies = rented_movies



    def rent_movie(self, movie:Movie)->None:

        if not movie.is_rented:

            movie.rent()

            self.rented_movies.append(movie)

        else:
            print(f"il film è stato affittato")



    def return_movie(self, movie:Movie)->None:

        if movie in self.rented_movies:

            movie.return_movie()

            self.rented_movies.remove(movie)

        else:
            print(f"il film è stato affittato")  


class VideoRentalStore:

    def __init__(self, movies:dict[str, Movie]={}, custumers: dict[str, Custumer] = {})->None:

        self.movies = movies
        self.custumers = custumers



    def add_movie(self, movie_id: str, title: str, director: str)->None:

        if movie_id in self.movies:

            print(f"Il film con id {movie_id} è gia presente ne catalogo")

        else:

            movie : Movie = Movie(movie_id=movie_id, title=title , director=director)

            self.movies[movie_id] = movie 



    def register_customer(self, customer_id: str, name: str) -> None:

        if customer_id in self.custumers:

            print(f"Il cliente è gia registrato!")

        else:

            customer: Custumer = Custumer (custumer_id=customer_id, name=name)

            self.custumers[customer_id] = customer


    
    def rent_movie(self, customer_id:str, movie_id:str) -> None:
        
        if customer_id in self.custumers and movie_id in self.movies:

            self.custumers[customer_id].rent_movie(self.movies[movie_id])
        
        else:
            
            print(f"Il film non trovato oppure cliente non trovato")



    def return_movie(self, customer_id:str, movie_id:str) -> None:
            
            if customer_id in self.custumers and movie_id in self.movies:

                self.custumers[customer_id].return_movie(self.movies[movie_id])
            
            else:
                
                print(f"Il film non trovato oppure cliente non trovato")


    
    def get_rented_movies(self, customer_id:str) -> list[Movie]:

        if customer_id in self.custumers:

            return self.custumers[customer_id].rented_movies
        
        else:

            print(f"Il cliente non è presente!")
            return []
        

#tutti i film nolegiati
    def get_rented_list(self) -> list[Movie]:

        lista_movies: list[Movie] = []

        for id, cliente in self.custumers.items():

            lista_movies += cliente.rented_movies

        return lista_movies