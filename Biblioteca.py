class Livro:
    def __init__(self, titulo, autor, id):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.emprestado = False

    def __str__(self):
        status = "Disponível" if not self.emprestado else "Emprestado"
        return f"{self.titulo} - {self.autor} ({self.id}) - Status: {status}"

class Membro:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        self.historico = []

    def __str__(self):
        return f"{self.nome} - Número de Membro: {self.numero}"

class Biblioteca:
    def __init__(self):
        self.catalogo = {}
        self.membros = {}

    def adicionar_livro(self, livro):
        self.catalogo[livro.id] = livro

    def adicionar_membro(self, membro):
        self.membros[membro.numero] = membro

    def emprestar_livro(self, livro_id, numero_membro):
        livro = self.catalogo.get(livro_id)
        membro = self.membros.get(numero_membro)
        if livro and membro and not livro.emprestado:
            livro.emprestado = True
            membro.historico.append(livro)
            return True
        return False

    def devolver_livro(self, livro_id, numero_membro):
        livro = self.catalogo.get(livro_id)
        membro = self.membros.get(numero_membro)
        if livro and membro and livro.emprestado:
            livro.emprestado = False
            membro.historico.remove(livro)
            return True
        return False

    def pesquisar_livro(self, **kwargs):
        resultados = []
        for livro in self.catalogo.values():
            match = True
            for key, value in kwargs.items():
                if getattr(livro, key) != value:
                    match = False
                    break
            if match:
                resultados.append(livro)
        return resultados

# Exemplo de uso:
if __name__ == "__main__":
    biblioteca = Biblioteca()

    livro1 = Livro("A Guerra dos Tronos", "George R. R. Martin", 1)
    livro2 = Livro("O Hobbit", "J.R.R. Tolkien", 2)
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)

    membro1 = Membro("João", 123)
    membro2 = Membro("Maria", 456)
    biblioteca.adicionar_membro(membro1)
    biblioteca.adicionar_membro(membro2)

    biblioteca.emprestar_livro(1, 123)
    biblioteca.emprestar_livro(2, 456)

    print("Livros disponíveis:")
    for livro in biblioteca.catalogo.values():
        print(livro)

    print("\nMembros da biblioteca:")
    for membro in biblioteca.membros.values():
        print(membro)

    print("\nPesquisa por autor:")
    resultados = biblioteca.pesquisar_livro(autor="J.R.R. Tolkien")
    for livro in resultados:
        print(livro)

    print("\nDevolvendo livro:")
    biblioteca.devolver_livro(2, 456)
    print("Livros disponíveis após devolução:")
    for livro in biblioteca.catalogo.values():
        print(livro)
