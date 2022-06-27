# Comando para configurar usuário em um novo computador

git config --global user.name "Fulano de Tal" # Configurar nome de usuário
git config --global user.email "Fulano de Tal" # Configurar email

# Iniciar um novo projeto git 

git init 

# Conectar repositório local a um repositório remoto

git remote add origin {URL}

# Adicionar arquivo especifico no repositório

git add {filename or folder}

# Adicionar todos os arquivos de uma pasta 

git add .

# Adicionar comentário (commit)

git commit -m "{meu comentário}"

# Enviar mudanças para a branch remota no reposiório remoto

git push origin {branch}

# Criar nova branch 

git checkout -b "{branch name}"

# Mudar para branch local

git switch {branch name}

# Visualizar branch atual

git branch

OBS: Todas adição de novos arquivos, devem conter comentários.