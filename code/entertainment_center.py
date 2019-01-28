# -*- coding: cp1252 -*-
import fresh_tomatoes
import media


#Criando a classe Avatar
avatar = media.Movie("Avatar", 120, "Filme legal", "https://upload.wikimedia.org/wikipedia/pt/thumb/b/b0/Avatar-Teaser-Poster.jpg/250px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
               "2005")

#Criando a classe bohemian_rhapsody
bohemian_rhapsody = media.Movie("Bohemian Rhapsody", 133, "banda de rock Queen em 1970.",
                  "http://t1.gstatic.com/images?q=tbn:ANd9GcSe74BDy8hvD0ZRE4RDR0NupS1TfYNBER1Rrao3_xitpEkuEMAi", "https://www.youtube.com/watch?v=GryRsVhOvxo",
               "2018")

#Criando a classe 
Aquaman = media.Movie("Aquaman", 133, "Aquaman aprende que não pode fazer tudo sozinho quando começa uma jornada com Mera em busca de um algo muito importante para o futuro de Atlantis.",
                  "https://s2.glbimg.com/fFW0Xou8Y3-7e-Xtr1L-YyTm_FE=/e.glbimg.com/og/ed/f/original/2018/08/28/aquaman.jpeg", "https://www.youtube.com/watch?v=90bG43JcwRE",
               "2019")


#avatar.show_info()
#adicionando todos os filmes no vetor
movies = [avatar,bohemian_rhapsody,Aquaman]
#Abrindo a tela de filmes
fresh_tomatoes.open_movies_page(movies)

