-- Cria o banco de dados
CREATE DATABASE petCDL;

-- Seleciona o banco de dados para uso
USE petshopcdl;

-- Criação da tabela 'tutors' (Tutores dos pets)
CREATE TABLE tutors (
    id INT AUTO_INCREMENT PRIMARY KEY, -- ID único para cada tutor
    name VARCHAR(100) NOT NULL,        -- Nome do tutor
    contact VARCHAR(50) NOT NULL      -- Contato (telefone ou email)
);

-- Criação da tabela 'pets' (Informações dos pets)
CREATE TABLE pets (
    id INT AUTO_INCREMENT PRIMARY KEY, -- ID único para cada pet
    name VARCHAR(100) NOT NULL,        -- Nome do pet
    species VARCHAR(50) NOT NULL,      -- Espécie (ex.: Cachorro, Gato)
    age INT NOT NULL,                  -- Idade do pet
    tutor_id INT,                      -- ID do tutor relacionado
    FOREIGN KEY (tutor_id) REFERENCES tutors(id) -- Chave estrangeira para a tabela 'tutors'
);

-- Criação da tabela 'consultations' (Consultas dos pets)
CREATE TABLE consultations (
    id INT AUTO_INCREMENT PRIMARY KEY, -- ID único para cada consulta
    pet_id INT NOT NULL,               -- ID do pet relacionado
    date DATE NOT NULL,                -- Data da consulta
    description TEXT NOT NULL,         -- Descrição da consulta
    FOREIGN KEY (pet_id) REFERENCES pets(id) -- Chave estrangeira para a tabela 'pets'
);

-- Inserção de dados iniciais para teste (opcional)
INSERT INTO tutors (name, contact) VALUES
('João Silva', '123456789'),
('Maria Oliveira', '987654321');

INSERT INTO pets (name, species, age, tutor_id) VALUES
('Rex', 'Cachorro', 5, 1),
('Mimi', 'Gato', 3, 2);

INSERT INTO consultations (pet_id, date, description) VALUES
(1, '2024-11-25', 'Vacinação contra raiva.'),
(2, '2024-11-26', 'Consulta geral.');
