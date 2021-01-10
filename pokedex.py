import tkinter as tk
import requests

def get_pokemon_type(pokemon):
    type=[]
    response=requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
    types=response.json()['types']
    for i in types:
        j=i['type']
        type.append(j['name'])
    return type


def get_pokemon_damage(pokemon):
    response=requests.get("https://pokeapi.co/api/v2/pokemon/jigglypuff")
    types=response.json()['types']
    types_caused_damage=[]
    for i in types:
        j=i['type']
        url=j['url'] #Getting url
        damage_relations=requests.get(url).json()['damage_relations']   #requesting the data
        double_damage_from=damage_relations['double_damage_from']

        half_damage_from=damage_relations['half_damage_from']
        for l in double_damage_from:
            types_caused_damage.append(l['name'])#For nxtstep
        for m in half_damage_from:
            types_caused_damage.append(m['name'])
    return types_caused_damage


def get_pokemon_doubledamageNames(pokemon):
    response=requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
    types=response.json()['types']
    poke_caused_doubledamage=[]
    for i in types:
        j=i['type']
        url=j['url'] #Getting url
        damage_relations=requests.get(url).json()['damage_relations']   #requesting the data
        double_damage_from=damage_relations['double_damage_from']
        for l in double_damage_from:
            poke_response=requests.get("https://pokeapi.co/api/v2/type/"+l['name']) 
            poke=(poke_response.json()['pokemon']) #by observing the json data.
            k=0
            for i in poke:
                if k<5:
                    j=(i['pokemon'])
                    poke_caused_doubledamage.append(j['name'])
                    k=k+1
    return poke_caused_doubledamage


def show_pokemon_data():
    pokemon_name=txt_pokemon_name.get()

    pokemon_data_type=get_pokemon_type(pokemon_name)
    lbl_type_value.config(text= pokemon_data_type)

    pokemon_data_causeddamage=get_pokemon_damage(pokemon_name)
    lbl_damage_value.config(text=pokemon_data_causeddamage)

    pokemon_data_doubledamageName=get_pokemon_doubledamageNames(pokemon_name)
    lbl_doubledamageName_value.config(text=pokemon_data_doubledamageName)


window=tk.Tk()
window.config(bg='#edafab')
window.title('PokeDex')

# From here all the labels and the values that should be given to those labels starts.

lbl_instructions = tk.Label(window, text ="Enter the name of pokemon")
lbl_instructions.pack()

txt_pokemon_name = tk.Entry(window)
txt_pokemon_name.pack()

btn_get_info = tk.Button(window,text="Get Data!",command= show_pokemon_data)
btn_get_info.pack()

lbl_type_text=tk.Label(window,text="Type",fg='#1c03fc')
lbl_type_text.pack()
lbl_type_value=tk.Label(window,text="???")
lbl_type_value.pack()

lbl_damage_text=tk.Label(window,text="Damage caused by",fg='#1c03fc')
lbl_damage_text.pack()
lbl_damage_value=tk.Label(window,text="???")
lbl_damage_value.pack()

lbl_doubledamageName_text=tk.Label(window,text="Pokemons from each type caused double damage",fg='#1c03fc')
lbl_doubledamageName_text.pack()
lbl_doubledamageName_value=tk.Label(window,text="???")
lbl_doubledamageName_value.pack()

window.mainloop()



