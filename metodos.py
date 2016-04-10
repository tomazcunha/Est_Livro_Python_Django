# -*- coding: utf-8 -*-

# http://br.lipsum.com/feed/html
lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed urna ligula, suscipit vel mauris ut, euismod pharetra eros. Nunc eu scelerisque elit. Donec eget commodo leo. Integer posuere egestas tristique."

lorem_full = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed urna ligula, suscipit vel mauris ut, euismod pharetra eros. Nunc eu scelerisque elit. Donec eget commodo leo. Integer posuere egestas tristique. Praesent tincidunt pellentesque nibh, vitae maximus sem sagittis nec. Cras tincidunt nibh gravida quam posuere, bibendum ornare nunc venenatis. Proin tincidunt velit mollis mi convallis consectetur. Aliquam euismod turpis ut tortor pulvinar feugiat. Etiam elit odio, hendrerit eu leo ac, varius maximus justo. Morbi sit amet sem orci. Fusce at mollis nunc. Duis semper vestibulum elementum. Sed quis hendrerit purus. Donec tristique dui vel molestie vulputate. Mauris vulputate metus eros, a sollicitudin erat tempor et.

Vivamus quis efficitur mauris, id tincidunt turpis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras ac odio sed orci iaculis imperdiet. In quis ipsum consectetur, suscipit orci quis, sagittis libero. Nullam laoreet diam a risus dictum, vel convallis ligula sollicitudin. Cras auctor suscipit nunc, eu euismod augue fringilla nec. Aliquam ut porta lacus, aliquam posuere ligula. Nullam ultrices nunc a sapien porta, nec posuere lorem commodo. Vivamus nec tellus mi. Duis gravida lacus magna, vel eleifend est porttitor eget.

Pellentesque condimentum augue quis sapien gravida tempus. Mauris commodo molestie neque ut gravida. In id imperdiet tortor. Morbi eget tortor leo. Pellentesque tincidunt est lorem, ut tempor mauris tempor nec. Vivamus a nulla ut nisi cursus dapibus. Praesent vitae lacinia purus, eu lobortis turpis. Sed elementum erat eget sagittis imperdiet. Pellentesque non pulvinar erat. Nunc euismod dui at erat accumsan tempor. Nam a nunc pharetra, congue odio pharetra, laoreet turpis. In pharetra, libero a lobortis consectetur, enim felis eleifend velit, quis gravida sapien turpis sit amet sapien. Sed ac arcu euismod, posuere velit vel, laoreet odio. Etiam vitae feugiat elit. Cras non leo ut dui vulputate dapibus nec eget massa.

Ut aliquam est sit amet lorem tristique vulputate at sed metus. Praesent bibendum magna faucibus ullamcorper iaculis. Ut vel ipsum non elit consequat vehicula. Vestibulum at nunc lectus. Fusce egestas, urna eget commodo eleifend, magna tortor tempus tellus, eget volutpat nulla turpis quis urna. Aliquam erat volutpat. Phasellus facilisis metus felis, sed tincidunt ipsum dignissim id. Sed pretium diam sapien, id facilisis turpis finibus sed.

Aenean pellentesque ligula lacus, at viverra lectus sodales at. Sed nisi nisi, facilisis eget sagittis in, porta sed mi. Ut quis fringilla mauris. Nunc ac turpis in sem eleifend laoreet. Praesent vestibulum pellentesque arcu, vel elementum velit imperdiet sit amet. Donec mauris justo, porta at lorem quis, volutpat tempus turpis. Fusce non ipsum quis nunc convallis efficitur a quis enim. Sed sed eros leo. Suspendisse volutpat bibendum diam. In tristique orci sit amet dignissim volutpat. Integer at fermentum felis. In convallis nec neque a fringilla. Maecenas ut elementum metus. Vestibulum varius nunc cursus leo posuere, vel vestibulum eros finibus.
"""

lor = "Lorem ipsum dolor sit amet"

# capitalize() = primeiro caractere em maiúsculo.
# "exemplo".capitalize()
print "exemplo".capitalize()
print lorem.capitalize()

# center(largura) = centraliza usando espaços em branco nos lados
print lor.center(100) # largura de 100 caracteres

# count() = conta substrings
letras =("a","b","c","d","e","f","g","h","i","j","l","m","n","o","p","q","r","s","t","u","v","x","z","w","y","k")
letras_valor ={}

for letra in letras:
    letras_valor[letra] = lorem_full.count(letra)
    # print letra , lorem_full.count(letra)

print sorted(letras_valor.values())


# http://defpython.blogspot.com.br/2007/01/conhecendo-os-dicionrios.html
# >>> items = [('nome','igor'), ('idade', 18), ('curso','python')]
# >>> d = dict(items)
# >>> d
# {'idade': 18, 'curso': 'python', 'nome': 'igor'}
