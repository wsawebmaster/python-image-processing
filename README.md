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

## Links uteis

[pip](https://pip.pypa.io/en/stable/)

[setup.py](https://setuptools.readthedocs.io/en/latest/setuptools.html)

[Testes automatizados](https://docs.pytest.org/en/latest/goodpractices.html)

[Uso do Tox](https://tox.wiki/en/latest/)


## Usar o pacote

	from image_processing.utils impor io, plot
	from image_processing.processing import combination, transformation

	image1 = io.read_image('caminho_fisico_imagem1.jpg')
	image2 = io.read_image('caminho_fisico_imagem2.jpg')

	plot.plot_image(image1)
	plot.plot_image(image2)

	result_image = combination.transfer_histogram(image1, image2)
	plot.plot_result(image1, image2, result_image)



---
---

### 📧 Contato

[LinkedIn](https://www.linkedin.com/in/wsawebmaster/)

[wsawebmaster@yahoo.com.br](mailto:wsawebmaster@yahoo.com.br)