-- Criar o banco de dados

CREATE DATABASE IF NOT EXISTS 
db_nomedosite;

USE db_nomedosite;

-- Tabela de produtos

CREATE TABLE tb_produtos (    
cod_produto INT AUTO_INCREMENT PRIMARY KEY,    
imagem_produto VARCHAR(255) NOT NULL,    
titulo VARCHAR(80) NOT NULL,   
descricao VARCHAR(200) NOT NULL,    
preco DECIMAL(10,2) NOT NULL,    
categoria VARCHAR(20) NOT NULL);

-- Tabela de usuários

CREATE TABLE tb_usuarios (    
id_usuario INT AUTO_INCREMENT PRIMARY KEY,    
usuario VARCHAR(40) NOT NULL UNIQUE,    
nome_pessoa VARCHAR(80) NOT NULL,    
senha VARCHAR(255) NOT NULL);

-- Tabela do carrinho

CREATE TABLE tb_carrinho (    
id INT AUTO_INCREMENT PRIMARY KEY,    
id_usuario INT NOT NULL,    
cod_produto INT NOT NULL,       
FOREIGN KEY (id_usuario) REFERENCES tb_usuarios(id_usuario),    
FOREIGN KEY (cod_produto) REFERENCES tb_produtos(cod_produto));

-- Tabela de comentários

CREATE TABLE tb_comentario (    
id_comentario INT AUTO_INCREMENT PRIMARY KEY,    
id_usuario INT NOT NULL,    
cod_produto INT NOT NULL,    
comentario TEXT NOT NULL,    
data_comentario DATETIME NOT NULL,    
FOREIGN KEY (id_usuario) REFERENCES tb_usuarios(id_usuario),    
FOREIGN KEY (cod_produto) REFERENCES tb_produtos(cod_produto));

-- Pensamentos para fazer aparecer o produto que o usuario add no carrinho

SELECT tb_usuarios.usuario, tb_produtos.titulo, tb_produtos.precoFROM     
tb_carrinho INNER JOIN tb_usuarios ON tb_carrinho.id_usuario = tb_usuarios.id_usuario INNER JOIN     
tb_produtos ON tb_carrinho.cod_produto = tb_produtos.cod_produtoWHERE     
tb_usuarios.usuario = 'nomedeusuario';