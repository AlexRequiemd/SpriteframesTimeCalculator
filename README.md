# Sprite Frames Time Calculator
Este mini software eu desenvolvi para ajudar na forma que faço animações na Godot Engine com AnimatedSprite2d juntamente com o AnimationPlayer.
Basicamente quando meu AnimatedSprite2d iniciava uma animação eu executava uma animação no AnimationPlayer no exato mesmo momento para demais propósitos, seja instanciar algo, mudar um hitbox, aplicar um sahder ou mudá-lo e etc.

E para que a animação do AnimationPlayer ocorresse no exato frame que eu desejasse, eu precisava adaptar os valores com base na quantidade de frames e de FPS que a animação do AnimatedSprite2d pssuía, e é basicamente isso que esse software faz. 

Você adiciona os valores da sua animação 2d e ele converte os valores para segundos, ou seja, Tempo Total da Animação e Duração de Cada Frame em segundos para você adicionar na animação no Animation Player para ela ser sincronizada perfeitamente com o AnimatedSprite2D.
