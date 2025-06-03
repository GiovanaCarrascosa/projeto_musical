-- Criar o banco de dados
CREATE DATABASE IF NOT EXISTS db_musicalizando;
USE db_musicalizando;

-- Tabela de categorias
CREATE TABLE tb_categorias (    
    cod_categoria INT AUTO_INCREMENT PRIMARY KEY,       
    nome VARCHAR(80) NOT NULL
);

-- Tabela de produtos
CREATE TABLE tb_produtos (    
    cod_produto INT AUTO_INCREMENT PRIMARY KEY,       
    titulo VARCHAR(80) NOT NULL,   
    descricao TEXT NOT NULL,    
    preco DECIMAL(10,2) NOT NULL,    
    cod_categoria INT NOT NULL,
    FOREIGN KEY (cod_categoria) REFERENCES tb_categorias(cod_categoria)
);

-- Tabela de fotos
CREATE TABLE tb_fotos_produto (
    cod_foto INT AUTO_INCREMENT PRIMARY KEY,
    url_foto VARCHAR(255) NOT NULL,
    cod_produto INT NOT NULL,  
    FOREIGN KEY (cod_produto) REFERENCES tb_produtos(cod_produto)
);

-- Tabela de usuários
CREATE TABLE tb_usuarios (    
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,    
    usuario VARCHAR(40) NOT NULL UNIQUE, 
    email VARCHAR(80) NOT NULL UNIQUE,     
    nome_pessoa VARCHAR(80) NOT NULL,   
    endereco VARCHAR(80) NOT NULL,
    telefone VARCHAR(20) NOT NULL,  
    senha VARCHAR(255) NOT NULL
);

-- Tabela do carrinho
CREATE TABLE tb_carrinho (    
    id_carrinho INT AUTO_INCREMENT PRIMARY KEY,    
    id_usuario INT NOT NULL,    
    cod_produto INT NOT NULL,     
    FOREIGN KEY (id_usuario) REFERENCES tb_usuarios(id_usuario),   
    FOREIGN KEY (cod_produto) REFERENCES tb_produtos(cod_produto)
);

-- Tabela de comentários
CREATE TABLE tb_comentario (    
    id_comentario INT AUTO_INCREMENT PRIMARY KEY,    
    id_usuario INT NOT NULL,    
    cod_produto INT NOT NULL,    
    comentario TEXT NOT NULL,    
    data_comentario DATETIME NOT NULL,    
    FOREIGN KEY (id_usuario) REFERENCES tb_usuarios(id_usuario),    
    FOREIGN KEY (cod_produto) REFERENCES tb_produtos(cod_produto)
);

-- Inserindo as categorias na tb_categorias
INSERT INTO tb_categorias (nome) VALUES
('Cd e Vinil'),
('Camisetas'),
('Acessorios');

-- Inserindo os produtos na tb_produtos

INSERT INTO tb_produtos (titulo, descricao, preco, cod_categoria) VALUES
('Vinil Taylor Swift 1989 (Taylors Version)', ' 22 Músicas  Incluindo 5 músicas inéditas do The Vault & 1 Bônus Track', 539.90, 1),
('CD Chappell Roan - The Rise and Fall of a Midwest Princess', 'Primeiro álbum da cantora e compositora pop norte-americana Chappell Roan.', 129.90, 1),
('Vinil Rita Lee - Rita Lee 3001', '3001 disco máquina do tempo de Rita Lee, é lançado pela primeira vez em vinil', 349.90, 1),
('Vinil Rihanna - Talk That Talk (LP)', 'Talk That Talk é o sexto álbum de estúdio de Rihanna, lançado em 18 de novembro de 2011.', 298.90, 1),
('Vinil The Weeknd - HURRY UP TOMORROW', '22 faixas em 2 discos Vinil preto', 329.90, 1),
('CD Sabrina Carpenter - Short n Sweet (Deluxe)', 'Short n Sweet mostra o espírito cintilante de Sabrina Carpenter, a pocket-sized popstar com uma presença artística grandiosa.', 89.90, 1),
('Vinil Ariana Grande - eternal sunshine deluxe: brighter days ahead', 'eternal sunshine deluxe: brighter days ahead - com nove faixas bônus, incluindo 6 novas músicas.', 699.90, 1),
('Vinil Jão - Pirata', 'Considerado um dos nomes mais importantes da nova cena pop brasileira, Jão lançou, o álbum PIRATA, o terceiro de estúdio da sua discografia.', 199.90, 1),
('Vinil Billie Eilish - HIT ME HARD AND SOFT ', 'Seu trabalho mais ousado até hoje, uma coleção diversificada, porém coesa, de músicas - idealmente ouvidas na íntegra, do começo ao fim', 399.90, 1),
('Vinil Zeca Pagodinho - 40 Anos', 'O registro do show Zeca Pagodinho – 40 anos gravado em audiovisual, no Engenhão, em 4 de fevereiro de 2024, ganhou uma versão em vinil', 349.90, 1),

