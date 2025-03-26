# 📂 Desenvolvendo um Pacote de Processamento de Imagens com Python e publicando no Pypi

## 📃 Descrição

Desenvolvido durante participação do Bootcamp Suzano - Python Developer na plataforma DIO
O pacote image_processing é usado para:
	Processamento:
		- Correspondência de histograma
		- Similaridade estrutural
		- Redimensionar imagem
	Utilitários:
		- Ler imagem
		- Salvar imagem
		- Plotar imagem
		- Plotar resultado
		- Plotar histograma

## 🚀 Tecnologias Utilizadas

- Python
- Pypi
- Setuptools
- Twine
- Git e Github

## Links uteis de documentação

[pip](https://pip.pypa.io/en/stable/) para instalar o package_name
[setup.py](https://setuptools.readthedocs.io/en/latest/setuptools.html)

### Comandos de instalação

	pip install -r requirements.txt

	python -m pip install --upgrade pip
	python -m pip install --user twine
	python -m pip install --user setuptools

### Comando para criar distribuições

	python setup.py sdist bdist_wheel

## Passos para subir o pacote

1 - Criar conta no [Test Pypi](https://test.pypi.org/account/register/)
2 - Publicar no Test Pypi

	python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

3 - Instalar pacote usando Test Pypi

	pip install --index-url https://test.pypi.org/simple/python-image-processing

4 - Testar pacote
5 - Criar conta no [Pypi](https://pypi.org/account/register/)
6 - Publicar no Pypi

	python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

7 - Instalar pacote usando Pypi

	python -m pip install python-image-processing

---
---

### 📧 Contato

[LinkedIn](https://www.linkedin.com/in/wsawebmaster/)

[wsawebmaster@yahoo.com.br](mailto:wsawebmaster@yahoo.com.br)