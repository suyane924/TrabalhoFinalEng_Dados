from faker import Faker
import pandas as pd
import random
from datetime import timedelta

# Inicializar o Faker
fake = Faker()
Faker.seed(0)

# Funções para gerar dados
def generate_client_data(n=10000):
    data = {
        "id_cliente": range(1, n+1),
        "nome": [fake.name() for _ in range(n)],
        "email": [fake.email() for _ in range(n)],
        "data_criacao": [fake.date_between(start_date='-3y', end_date='today') for _ in range(n)],
    }
    return pd.DataFrame(data)

def generate_categories(n=50):
    data = {
        "id_categoria": range(1, n+1),
        "nome": [fake.word().capitalize() for _ in range(n)],
        "descricao": [fake.sentence(nb_words=6) for _ in range(n)],
    }
    return pd.DataFrame(data)

def generate_products(n=10000, categories=None):
    if categories is None:
        categories = range(1, 51)  # Se não for passado um argumento de categorias, usa de 1 a 50
    
    data = {
        "id_produto": range(1, n+1),
        "nome": [fake.word().capitalize() for _ in range(n)],
        "preco": [round(random.uniform(10, 500), 2) for _ in range(n)],
        "estoque": [random.randint(0, 200) for _ in range(n)],
        "id_categoria": [random.choice(categories) for _ in range(n)],
    }
    return pd.DataFrame(data)

def generate_orders(n=10000, client_ids=None):
    if client_ids is None:
        client_ids = range(1, 10001)  
    
    data = {
        "id_pedido": range(1, n+1),
        "id_cliente": [random.choice(client_ids) for _ in range(n)],
        "data_pedido": [fake.date_between(start_date='-3y', end_date='today') for _ in range(n)],
        "valor_total": [round(random.uniform(20, 2000), 2) for _ in range(n)],
    }
    return pd.DataFrame(data)

def generate_payments(n=10000, order_ids=None):
    if order_ids is None:
        order_ids = range(1, 10001) 
    
    data = {
        "id_pagamento": range(1, n+1),
        "id_pedido": [random.choice(order_ids) for _ in range(n)],
        "valor_pago": [round(random.uniform(20, 2000), 2) for _ in range(n)],
        "data_pagamento": [fake.date_between(start_date='-3y', end_date='today') for _ in range(n)],
        "metodo_pagamento": [random.choice(["Cartão de Crédito", "Boleto", "Pix", "Cartão de Débito"]) for _ in range(n)],
    }
    return pd.DataFrame(data)

def generate_deliveries(n=10000, order_ids=None):
    if order_ids is None:
        order_ids = range(1, 10001) 
    
    data = {
        "id_entrega": range(1, n+1),
        "id_pedido": [random.choice(order_ids) for _ in range(n)],
        "data_entrega": [fake.date_between(start_date='-3y', end_date='today') for _ in range(n)],
        "status_entrega": [random.choice(["Entregue", "Em trânsito", "Cancelado"]) for _ in range(n)],
        "endereco_entrega": [fake.address() for _ in range(n)],
    }
    return pd.DataFrame(data)

# Gerar dados
clientes = generate_client_data()
categories = generate_categories()
products = generate_products(n=10000, categories=categories['id_categoria'].tolist())  # Ajustando para 10.000 produtos
orders = generate_orders(n=10000)
payments = generate_payments(n=10000, order_ids=orders['id_pedido'].tolist())
deliveries = generate_deliveries(n=10000, order_ids=orders['id_pedido'].tolist())

# Salvar os dados em arquivos CSV
clientes.to_csv('clientes.csv', index=False)
categories.to_csv('categorias.csv', index=False)
products.to_csv('produtos.csv', index=False)  # Tabela de produtos agora com 10.000 linhas
orders.to_csv('pedidos.csv', index=False)
payments.to_csv('pagamentos.csv', index=False)
deliveries.to_csv('entregas.csv', index=False)

print("Arquivos CSV gerados com sucesso!")