('Camiseta Lady Gaga - MAYHEM Cover', 'A Camiseta MAYHEM com arte da capa do álbum na frente é um produto exclusivo e oficial Musicalizando.', 149.90, 2),
('Camiseta Ariana Grande - ETERNAL SUNSHINE TRACKLIST', 'A Camiseta ETERNAL SUNSHINE TRACKLIST é um produto exclusivo e oficial Musicalizando.', 89.00, 2),
('Camiseta Sabrina Carpenter - Espresso Photo Tee Off-White', 'A Camiseta Espresso Photo Tee é um produto exclusivo e oficial Musicalizando.', 164.90, 2),
('Camiseta Billie Eilish - Billie Star (Oversized)', 'A Camiseta Billie Star é um produto exclusivo e oficial Universal Music.', 129.90, 2),
('TAYLOR SWIFT - THE ERAS TOUR COLLECTION', 'A camiseta the eras tour collection faz parte da grande turnê da cantora Taylor Swift', 129.00, 2),
('Camiseta Rita Lee - Bruxa', 'A Camiseta Bruxa é um produto exclusivo e oficial Universal Music.', 99.90, 2),
('Camiseta Red Moon In Venus Halftone Butterfly.', 'A camiseta Red Moon In Venus Halftone Butterfly Photo Tracklist é um produto exclusivo e oficial Musicalizando.', 109.90, 2),
('Camiseta Conan Gray - Superache Tee', 'A Camiseta Superache Tee é um produto exclusivo e oficial Musicalizando. ', 99.90, 2),
('Camiseta Demi Lovato - Heart Attack Anniversary', 'A Camiseta DL Heart Attack Band Tee é um produto exclusivo e oficial Musicalizando.', 99.90, 2),
('Camiseta 60 PLASTERED TONGUE', 'A Camiseta 60 PLASTERED TONGUE é um produto exclusivo e oficial Musicalizando.', 79.90, 2),

('Totebag Lady Gaga - Rio Silhueta', 'Totebag Lady Gaga – Rio Silhueta (White) com gráficos impressos frente e verso.', 119.90, 3),
('Pin Renato Russo - Temos Nosso Próprio Tempo', 'O Pin Temos Nosso Próprio Tempo é um produto exclusivo e oficial Musicalizando.', 68.99, 3),
('Caneca ANAVITÓRIA - Trevo', 'Sua vida útil pode ser prolongada ainda mais, se for utilizado utensílios de plástico, madeira ou silicone.', 69.90, 3),
('Copo Térmico Anitta - Larissa', 'Copo térmico "Larissa: O outro lado de Anitta', 69.50, 3),
('Quadro Florence + the Machine', 'Moldura em madeira e espessura da moldura 1,5cm e acetato acrílico.', 110.20, 3),
('Capa de Almofada Cazuza - Exagerado', ' A Capa de Almofada Exagerado é um produto exclusivo e oficial Musicalizando.', 46.34, 3),
('Caderneta capa dura Rita Lee - A Rainha', 'O Moleskine A Rainha é um produto exclusivo e oficial Musicalizando.', 100.00, 3),
('Kit Pin Jão - Caixa 4 PINs', 'Os Pins Jão são produtos exclusivos e oficiais Musicalizando.', 99.90, 3),
('Toalha Queen - Dont Stop Me Now', 'A Toalha Dont Stop Me Now é um produto exclusivo e oficial Musicalizando.', 44.60, 3),
('Capa de almofada Vários Artistas', 'A capa de Almofada Music Is Universal Cartoon é um produto exclusivo e oficial Musicalizando.', 35.90, 3);


-- Inserindo as fotos na tb_fotos_produto

