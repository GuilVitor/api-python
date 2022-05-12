from cProfile import run
from distutils.log import debug
from hashlib import new
from urllib import request, response
from flask import Flask, request

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

users_data ={
    1:{
        "id": 1,
        "name":"thor",
        "logo": "https://static1.purebreak.com.br/articles/6/42/37/6/@/197155-thor-chris-hemsworth-conta-porque-nao-diapo-3.jpg",
        "capa" : "https://img.r7.com/images/2013/05/07/16_40_14_201_file?dimensions=643x600 ",
        "Descricao" : " Thor era uma divindade da mitologia nórdica e reconhecido como o deus do trovão, das tempestades e da agricultura. Originário da cultura germânica, é reconhecido pelos historiadores como o deus mais popular entre os nórdicos da Era Viking. Filho de Odin, era tido como o mais poderoso do panteão nórdico. "

    },
    2:{
        "id": 2,
        "name" : "Capitao-America",
        "logo" : "https://observatoriodocinema.uol.com.br/wp-content/uploads/2020/06/Captain-America.jpg",
        "capa" : "https://cdn.falauniversidades.com.br/wp-content/uploads/2019/02/capitao-america-heroi-avengers-vingadores-ultimato.jpg ",
        "Descricao" : " O Capitão América é a identidade heroica de Steve Rogers. Além disso, é considerado como o primeiro Vingador. Em suma, o personagem nasceu em 1941, na revista Captain America Comics #1. Ademais, o super herói foi criado por Joe Simon e Jack Kirby, dos estúdios da Marvel Comics.  "
    },
    3:{
        "id": 3,
        "name" : "Hulk",
        "logo" : "https://noticiasetecnologia.com/wp-content/uploads/2021/01/The-Incredible-Hulk.jpg",
        "capa" : "https://kanto.legiaodosherois.com.br/w760-h398-gnw-cfill-q95/wp-content/uploads/2022/01/legiao_hAeZHQJt594f.jpg.jpeg ",
        "Descricao" : " o Hulk é um selvagem e poderoso alter ego do Dr. Robert Bruce Banner, um cientista que foi atingido por raios gama enquanto salvava um adolescente durante o teste militar de uma bomba por ele desenvolvida. "
    },
    4:{
        "id": 4,
        "name" : "Homem de Ferro",
        "logo" : "https://observatoriodocinema.uol.com.br/wp-content/uploads/2021/02/homem-de-ferro-tony-divulgacao.jpg",
        "capa" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgP6VPZuBqcewExTvmShSKr1bMJxEBzWhW2AVJk6m4UexOHTZ8JEuiDFcAJJqj0JmUOFo&usqp=CAU ",
        "Descricao" : " O Homem de Ferro (Iron Man) é um personagem dos quadrinhos publicados pela Marvel Comics. Sua verdadeira identidade é o empresário e bilionário Tony Stark, que usa armaduras de alta tecnologia no combate ao crime. "
    },
    5:{ 
        "id": 5,
        "name" : "Thanos",
        "logo" : "https://turnmundonerd.com.br/wp-content/uploads/2021/11/poltrona-google-let-users-play-with-thanos-destructive-power.jpg",
        "capa" : "https://i.pinimg.com/474x/17/75/ab/1775ab5040cb1d51fd2e81546889ff16.jpg ",
        "Descricao" : " Thanos é um personagem fictício, um supervilão das histórias em quadrinhos publicadas pela Marvel Comics, inspirado em Thanatos. "
    },
    6:{
        "id": 6,
        "name" : "Batman",
        "logo" : "https://wallpapers.com/images/high/the-batman-2022-red-light-yklg9yvfwbwuwybs.jpg",
        "capa" : "https://i.pinimg.com/736x/41/1c/78/411c78af8811e5683aea642de790ef2c.jpg ",
        "Descricao" : "O Batman (inicialmente chamado o Bat-Man) também conhecido pelas alcunhas Homem-Morcego, Cavaleiro das Trevas, Cruzado Encapuzado, Maior Detetive do Mundo, é um personagem fictício e super-herói encapuçado da editora norte-americana DC Comics, criado pelo desenhista Bob Kane e pelo escritor Bill Finger. "

    },
    7:{
      "id": 7,
        "name" : "Superman",
        "logo" : "https://pipocamoderna.com.br/wp-content/uploads/2016/08/superman__henry_cavill__batman_v_superman.jpg",
        "capa" : "https://observatoriodocinema.uol.com.br/wp-content/uploads/2019/11/superman-henry-cavill.jpg ",
        "Descricao" : " Superman ou Super-Homem é um super-herói de histórias em quadrinhos publicadas pela DC Comics. O personagem, entretanto, desde os anos 1930, já foi adaptado para diversos outros meios, como cinema, rádio, televisão, literatura e video game. "
    },
    8:{
       "id": 8,
        "name" : "Mulher-maravilha",
        "logo" : "https://img.elo7.com.br/product/zoom/2163028/poster-do-filme-mulher-maravilha-50cm-x-70cm-poster.jpg",
        "capa" : "https://res.cloudinary.com/social-comics/image/authenticated/s--f3DYbZQJ--/v1634775911/blog/20170412_gal_gadot_mulher_maravilha_wonder_woman_28990a442a.jpg ",
        "Descricao" : " O verdadeiro nome da Mulher-Maravilha é Diana Prince, uma amazona filha da rainha Hipólita e de Zeus, um conhecido deus da mitologia grega. A heroína vive com outras guerreiras em uma ilha mítica chamada Temiscira. "
    },
    9:{
       "id": 9,
        "name" : "Flash",
        "logo" : "https://pipocamoderna.com.br/wp-content/uploads/2017/10/Justiceleague-FLASH-628.jpg",
        "capa" : "https://br.web.img3.acsta.net/newsv7/19/03/18/15/34/5022183.jpg ",
        "Descricao" : " Era de Prata dos Quadrinhos, Este novo Flash era Barry Allen, um funcionário da polícia científica que ganhou seus poderes após ser banhado por produtos químicos quando seu laboratório foi atingido por um raio. Ele adotou o nome de Flash, depois de ler uma história em quadrinhos sobre o Flash original. "
    },
    10:{
         "id": 10,
        "name" : "Darksaid",
        "logo" : "https://cdna.artstation.com/p/assets/images/images/035/890/286/large/sean-gorman-darkstation.jpg?1616166117",
        "capa" : "https://i.pinimg.com/280x280_RS/47/2d/8a/472d8aadf35079871c192e68504a62f4.jpg ",
        "Descricao" : "Darkseid é um personagem fictício e um supervilão poderoso que aparece nas histórias em quadrinhos publicadas pela editora americana DC Comics, geralmente descrito como uma das maiores ameaças do Universo DC. "
    },
   

}
def response_users():
   return{"users": list(users_data.values())}

@app.route("/")
def root():
    return "<h1>Api com flask</h1>"



@app.route("/users")
def list_users():
    return response_users()    

@app.route("/users", methods=["POST"])
def create_user():
    body = request.json

    addId = list(users_data.keys())

    if addId:
    
    
     new_id = addId[-1] +1

    else : 
    
      new_id = 1

    users_data[new_id] ={

             "id": new_id,
             "name" : body["name"]

         }

    return response_users()

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete(user_id: int):
    user = users_data.get(user_id)
    
    if user:
     
     del users_data[user_id]

    return response_users()

@app.route("/users/<int:user_id>", methods=["PUT"])
def update(user_id: int):
    body = request.json
    name = body.get("name")

    if user_id in users_data:
        users_data[user_id]["name"] = name
      
    return response_users()


app.run(debug=True)