INSERT INTO tb_fotos_produto (url_foto, cod_produto) VALUES
('/projeto_musical/static/img/cd-img/cd-1989-taylorswift.png', 1),
('vinil-chanpelroan.png', 2),
('vinil-ritalee.png', 3),
('vinil-talk-rihanna.png', 4),
('vinil-hurryup-theweeknd.png', 5),
('cd-shortandsweet-sabrina.png', 6),
('vinil-eternalsunshine-ariana.png', 7),
('vinil-pirata-jao.png.png', 8),
('vinil-hithard-billie.png', 9),
('vinil-zecapagodinho.png', 10),
('camiseta_ladygaga.png.png', 11),
('camiseta_arianagrande.png', 12),
('camiseta_sabrinacarpenter.png', 13),
('camiseta_billieeilish.png', 14),
('camiseta_taylorswift.png', 15),
('camiseta_ritalee.png', 16),
('camiseta_kaliuchis.png', 17),
('camiseta_conangray.png', 18),
('camiseta_demilovato.png', 19),
('camiseta_therollingstones.png', 20),
('acessorio-ecobag-ladygaga.png', 21),
('acessorio-pin-renato.png', 22),
('acessorio-caneca-anavitoria.png', 23),
('acessorio-copo-anitta.png', 24),
('acessorio-quadro-florence.png', 25),
('acessorio-almofada-cazuza.png', 26),
('acessorio-caderno-ritalee.png', 27),
('acessorios-pin-jao.png', 28),
('acessorio-toalha-queen.png', 29),
('acessorio-almofada-artistas.png', 30);

-- Inserindo as fotos com o caminho das pastas

INSERT INTO tb_fotos_produto (url_foto, cod_produto) VALUES
('/projeto_musical/static/img/cd-img/cd-1989-taylorswift.png', 1),
('/projeto_musical/static/img/cd-img/vinil-chanpelroan.png', 2),
('/projeto_musical/static/img/cd-img/vinil-ritalee.png', 3),
('/projeto_musical/static/img/cd-img/vinil-talk-rihanna.png', 4),
('/projeto_musical/static/img/cd-img/vinil-hurryup-theweeknd.png', 5),
('/projeto_musical/static/img/cd-img/cd-shortandsweet-sabrina.png', 6),
('/projeto_musical/static/img/cd-img/vinil-eternalsunshine-ariana.png', 7),
('/projeto_musical/static/img/cd-img/vinil-pirata-jao.png.png', 8),
('/projeto_musical/static/img/cd-img/vinil-hithard-billie.png', 9),
('/projeto_musical/static/img/cd-img/vinil-zecapagodinho.png', 10),
('/projeto_musical/static/img/camisetas-img/camiseta_ladygaga.png.png', 11),
('/projeto_musical/static/img/camisetas-img/camiseta_arianagrande.png', 12),
('/projeto_musical/static/img/camisetas-img/camiseta_sabrinacarpenter.png', 13),
('/projeto_musical/static/img/camisetas-img/camiseta_billieeilish.png', 14),
('/projeto_musical/static/img/camisetas-img/camiseta_taylorswift.png', 15),
('/projeto_musical/static/img/camisetas-img/camiseta_ritalee.png', 16),
('/projeto_musical/static/img/camisetas-img/camiseta_kaliuchis.png', 17),
('/projeto_musical/static/img/camisetas-img/camiseta_conangray.png', 18),
('/projeto_musical/static/img/camisetas-img/camiseta_demilovato.png', 19),
('/projeto_musical/static/img/camisetas-img/camiseta_therollingstones.png', 20),
('/projeto_musical/static/img/acessorios/acessorio-ecobag-ladygaga.png', 21),
('/projeto_musical/static/img/acessorios/acessorio-pin-renato.png', 22),
('/projeto_musical/static/img/acessorios/acessorio-caneca-anavitoria.png', 23),
('/projeto_musical/static/img/acessorios/acessorio-copo-anitta.png', 24),
('/projeto_musical/static/img/acessorios/acessorio-quadro-florence.png', 25),
('/projeto_musical/static/img/acessorios/acessorio-almofada-cazuza.png', 26),
('/projeto_musical/static/img/acessorios/acessorio-caderno-ritalee.png', 27),
('/projeto_musical/static/img/acessorios/acessorios-pin-jao.png', 28),
('/projeto_musical/static/img/acessorios/acessorio-toalha-queen.png', 29),
('/projeto_musical/static/img/acessorios/acessorio-almofada-artistas.png', 30);

-- selects

SELECT cod_produto,
       titulo,
       descricao,
       preco,
       cod_categoria,
       url_foto
FROM tb_produtos
INNER JOIN tb_fotos_produto
ON tb_produtos.cod_produto = tb_fotos_produto.cod_produto;


select * from tb_categorias;
select * from tb_produtos;
select * from tb_fotos_produto;
select * from tb_usuarios;